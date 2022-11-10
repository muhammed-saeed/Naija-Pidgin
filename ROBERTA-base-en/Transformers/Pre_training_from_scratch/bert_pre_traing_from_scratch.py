from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from transformers import BertForMaskedLM
from pathlib import Path
import os
import json

paths = ["/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer(lowercase=True)

# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# model = BertModel.from_pretrained("bert-base-uncased", num_labels=0)
# model =  BertForMaskedLM.from_pretrained("bert-base-uncased")
model_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch-pre-trained_100_epoch/models/model"
tokenizer_folder = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch-pre-trained_100_epoch/models/tokenizer"
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
from transformers import BertForMaskedLM
from transformers import BertConfig


# Set a configuration for our RoBERTa model
# config = RobertaConfig(
#     vocab_size=50_265,
#     max_position_embeddings=514,
#     num_attention_heads=12,
#     num_hidden_layers=6,
#     type_vocab_size=1,
# )
# # Initialize the model from a configuration without pretrained weights
# model = RobertaForMaskedLM(config=config)
# print('Num parameters: ',model.num_parameters())



config = BertConfig(
    vocab_size=50_265,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)
# Initialize the model from a configuration without pretrained weights
model = BertForMaskedLM(config=config)
print('Num parameters: ',model.num_parameters())







from transformers import RobertaTokenizerFast, BertTokenizerFast
from tokenizers import BertWordPieceTokenizer

# Create the tokenizer from a trained one
MAX_LEN = 512
# tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_folder, max_len=MAX_LEN)
# ----------------------------
from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


special_tokens = [
  "[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]", "<S>", "<T>"
]
# if you want to train the tokenizer on both sets
# files = ["train.txt", "test.txt"]
# training the tokenizer on the training set
files = ["/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"]

# 30,522 vocab is BERT's default vocab size, feel free to tweak
vocab_size = 30_522
# maximum sequence length, lowering will result to faster training (when increasing batch size)
max_length = 512
# whether to truncate
truncate_longer_samples = False

# initialize the WordPiece tokenizer
tokenizer = BertWordPieceTokenizer()
# train the tokenizer
tokenizer.train(files=files, vocab_size=vocab_size, special_tokens=special_tokens)
# enable truncation up to the maximum 512 tokens
tokenizer.enable_truncation(max_length=max_length)


# make the directory if not already there
if not os.path.isdir(tokenizer_folder):
  os.mkdir(tokenizer_folder)
# save the tokenizer  
tokenizer.save_model(tokenizer_folder)
# dumping some of the tokenizer config to config file, 
# including special tokens, whether to lower case and the maximum sequence length
with open(os.path.join(tokenizer_folder, "config.json"), "w") as f:
  tokenizer_cfg = {
      "do_lower_case": True,
      "unk_token": "[UNK]",
      "sep_token": "[SEP]",
      "pad_token": "[PAD]",
      "cls_token": "[CLS]",
      "mask_token": "[MASK]",
      "model_max_length": max_length,
      "max_len": max_length,
  }
  json.dump(tokenizer_cfg, f)

# when the tokenizer is trained and configured, load it as BertTokenizerFast
tokenizer = BertTokenizerFast.from_pretrained(tokenizer_folder)




# tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_folder, max_len=MAX_LEN)




#*************************


from transformers import RobertaTokenizer, RobertaForMaskedLM, BertTokenizer

# tokenizer = BertTokenizer(tokenizer_folder, max_len=MAX_LEN)
mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
# tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
# model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

# tokenizer = PreTrainedTokenizerFast("/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch-pre-trained_100_epoch/models/tokenizer/vocab.json")
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
    output_dir="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch-pre-trained_100_epoch",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_device_train_batch_size=32,
    save_steps=500,
    save_total_limit=2,
    seed=1,
    report_to="wandb",
    run_name="BE scratch pre-training using Transfomers on PCM Data 100 epoch" 
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)
trainer.train()

trainer.save_model("/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch_pretraining_trainer_saved_100_epochs")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="/home/CE/musaeed/ROBERTA-base-en/Transformers/Pre_training_from_scratch/bert-scratch_pretraining_trainer_saved_100_epochs",
    tokenizer="roberta-base"
)
fill_mask("Send these <mask> back!")