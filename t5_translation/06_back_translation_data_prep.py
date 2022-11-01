import os
import pandas as pd

# real_pcm_path = "/home/CE/musaeed/t5_translation/backtranslation/pcmreal_enbt/pcm_entire_mono.txt"
# bt_en_path = "/home/CE/musaeed/t5_translation/backtranslation/pcmreal_enbt/pcmreal2en.txt"
bt_pcm_path = "/home/CE/musaeed/t5_translation/backtranslation/enreal_pcmbt/enreal2pcm.txt"
real_en = '/home/CE/musaeed/t5_translation/backtranslation/enreal_pcmbt/train.en'
def prepare_translation_datasets():
    with open(bt_pcm_path, "r", encoding="utf-8") as f:
        pcm_text = f.readlines()
        pcm_text = [text.strip("\n") for text in pcm_text]

    with open(real_en, "r") as f:
        english_text = f.readlines()
        english_text = [text.strip("\n") for text in english_text]

    data = []
    for pcm, english in zip(pcm_text, english_text):
        data.append(["translate pcm to english", pcm, english])
        data.append(["translate english to pcm", english, pcm])

    train_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])


    return train_df

train_df = prepare_translation_datasets()
train_df.to_csv("/home/CE/musaeed/t5_translation/backtranslation/enreal_pcmbt/enreal_pcmbt_train.tsv", sep="\t",index = False)
# eval_df.to_csv("/home/CE/musaeed/t5_translation/data/tsv/eval.tsv", sep="\t", index= False)