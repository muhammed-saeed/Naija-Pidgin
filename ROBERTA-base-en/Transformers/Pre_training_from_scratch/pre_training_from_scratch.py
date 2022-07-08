from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from pathlib import Path

paths = ["/content/train_file.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer(lowercase=True)


tokenizer_folder = "/content/models/tokenizer"
# Customize training
tokenizer.train(files=paths, vocab_size=50_260, min_frequency=2,
                show_progress=True,
                special_tokens=[
                                "<s>",
                                "<pad>",
                                "</s>",
                                "<unk>",
                                "<mask>",
])
#Save the Tokenizer to disk
tokenizer.save_model(tokenizer_folder)

from transformers import RobertaConfig
from transformers import RobertaForMaskedLM

# Set a configuration for our RoBERTa model
config = RobertaConfig(
    vocab_size=50_260,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)
# Initialize the model from a configuration without pretrained weights
model = RobertaForMaskedLM(config=config)
print('Num parameters: ',model.num_parameters())

from transformers import RobertaTokenizerFast
# Create the tokenizer from a trained one
MAX_LEN = 512
tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_folder, max_len=MAX_LEN)

from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, df, tokenizer):
        # or use the RobertaTokenizer from `transformers` directly.
        self.examples = []
        # For every value in the dataframe 
        for example in df.values:
            # 
            x=tokenizer.encode_plus(example, max_length = MAX_LEN, truncation=True, padding=True)
            self.examples += [x.input_ids]

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        # We’ll pad at the batch level.
        return torch.tensor(self.examples[i])
      



import pandas as pd
train_df = pd.read_csv("/content/train_file.txt", on_bad_lines='skip', header=None)
test_df = pd.read_csv("/content/train_file.txt", on_bad_lines='skip', header=None)



# Create the train and evaluation dataset
train_dataset = CustomDataset(train_df[0], tokenizer)
eval_dataset = CustomDataset(test_df[0], tokenizer)


from transformers import DataCollatorForLanguageModeling

# Define the Data Collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)


import torch
from transformers import Trainer, TrainingArguments
# Define the training arguments
model_folder = "/content/models/model"
TRAIN_EPOCHS= 10
VALID_BATCH_SIZE = 8
TRAIN_BATCH_SIZE = 16
WEIGHT_DECAY = 0.0
LEARNING_RATE = 1e-3
training_args = TrainingArguments(
    output_dir=model_folder,
    overwrite_output_dir=True,
    evaluation_strategy = 'epoch',
    num_train_epochs=TRAIN_EPOCHS,
    learning_rate=LEARNING_RATE,
    weight_decay=WEIGHT_DECAY ,
    per_device_train_batch_size=TRAIN_BATCH_SIZE ,
    per_device_eval_batch_size=VALID_BATCH_SIZE ,
    save_steps=8192,
    #eval_steps=4096,
    save_total_limit=1,
)
# Create the trainer for our model
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    #prediction_loss_only=True,
)
# Train the model
trainer.train()




