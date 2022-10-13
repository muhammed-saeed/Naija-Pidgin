from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from pathlib import Path
from transformers import BartTokenizerFast

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "5"
paths = ["/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/real_data/pcm_entire_mono.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer(lowercase=True)
MAX_LEN=512
# tokenizer = BartTokenizerFast.from_pretrained("facebook/bart-base", max_len=MAX_LEN)


model_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bart_pretraining_scratch_pcm/bart-scratch-pre-trained_100_epoch/model/model"
tokenizer_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bart_pretraining_scratch_pcm/bart-scratch-pre-trained_100_epoch/model/tokenizer"
mono_pcm_file = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/real_data/pcm_entire_mono.txt"


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
from transformers import BartModel, BartConfig
from transformers import BartTokenizerFast
from transformers import BartTokenizer, BartForCausalLM


config = BartConfig.from_pretrained("facebook/bart-base")
model = BartForCausalLM(config=config)
# # Set a configuration for our RoBERTa model
# config = RobertaConfig(
#     vocab_size=50_265,
#     max_position_embeddings=514,
#     num_attention_heads=12,
#     num_hidden_layers=6,
#     type_vocab_size=1,
# )
# # Initialize the model from a configuration without pretrained weights
# model = RobertaForMaskedLM(config=config)
print('Num parameters: ',model.num_parameters())



# from transformers import RobertaTokenizerFast
# Create the tokenizer from a trained one
MAX_LEN = 512
tokenizer = BartTokenizerFast.from_pretrained(tokenizer_folder, max_len=MAX_LEN)
# tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_folder, max_len=MAX_LEN)




#*************************


from transformers import RobertaTokenizer, RobertaForMaskedLM


mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/real_data/pcm_entire_mono.txt"
# tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
# model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= mono_path,
    block_size=32,
)
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bart_pretraining_scratch_pcm/bart-scratch-pre-trained_100_epoch",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_device_train_batch_size=32,
    save_steps=500,
    save_total_limit=2,
    seed=1,
    report_to="wandb",
    run_name="BART scratch pre-training using Transfomers on PCM Data 100 epoch" 
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)
trainer.train()

trainer.save_model("/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bart_pretraining_scratch_pcm/bart-scratch-pretraining_traininer_folder")

# from transformers import pipeline

# fill_mask = pipeline(
#     "fill-mask",
#     model="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bart_pretraining_scratch_pcm/bart-scratch-pretraining_traininer_folder",
#     tokenizer="roberta-base"
# )
# fill_mask("Send these <mask> back!")
