import encodings
import random

entire_bible_path_en = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_entire_bible_2.txt"
entire_bible_path_pcm = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\pcm_entire_bible_2.txt"

train_en_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\train\train.en"
train_pcm_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\train\train.pcm"

test_en_path  = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\test\test.en"
test_pcm_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\test\test.pcm"

val_en_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\val\val.en"
val_pcm_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\nmt_only_bible\val\val.pcm"

our_en = []
our_pcm = []

with open(entire_bible_path_en, "r", encoding="utf-8") as fb:
    our_en = fb.readlines()

with open(entire_bible_path_pcm, "r", encoding="utf-8") as fb:
    our_pcm = fb.readlines()

temp = list(zip(our_pcm, our_en))
random.shuffle(temp)
res1, res2 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
our_pcm, our_en = list(res1), list(res2)

with open(val_en_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_en[:int(len(our_en)*.15)])

with open(val_pcm_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_pcm[:int(len(our_pcm)*.15)])
#####################
with open(test_pcm_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_pcm)

with open(test_en_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_en)
###########
with open(train_en_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_en)


with open(train_pcm_path, "w", encoding="utf-8") as fb:
    fb.writelines(our_pcm)