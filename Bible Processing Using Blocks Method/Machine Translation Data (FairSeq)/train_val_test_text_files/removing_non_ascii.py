from base64 import encode
import re
path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\pcm_shuffled.txt"
def clean_str(s):
    res = re.sub(r'[^\x00-\x7F]+',' ', s)
    #the clear string takes the string and read the entire string if the character not in ascii replace with space
    res = re.sub(r' +',' ', res)
    #to ensure that there are no many spaceses after each other do " ', ' ' "
    return res

with open(path, "r", encoding="utf-8") as f:
    lines = f.read()
    cleaned_lines = clean_str(lines)
    with open(path, "w") as o:
        o.write(cleaned_lines)

data = ""
with open(path, "r") as fb:
    data =fb.read()
