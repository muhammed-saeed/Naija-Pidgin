import pandas as pd
import numpy as np
dev_path =  r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\Nigerian Pidgin Tweets and Sentiment.csv"
train_path = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\14000 Nigerian Pidgin Tweets and Sentiments.csv"
test = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\pcm_test.csv"

df_dev = pd.read_csv(dev_path)
df_train = pd.read_csv(train_path)
# df_test = pd.r(test_path)
df_dev = df_dev.rename(columns={'Pidgin Tweets':'text'})
df_train = df_train.rename(columns={'Clean_Content':'text','Human_Label':'Sentiment'})

entire_df = pd.concat([df_dev,df_train], axis=0)
entire_df = entire_df.dropna()
entire_df = entire_df['text']
print(df_dev.head())
print("###################")
print(df_train.head())
print("#########################")
print(entire_df.head())
a = entire_df.values
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\senti_text.txt", 'w', encoding="utf-8") as f:
    for line in a:
        f.write(str(line))
        f.write("\n")
