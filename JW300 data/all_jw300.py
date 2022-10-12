en_train = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\train\train.en"
pcm_train = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\train\train.pcm"
en_test = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\test\test.en"
pcm_test = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\test\test.pcm"
en_val = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\val\val.en"
pcm_val = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\val\val.pcm"

en_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300\jw300.en"
pcm_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300\jw300.pcm"
en = open(en_train,"r", encoding="utf-8").readlines()
en.extend(open(en_test,"r", encoding="utf-8").readlines())
en.extend(open(en_val,"r", encoding="utf-8").readlines())

pcm = open(pcm_train,"r", encoding="utf-8").readlines()
pcm.extend(open(pcm_test,"r", encoding="utf-8").readlines())
pcm.extend(open(pcm_val,"r", encoding="utf-8").readlines())

print(f"the length of the en is {len(en)} and the lenght of pcm is {len(pcm)}")

with open(en_jw300, "w", encoding="utf-8") as fb:
    fb.writelines(en)

with open(pcm_jw300, "w", encoding="utf-8") as fb:
    fb.writelines(pcm)    