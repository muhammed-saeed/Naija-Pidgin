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

