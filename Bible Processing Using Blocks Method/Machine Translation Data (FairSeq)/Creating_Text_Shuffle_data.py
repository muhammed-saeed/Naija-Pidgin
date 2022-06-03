import pandas as pd
import numpy as np
parrellel_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\parraellel.csv"
df = pd.read_csv(parrellel_path)
print(df.columns)
pcm_df = df["Pcm"]

a = pcm_df.values
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\pcm_shuffled.txt", 'w', encoding="utf-8") as f:
    for line in a:
        f.write(str(line))
        f.write("\n")

# numpy_array = pcm_df.to_numpy()
# np.savetxt("C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\pcm_shuffled_2.txt",encoding="ISO-8859-1", numpy_array, fmt = "%d")
en_df = df["English"]
a = en_df.values
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\en_shuffled.txt", 'w') as f:
    for line in a:
        f.write(str(line))
        f.write("\n")


