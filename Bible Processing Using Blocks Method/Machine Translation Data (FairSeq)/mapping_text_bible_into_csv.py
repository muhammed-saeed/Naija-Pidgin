from base64 import encode
import csv
import encodings
from operator import index
import pandas as pd

en_entire_bible = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_entire_bible_2.txt"
df = pd.read_fwf(en_entire_bible)
csv_bible = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\en_bible.csv"
df.to_csv(csv_bible, index=0)

pcm_entire_bible = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\pcm_entire_bible_2.txt"
df = pd.read_fwf(pcm_entire_bible, encoding="utf-8")
csv_bible = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\csv_files\pcm_bible.csv"

df.to_csv(csv_bible, index=0)