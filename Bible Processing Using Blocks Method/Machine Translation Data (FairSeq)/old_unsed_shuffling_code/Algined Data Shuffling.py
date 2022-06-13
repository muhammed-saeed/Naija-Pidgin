import pandas as pd
parrellel_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\parraellel.csv"
df_1 = pd.read_csv(r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\en_bible.csv")
df_2 = pd.read_csv(r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\pcm_bible.csv")
df_3 = pd.DataFrame(columns=["English","Pcm"])
# print(df_1.columns)
# print(df_2.columns)
df_3["English"] = df_1["At the first God made the heaven and the earth."]
df_3["Pcm"] = df_2["Wen di world just start, na God kreate di heaven and di eart."]
df_3 = df_3.sample(frac=1)
df_3.to_csv(parrellel_path, index=0)

