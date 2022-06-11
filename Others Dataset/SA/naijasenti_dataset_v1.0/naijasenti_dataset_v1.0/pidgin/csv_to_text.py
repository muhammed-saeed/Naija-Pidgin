import pandas as pd
import numpy as np
dev_path = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\pcm_dev.csv"
train_path = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\pcm_train.csv"
test_path = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\pcm_test.csv"

df_dev = pd.read_csv(dev_path)
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

entire_df = pd.concat([df_dev,df_train, df_test], axis=0)
entire_df = entire_df.dropna()
entire_df = entire_df['text']
a = entire_df.values
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\senti_text.txt", 'w', encoding="utf-8") as f:
    for line in a:
        f.write(str(line))
        f.write("\n")
