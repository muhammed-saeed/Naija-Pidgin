from cgi import test
import os
mt_files = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\train_val_test_text_files\\"

pcm_total_data = ""
en_total_data = ""

pcm_shuffled_data  = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\pcm_shuffled.txt"
en_shuffled_data = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\en_shuffled.txt"
with open(pcm_shuffled_data,"r", encoding="utf-8") as fb:
    pcm_total_data = fb.readlines()

with open(en_shuffled_data,"r", encoding="utf-8") as fb:
    en_total_data = fb.readlines()




test_lines = int(.15*len(en_total_data))
val_lines = 2*test_lines
mt_files_train = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\train\\"
mt_files_test = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\test\\"
mt_files_val = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\val\\"

en_train_path= mt_files_train + "train.lc.norm.tok.en"
en_val_path = mt_files_val+"val.lc.norm.tok.en"
en_test_path = mt_files_test+ "test.lc.norm.tok.en"
with open(en_test_path,"w", encoding="utf-8") as fb:
    # test_data = en_total_data[len(en_total_data)-val_lines-test_lines:]
    test_data = en_total_data[-test_lines:]

    fb.writelines(test_data)
    print(f"len test data {len(test_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))

with open(en_val_path,"w", encoding="utf-8") as fb:
    # val_data = en_total_data[len(en_total_data)-val_lines: len(en_total_data)-val_lines+test_lines]
    val_data = en_total_data[-val_lines:-test_lines]
    fb.writelines(val_data)
    print(f"len val data {len(val_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))
with open(en_train_path,"w", encoding="utf-8") as fb:
    # train_data = en_total_data[:len(en_total_data)-val_lines-test_lines]
    train_data = en_total_data[:-val_lines]
    fb.writelines(train_data)
    print(f"len train data {len(train_data)} and len of total_data is {len(en_total_data)}")
    # print(len(en_total_data))


###############################################

pcm_train_path= mt_files_train + "train.lc.norm.tok.pcm"
pcm_val_path = mt_files_val+"val.lc.norm.tok.pcm"
pcm_test_path = mt_files_test+ "test.lc.norm.tok.pcm"
with open(pcm_test_path,"w", encoding="utf-8") as fb:
    # test_data = pcm_total_data[len(pcm_total_data)-val_lines-test_lines:]
    test_data = pcm_total_data[-test_lines:]
    fb.writelines(test_data)
    print( f"len test data {len(test_data)} and len of total_data is {len(pcm_total_data)}")

with open(pcm_val_path,"w", encoding="utf-8") as fb:
    # val_data = pcm_total_data[len(pcm_total_data)-val_lines: len(pcm_total_data)-val_lines+test_lines]
    val_data = pcm_total_data[-val_lines:-test_lines]
    fb.writelines(val_data)
    print(f"len val data {len(val_data)} and len of total_data is {len(pcm_total_data)}")
    # print(len(pcm_total_data))
with open(pcm_train_path,"w", encoding="utf-8") as fb:
    # train_data = pcm_total_data[:len(pcm_total_data)-val_lines-test_lines]
    train_data = pcm_total_data[:-val_lines]
    fb.writelines(train_data)
    print(f"len train data {len(train_data)} and len of total_data is {len(pcm_total_data)}")
    # print(len(pcm_total_data))






# fairseq-train "/home/CE/musaeed/ironside_nmt/pcm_en.tokenized.pcm-en"  --arch transformer   --dropout 0.3   --attention-dropout 0.1   --encoder-embed-dim 300   --encoder-ffn-embed-dim 1024  --encoder-layers 4   --encoder-attention-heads 10  --encoder-learned-pos   --decoder-embed-dim 300   --decoder-ffn-embed-dim 1024   --decoder-layers 4   --decoder-attention-heads 10   --decoder-learned-pos   --max-epoch 350   --optimizer adam   --lr 5e-4   --batch-size 64   --seed 1   --encoder-layerdrop 0.0   --decoder-layerdrop 0.2  --criterion=label_smoothed_cross_entropy --activation-dropout 0.3 --warmup-updates 4000 --source-lang=pcm --target-lang=en --label-smoothing=0.5 --lr-scheduler=inverse_sqrt --save-dir /home/CE/musaeed/ironside_nmt/ --find-unused-parameters  --ddp-backend=no_c10d > /local/home/CE/musaeed/training_log.txt