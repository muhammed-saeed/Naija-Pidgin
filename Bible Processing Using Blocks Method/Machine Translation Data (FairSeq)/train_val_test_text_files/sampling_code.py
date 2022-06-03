from cgi import test
import os
mt_files = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_val_test_text_files\\"

pcm_total_data = ""
en_total_data = ""

pcm_shuffled_data  = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\pcm_shuffled.txt"
en_shuffled_data = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\en_shuffled.txt"
with open(pcm_shuffled_data,"r") as fb:
    pcm_total_data = fb.readlines()

with open(en_shuffled_data,"r") as fb:
    en_total_data = fb.readlines()

test_lines = 1200
val_lines = 1200
mt_files_train = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\train\\"
mt_files_test = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\test\\"
mt_files_val = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\val\\"

en_train_path= mt_files_train + "train.lc.norm.tok.en"
en_val_path = mt_files_val+"val.lc.norm.tok.en"
en_test_path = mt_files_test+ "test.lc.norm.tok.en"
with open(en_test_path,"w") as fb:
    test_data = en_total_data[len(en_total_data)-val_lines-test_lines:]
    fb.writelines(test_data)
    print(f"len test data {len(test_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))

with open(en_val_path,"w") as fb:
    val_data = en_total_data[len(en_total_data)-val_lines: len(en_total_data)-val_lines+test_lines]
    fb.writelines(val_data)
    print(f"len test data {len(val_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))
with open(en_train_path,"w") as fb:
    train_data = en_total_data[:len(en_total_data)-val_lines-test_lines]
    fb.writelines(train_data)
    print(f"len test data {len(train_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))


###############################################

pcm_train_path= mt_files_train + "train.lc.norm.tok.pcm"
pcm_val_path = mt_files_val+"val.lc.norm.tok.pcm"
pcm_test_path = mt_files_test+ "test.lc.norm.tok.pcm"
with open(pcm_test_path,"w") as fb:
    test_data = pcm_total_data[len(pcm_total_data)-val_lines-test_lines:]
    fb.writelines(test_data)
    print( f"len test data {len(test_data)} and len of total_data is {len(pcm_total_data)}")

with open(pcm_val_path,"w") as fb:
    val_data = pcm_total_data[len(pcm_total_data)-val_lines: len(pcm_total_data)-val_lines+test_lines]
    fb.writelines(val_data)
    print(f"len test data {len(val_data)} and len of total_data is {len(pcm_total_data)}")
    # print(len(pcm_total_data))
with open(pcm_train_path,"w") as fb:
    train_data = pcm_total_data[:len(pcm_total_data)-val_lines-test_lines]
    fb.writelines(train_data)
    print(f"len test data {len(train_data)} and len of total_data is {len(pcm_total_data)}")
    # print(len(pcm_total_data))


