import glob
import os
pcm_mono_path = "/home/CE/musaeed/pcm_roberta/pcm_text.txt"
from pathlib import Path
from tokenizers import ByteLevelBPETokenizer

# os.chdir(r'/content/drive/MyDrive/Naijia Project/mono-pcm/')
# paths = glob.glob('*.txt')
# # Initialize a tokenizer
# tokenizer = ByteLevelBPETokenizer()
# paths_new= [ pcm_mono_path + x  for x in paths]
# print(paths_new)
# # Customize training
tokenizer = ByteLevelBPETokenizer()

tokenizer.train(files=["/home/CE/musaeed/pcm_roberta/pcm_text.txt"], vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])
import os
try:
    os.mkdir("/home/CE/musaeed/pcm_roberta/RoBERTa/")
except FileExistsError:
    print("File already exsist in location ")
token_dir = "/home/CE/musaeed/pcm_roberta/RoBERTa/"
if not os.path.exists(token_dir):
  os.makedirs(token_dir)
tokenizer.save_model(token_dir)


# pip install git+https://github.com/huggingface/transformers
# pip list | grep -E 'transformers|tokenizers'