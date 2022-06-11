import pandas as pd
import numpy as np
import re
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
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\enrich_senti_text.txt", 'w', encoding="utf-8") as f:
    for line in a:
        f.write(str(line))
        f.write("\n")


text_ = ""
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\enrich_senti_text.txt", 'r', encoding="utf-8") as fb:
    text_ = fb.read()
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
new_text = re.sub(emoji_pattern, " ", text_)
# # new_text = emoji_pattern.sub(r'', text_) # no emoji

# print(text) # with emoji

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
    
# import emoji

# def extract_emojis(s):
#   return ''.join(c for c in s if c not in emoji.UNICODE_EMOJI['en'])
# # new_text = deEmojify(text_)
# clean_text = extract_emojis(text_)

import re
clean_text = re.sub(r'[^\x00-\x7f]',r' ',text_)  

with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\clean_enrich_senti_text.txt", 'w', encoding="utf-8") as fb:
    fb.write(clean_text)