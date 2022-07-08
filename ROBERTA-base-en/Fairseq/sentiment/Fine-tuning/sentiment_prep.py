import pandas as pd
import numpy as np
train_df_path = "/home/CE/musaeed/pcm_roberta/senti_data/pcm_train.csv"
dev_df_path = "/home/CE/musaeed/pcm_roberta/senti_data/pcm_dev.csv"
test_df_path = "/home/CE/musaeed/pcm_roberta/senti_data/pcm_test.csv"

train_bpe_text_path = "/home/CE/musaeed/pcm_roberta/pcm_senti/train.input0"
train_bpe_label_path = "/home/CE/musaeed/pcm_roberta/pcm_senti/train.label"

dev_bpe_text_path = "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.input0"
dev_bpe_label_path = "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.label"

train_df = pd.read_csv(train_df_path)
dev_df = pd.read_csv(dev_df_path)
# test_df = pd.read_csv("/content/drive/MyDrive/Naija Project/Sentiment Analysis/shamusdeen data/pcm_test.csv")
frames = [train_df, dev_df]
mapping = {'positive':2, 'negative':0, 'neutral':1}


senti_df = pd.concat(frames)

senti_df = senti_df.replace({'label':mapping})

senti_df = senti_df.sample(frac=1).reset_index()
senti_df = senti_df.dropna()

np.savetxt(train_bpe_text_path, senti_df.text.values, fmt = "%s")
np.savetxt(train_bpe_label_path, senti_df.label.values, fmt = "%d")

test_df = pd.read_csv("/home/CE/musaeed/pcm_roberta/senti_data/pcm_test.csv")
test_df = test_df.replace({'label':mapping})

test_df = test_df.dropna()
np.savetxt(dev_bpe_text_path, test_df.text.values, fmt = "%s")
np.savetxt(dev_bpe_label_path, test_df.label.values, fmt = "%d")
