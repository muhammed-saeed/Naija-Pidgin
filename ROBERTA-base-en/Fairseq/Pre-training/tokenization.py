import glob
import os
pcm_mono_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
from pathlib import Path
from tokenizers import ByteLevelBPETokenizer


tokenizer = ByteLevelBPETokenizer()
#this vocab size is chosen to generate dict of length 50_260 with preprocess

tokenizer.train(files=["/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"], vocab_size=52_382, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])
import os
try:
    os.mkdir("/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/tokenization_pcm_files/")
except FileExistsError:
    print("File already exsist in location ")
token_dir = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/tokenization_pcm_files/"
if not os.path.exists(token_dir):
  os.makedirs(token_dir)
tokenizer.save_model(token_dir)


# pip install git+https://github.com/huggingface/transformers
# pip list | grep -E 'transformers|tokenizers'