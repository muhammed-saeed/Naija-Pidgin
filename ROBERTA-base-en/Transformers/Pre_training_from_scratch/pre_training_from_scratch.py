from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from pathlib import Path
import os

paths = ["/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer(lowercase=True)

model_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/roberta-scratch-pre-trained_100_epoch/models/model"
tokenizer_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/roberta-scratch-pre-trained_100_epoch/models/tokenizer"
mono_pcm_file = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"


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



# Customize training
tokenizer.train(files=paths, vocab_size=50_265, min_frequency=2,
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
    vocab_size=50_265,
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




#*************************


from transformers import RobertaTokenizer, RobertaForMaskedLM


mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
# tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
# model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= mono_path,
    block_size=64,
)
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/roberta-scratch-pre-trained_100_epoch",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_device_train_batch_size=64,
    save_steps=500,
    save_total_limit=2,
    seed=1,
    report_to="wandb",
    run_name="RoBERTa scratch pre-training using Transfomers on PCM Data 100 epoch" 
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)
trainer.train()

trainer.save_model("/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/roberta-scratch_pretraining_trainer_saved_100_epochs")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/roberta-scratch_pretraining_trainer_saved_100_epochs",
    tokenizer="roberta-base"
)
fill_mask("Send these <mask> back!")