train_en = r"C:\Users\lst\Desktop\Naija-Pidgin\JW300 data\train\train.en"
test_en = r"C:\Users\lst\Desktop\Naija-Pidgin\JW300 data\test\test.en"
val_en = r"C:\Users\lst\Desktop\Naija-Pidgin\JW300 data\val\val.en"
data_le = None
len__ = 0
data_le = open(train_en, "r", encoding="utf-8")
len__ += len(data_le.readlines())
data_le = open(test_en, "r", encoding="utf-8")
len__ += len(data_le.readlines())
data_le = open(val_en, "r", encoding="utf-8")
len__ += len(data_le.readlines())
print(len__)
