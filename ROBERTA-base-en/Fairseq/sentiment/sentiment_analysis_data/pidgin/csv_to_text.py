import pandas as pd
import numpy as np
dev_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_dev.csv"
train_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_train.csv"
test_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_test.csv"

df_dev = pd.read_csv(dev_path)
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

df_train_text = df_train['text']
df_test_text = df_test['text']
df_dev_text = df_dev['text']


labels_maps = {"positive" : 2,
                     "neutral" : 1,
                     
                     "negative" : 0}

df_dev_label = df_dev['label'].map(labels_maps)
df_train_label = df_train['label'].map(labels_maps)
df_test_label = df_test['label'].map(labels_maps)

# df_dev_label = df_dev['label']
# df_train_label = df_train['label']
# df_test_label = df_test['label']
print(f"the columns in the data frame are {df_train.columns}")
print(f"the values of the label are{df_train.label.values}")
dev_text_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_dev.input0"
train_text_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_train.input0"
test_text_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_test.input0"

dev_label_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_dev.label"
train_label_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_train.label"
test_label_path = "/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_test.label"
with open(dev_text_path,"w", encoding="utf-8") as f:
    a = df_dev_text.values
    for line in a:
        f.write(str(line))
        f.write("\n")

with open(train_text_path,"w", encoding="utf-8") as f:
    a = df_train_text.values
    for line in a:
        f.write(str(line))
        f.write("\n")

with open(test_text_path,"w", encoding="utf-8") as f:
    a = df_test_text.values
    for line in a:
        f.write(str(line))
        f.write("\n")


with open(dev_label_path,"w", encoding="utf-8") as f:
    a = df_dev_label.values
    for line in a:
        f.write(str(line))
        f.write("\n")


with open(train_label_path,"w", encoding="utf-8") as f:
    a = df_train_label.values
    for line in a:
        f.write(str(line))
        f.write("\n")


with open(test_label_path,"w", encoding="utf-8") as f:
    a = df_test_label.values
    for line in a:
        f.write(str(line))
        f.write("\n")

# entire_df = pd.concat([df_dev,df_train, df_test], axis=0)
# entire_df = entire_df.dropna()
# entire_df = entire_df['text']
# a = entire_df.values
# with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\senti_text.txt", 'w', encoding="utf-8") as f:
#     for line in a:
#         f.write(str(line))
#         f.write("\n")
