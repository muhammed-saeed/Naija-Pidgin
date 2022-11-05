import os
import pandas as pd

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = T5Args()
model_args.max_length = 198
model_args.length_penalty = 1
model_args.fp16=False
model_args.eval_batch_size=8
model_args.num_beams = 10
# model_args.n_gpu=3





model_output_dir = "/home/CE/musaeed/checkpoint-124900-epoch-5"
model = T5Model("mt5", model_output_dir, args=model_args, cuda_devices=[4])

pcm_mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
english_mono_path = "/home/CE/musaeed/ende/"
# english_mono_path = "/home/CE/musaeed/t5_translation/english_back_translation/newfile.txt"

def real_data_preperation(english_mono_path):
    english_data = open(english_mono_path,"r").readlines()
    to_pcm = [line.lower() for line in english_data]

    en2pcm = "translate english to pcm: "
    pcm2en = "translate pcm to english: "
    # to_pcm_ = [en2pcm + s for s in to_pcm]
    to_pcm_  = [en2pcm + s for s in to_pcm]


    print(f"the english data is {to_pcm[:10]}")
    print("#################################################")
    return to_pcm_


files = os.listdir(english_mono_path)
print(f"{files}")
output_folder = "/home/CE/musaeed/t5_translation/backtranslation/"
for file in files:
    output_file = output_folder + file + ".txt"
    input_file = english_mono_path + file
    to_pcm_ = real_data_preperation(input_file)
    pcm_preds = model.predict(to_pcm_)

    with open(output_file,"w", encoding="utf-8") as fb:
        for line in pcm_preds:
            fb.write(line)
            fb.write("\n")

