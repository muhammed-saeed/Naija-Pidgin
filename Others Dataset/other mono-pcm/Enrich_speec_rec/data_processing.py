import re 
# >>> x = "This is a sentence. (once a day) [twice a day]"
# >>> re.sub("[\(\[].*?[\)\]]", "", x)
val_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\Validation_Transcribe"
train_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\Train_Transcribe"
test_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\Test_Transcribe"


train_data = ""
test_data = ""
val_data = ""

with open(train_path, "r") as fb:
    train_data = fb.read()
with open(test_path, "r") as fb:
    test_data = fb.read()
with open(val_path, "r") as fb:
    val_data = fb.read()

train_data  = re.sub("\(.*?\)", " ", train_data)
test_data  = re.sub("\(.*?\)", " ", test_data)
val_data  = re.sub("\(.*?\)", " ", val_data)
entire_data = train_data + "\n" + test_data + "\n" + val_data
with open(r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\enrich_spec_rec.txt", "w") as fb:
    fb.write(entire_data)
    fb.write("\n")

