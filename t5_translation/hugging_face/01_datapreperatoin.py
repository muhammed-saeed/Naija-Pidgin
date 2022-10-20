import os
import pandas as pd

def prepare_translation_datasets(data_path):
    with open(os.path.join(data_path, "train.pcm"), "r", encoding="utf-8") as f:
        pcm_text = f.readlines()
        pcm_text = [text.strip("\n") for text in pcm_text]

    with open(os.path.join(data_path, "train.en"), "r") as f:
        english_text = f.readlines()
        english_text = [text.strip("\n") for text in english_text]

    data = []
    for pcm, english in zip(pcm_text, english_text):
        data.append(["translate pcm to english", pcm, english])
        data.append(["translate english to pcm", english, pcm])

    train_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])


    with open(os.path.join(data_path, "val.pcm"), "r", encoding="utf-8") as f:
        pcm_text = f.readlines()
        pcm_text = [text.strip("\n") for text in pcm_text]

    with open(os.path.join(data_path, "val.en"), "r") as f:
        english_text = f.readlines()
        english_text = [text.strip("\n") for text in english_text]

    data = []
    for pcm, english in zip(pcm_text, english_text):
        data.append(["translate pcm to english", pcm, english])
        data.append(["translate english to pcm", english, pcm])
    
    dev_df =  pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])

    train_df_  = pd.concat(
    [train_df, dev_df],
    axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
    )

    with open(os.path.join(data_path, "test.pcm"), "r", encoding="utf-8") as f:
        pcm_text = f.readlines()
        pcm_text = [text.strip("\n") for text in pcm_text]

    with open(os.path.join(data_path, "test.en"), "r") as f:
        english_text = f.readlines()
        english_text = [text.strip("\n") for text in english_text]

    data = []
    for pcm, english in zip(pcm_text, english_text):
        data.append(["translate pcm to english", pcm, english])
        data.append(["translate english to pcm", english, pcm])

    eval_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])

    return train_df_, eval_df

train_df, eval_df = prepare_translation_datasets("/home/CE/musaeed/t5_translation/data")
# train_df.to_csv("/home/CE/musaeed/t5_translation/data/tsv/train.tsv", sep="\t",index = False)
# eval_df.to_csv("/home/CE/musaeed/t5_translation/data/tsv/eval.tsv", sep="\t", index= False)

# print(train_df.head())
train_df.reset_index(inplace=True)
eval_df.reset_index(inplace=True)


train_df.to_json("/home/CE/musaeed/Naija-Pidgin/t5_translation/hugging_face/data/train.json")
eval_df.to_json("/home/CE/musaeed/Naija-Pidgin/t5_translation/hugging_face/data/eval.json")