from tokenizers import ByteLevelBPETokenizer
import glob
import os

os.chdir(r'/home/CE/musaeed/mono-pcm/')
my_files = glob.glob('*.txt')
print(my_files)
paths = my_files
# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=32_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])


import os
os.mkdir('/home/CE/musaeed/RoBERTa')
token_dir = '/home/CE/musaeed/RoBERTa'
if not os.path.exists(token_dir):
  os.makedirs(token_dir)
tokenizer.save_model(token_dir)

#hte merges files contains the sub-words of the strings
#the vocab file contains the indices of the sub-words

from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

tokenizer = ByteLevelBPETokenizer(
    "/home/CE/musaeed/RoBERTa/vocab.json",
    "/home/CE/musaeed/RoBERTa/merges.txt",
)

########################################
tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)

###############################################
#Confgiuration 

from transformers import RobertaConfig
#defining the configurations of the RoBERTA model
#creating the config file
config = RobertaConfig(
    vocab_size=32_000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)
#defining the configurations of the RoBERTA model

config.to_json_file('/home/CE/musaeed/RoBERTa/config.json')

######################
###########
#Loading the bert tokenizers as Roberta ones

from transformers import RobertaTokenizer
tokenizer = RobertaTokenizer.from_pretrained("/home/CE/musaeed/RoBERTa", max_length=512)
#
#loading the tokenizer that we have created above

#################
#initialize the RoBERTA model
from transformers import RobertaForMaskedLM

model = RobertaForMaskedLM(config=config)
print(model)

##########################
#/home/CE/musaeed/pcm_mono.txt

####################################



# from transformers import LineByLineTextDataset

# # dataset = LineByLineTextDataset(
# #     tokenizer=tokenizer,
# #     file_path="/content/drive/MyDrive/Naijia Project/mono-pcm/train.txt",
# #     block_size=128,
# # )

# dataset = LineByLineTextDataset(
#     tokenizer=tokenizer,
#     file_path="/home/CE/musaeed/pcm_mono.txt",
#     block_size=128,
# )
# #The program will now load the dataset line by line for batch training with block_
# #size=128 limiting the length of an ex

# ###########################333

# ####

# from transformers import DataCollatorForLanguageModeling
# #to pre-pare the dataset into batches to be passed to the run_mlm
# data_collator = DataCollatorForLanguageModeling(
#     tokenizer=tokenizer, mlm=True, mlm_probability=0.15
# )


# ######################################
# num_epochs_ = 5
# train_output_path =     "/home/CE/musaeed/RoBERTa/" + str(num_epochs_)
# os.mkdir(train_output_path)

# #############################


# from transformers import Trainer, TrainingArguments

# training_args = TrainingArguments(
#     output_dir=train_output_path,
#     overwrite_output_dir=True,
#     num_train_epochs=num_epochs_,
#     per_device_train_batch_size=64,
#     save_steps=10_000,
#     save_total_limit=2,
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     data_collator=data_collator,
#     train_dataset=dataset,
# )


# #########################################3
# trainer.train()