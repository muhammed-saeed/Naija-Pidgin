import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

pcm_train = "/home/CE/musaeed/ROBERTA-base-en/pidgin/pcm_train.csv"
pcm_dev = "/home/CE/musaeed/ROBERTA-base-en/pidgin/pcm_dev.csv"
pcm_test = "/home/CE/musaeed/ROBERTA-base-en/pidgin/pcm_test.csv"
multi_train_df = pd.read_csv(pcm_train)
multi_dev_df = pd.read_csv(pcm_dev)
multi_test_df = pd.read_csv(pcm_test)
multi_train_df.dropna(inplace=True)
multi_train_df.dropna(inplace=True)
multi_test_df.dropna(inplace=True)

multi_train_df.rename(columns = {'text':'input_text', 'label':'target_text'}, inplace = True)
multi_dev_df.rename(columns = {'text':'input_text', 'label':'target_text'}, inplace = True)
multi_test_df.rename(columns = {'text':'input_text', 'label':'target_text'}, inplace = True)

multi_train_df["prefix"] = "multilabel classification"
multi_dev_df["prefix"] = "multilabel classification"
multi_test_df["prefix"] = "multilabel classification"

multi_train_df = multi_train_df[["prefix", "input_text", "target_text"]]
multi_dev_df = multi_dev_df[["prefix", "input_text", "target_text"]]
multi_test_df = multi_test_df[["prefix", "input_text", "target_text"]]



print(multi_train_df.head())

multi_train_df.to_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/train.tsv", "\t", index=False)
multi_dev_df.to_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/eval.tsv","\t", index=False)
multi_test_df.to_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/test.tsv","\t", index=False)
