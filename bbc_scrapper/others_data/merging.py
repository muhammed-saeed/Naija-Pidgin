train= r"C:\Users\lst\Desktop\Naija-Pidgin\bbc_scrapper\others_data\train.txt"
data_1 = ""
eval = r"C:\Users\lst\Desktop\Naija-Pidgin\bbc_scrapper\others_data\eval.txt"
data_2 = ""
with open(train, "r", encoding="utf8") as fb:
    data_1 = fb.read()
with open(eval, "r", encoding="utf8") as fb:
    data_2 = fb.read()

total = data_1 + "\n" + data_2
merged_data =  r"C:\Users\lst\Desktop\Naija-Pidgin\bbc_scrapper\others_data\merged.txt"

with open(merged_data, "w") as fb:
    fb.write(total)
