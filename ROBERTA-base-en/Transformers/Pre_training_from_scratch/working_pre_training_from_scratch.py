from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from pathlib import Path
import os

paths = ["/home/CE/musaeed/ROBERTA-EN-TRANS/Mono_lingual_data/pcm_entire_mono.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer(lowercase=True)

model_folder = "/home/CE/musaeed/ROBERTA-EN-TRANS/Transformers/Pre_training_from_scratch/models/model"
tokenizer_folder = "/home/CE/musaeed/ROBERTA-EN-TRANS/Transformers/Pre_training_from_scratch/models/tokenizer"
mono_pcm_file = "/home/CE/musaeed/ROBERTA-EN-TRANS/Mono_lingual_data/pcm_entire_mono.txt"


train_data_path = "/home/CE/musaeed/ROBERTA-EN-TRANS/Mono_lingual_data/PLM_DATA/pcm_train_mono.txt"
eval_data_path = "/home/CE/musaeed/ROBERTA-EN-TRANS/Mono_lingual_data/PLM_DATA/pcm_validation_mono.txt"

####


isExist = os.path.exists(model_folder)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(model_folder)
  print("The new directory is created!")


isExist = os.path.exists(tokenizer_folder)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(tokenizer_folder)
  print("The new directory is created!")

##################################

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
# # Create the train and evaluation dataset
# train_dataset = CustomDataset(train_df[0], tokenizer)
# eval_dataset = CustomDataset(test_df[0], tokenizer)


from transformers import LineByLineTextDataset

train_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= train_data_path,
    block_size=64,
)

eval_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= eval_data_path,
    block_size=64,
)

from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import DataCollatorForLanguageModeling

# Define the Data Collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)


import torch
from transformers import Trainer, TrainingArguments
# Define the training arguments

TRAIN_EPOCHS= 100
VALID_BATCH_SIZE = 8
TRAIN_BATCH_SIZE = 8
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
    save_steps=8192,
    eval_steps=4096,
    # per_device_eval_batch_size=VALID_BATCH_SIZE ,
    report_to="wandb",
    run_name="RoBERTa scratch pre-training using Transfomers on PCM Data",
    save_total_limit=1
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

from transformers import pipeline
# Create a Fill mask pipeline
fill_mask = pipeline(
    "fill-mask",
    model=model_folder,
    tokenizer=tokenizer_folder
)
# Test some examples
# knit midi dress with vneckline
# =>
fill_mask("midi <mask> with vneckline.")
# The test text: Round neck sweater with long sleeves
fill_mask("Round neck sweater with <mask> sleeves.")


