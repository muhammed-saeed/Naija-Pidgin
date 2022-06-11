from cgi import test
import os 
dev_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other parrellel data\Tree_bank\pcm_nsc-ud-dev.conllu"
test_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other parrellel data\Tree_bank\pcm_nsc-ud-test.conllu"
train_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other parrellel data\Tree_bank\pcm_nsc-ud-train.conllu"

train_data = []
test_data = []
dev_data = []
with open(train_path, "r") as fb:
    train_data = fb.readlines()
with open(test_path, "r") as fb:
    test_data = fb.readlines()
with open(dev_path, "r") as fb:
    dev_data = fb.readlines()

pcm_data = []
en_data = []
total_data = []
total_data.extend(train_data)
total_data.extend(dev_data)
total_data.extend(test_data)
print(f"total {len(total_data)} train {len(train_data)} test {len(test_data)} dev {len(dev_data)}")
for line in total_data:
    if "text_ortho = " in line:
        pcm_data.append(line[15:])
    if "text_en = " in line:
        en_data.append(line[12:])
print(f"the parrellel pcm is {len(pcm_data)} and the parrellel en is {len(en_data)}")

parrellel_pcm = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other parrellel data\Tree_bank\pcm_parrellel.txt"

parrellel_en = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other parrellel data\Tree_bank\en_parrellel.txt"

with open(parrellel_en, "w") as fb:
    fb.writelines(en_data)
with open(parrellel_pcm, "w") as fb:
    fb.writelines(pcm_data)

print(en_data[0][12:])