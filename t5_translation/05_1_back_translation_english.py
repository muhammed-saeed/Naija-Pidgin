import os
import pandas as pd

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3,4"
import logging
import sacrebleu
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = T5Args()
model_args.max_length = 198
model_args.length_penalty = 1
model_args.fp16=False
model_args.eval_batch_size=16
model_args.num_beams = 10
model_args.n_gpu=3





def prepare_translation_datasets(data_path):
    with open(os.path.join(data_path, "back_translation.pcm"), "r", encoding="utf-8") as f:
        pcm_text = f.readlines()
        pcm_text = [text.strip("\n") for text in pcm_text]

    with open(os.path.join(data_path, "back_translation.en"), "r") as f:
        english_text = f.readlines()
        english_text = [text.strip("\n") for text in english_text]

    data = []
    for pcm, english in zip(pcm_text, english_text):
        data.append(["translate pcm to english", pcm, english])
        data.append(["translate english to pcm", english, pcm])

    train_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])




# model_output_dir = "/home/CE/musaeed/t5_translation/output_dir/checkpoint-4996-epoch-1"
# model_output_dir = "/home/CE/musaeed/t5_translation/output_using_the_prefix_for_training/checkpoint-37470-epoch-6"
model_output_dir = "/home/CE/musaeed/t5_translation/contine_epoch_5_output_using_the_prefix_for_training_mt_small/checkpoint-74940-epoch-7"
model = T5Model("mt5", model_output_dir, args=model_args, cuda_devices=[2,3,4])

# eval_df = pd.read_csv("/home/CE/musaeed/Naija-Pidgin/t5_translation/data/tsv/eval.tsv", sep="\t").astype(str)

# pcm_truth = [eval_df.loc[eval_df["prefix"] == "translate english to pcm"]["target_text"].tolist()]
# to_pcm = eval_df.loc[eval_df["prefix"] == "translate english to pcm"]["input_text"].tolist()
# pcm_truth_list = eval_df.loc[eval_df["prefix"] == "translate english to pcm"]["target_text"].tolist()

# english_truth = [eval_df.loc[eval_df["prefix"] == "translate pcm to english"]["target_text"].tolist()]
# to_english = eval_df.loc[eval_df["prefix"] == "translate pcm to english"]["input_text"].tolist()
# english_truth_list = eval_df.loc[eval_df["prefix"] == "translate pcm to english"]["target_text"].tolist()

pcm_mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
english_mono_path = "/home/CE/musaeed/t5_translation/ende/train.en"
# english_mono_path = "/home/CE/musaeed/t5_translation/english_back_translation/newfile.txt"
english_data = open(english_mono_path,"r").readlines()
to_pcm = [line.lower() for line in english_data]

en2pcm = "translate english to pcm: "
pcm2en = "translate pcm to english: "
# to_pcm_ = [en2pcm + s for s in to_pcm]
to_pcm_  = [en2pcm + s for s in to_pcm]


print(f"the english data is {to_pcm[:10]}")
print("#################################################")
# string_ = " ".join(pcm_truth[0])
# lines = pcm_truth[0].split(",")
# print(f"the lenght of pcm_truth is {len(pcm_truth_list)}")
# print(f"examples of pcm_truth {pcm_truth}")

# Predict
# pcm_preds = model.predict(to_pcm_)







en2pcm = "translate english to pcm: "
pcm2en = "translate pcm to english: "



print(f"the english data is {to_pcm[:10]}")
print("#################################################")
# string_ = " ".join(pcm_truth[0])
# lines = pcm_truth[0].split(",")
# print(f"the lenght of pcm_truth is {len(pcm_truth_list)}")
# print(f"examples of pcm_truth {pcm_truth}")

# Predict
pcm_preds = model.predict(to_pcm_)

with open("/home/CE/musaeed/t5_translation/backtranslation/EN2DEenreal2pcm.txt","w", encoding="utf-8") as fb:
    for line in pcm_preds:
        fb.write(line)
        fb.write("\n")

