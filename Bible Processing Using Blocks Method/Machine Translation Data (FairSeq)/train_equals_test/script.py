import random
pcm_path = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\pcm_entire_bible_2.txt"
en_path = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_entire_bible_2.txt"

en_data  = []
pcm_data = []

with open(en_path, "r", encoding="utf-8") as fb:
    en_data = fb.readlines()


with open(pcm_path, "r", encoding="utf-8") as fb:
    pcm_data = fb.readlines()

temp = list(zip(pcm_data, en_data))
random.shuffle(temp)
res1, res2 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
our_pcm, our_en = list(res1), list(res2)

dev_data_en = our_en[:1000]
dev_data_pcm = our_pcm[:1000]

train_data_pcm = our_pcm[1000:]
train_data_en = our_en[1000:]


test_en = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\test\test.en"
test_pcm = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\test\test.pcm"

val_en= r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\val\val.en"
val_pcm= r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\val\val.pcm"

train_en = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\train\train.en"
train_pcm= r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_equals_test\train\train.pcm"

with open(test_en, "w", encoding="utf-8") as fb:
    fb.writelines(train_data_en)

with open(test_pcm, "w", encoding="utf-8") as fb:
    fb.writelines(train_data_pcm)

with open(train_en, "w", encoding="utf-8") as fb:
    fb.writelines(train_data_en)

with open(train_pcm, "w", encoding="utf-8") as fb:
    fb.writelines(train_data_pcm)


with open(val_en, "w", encoding="utf-8") as fb:
    fb.writelines(dev_data_en)


with open(val_pcm, "w", encoding="utf-8") as fb:
    fb.writelines(dev_data_pcm)

