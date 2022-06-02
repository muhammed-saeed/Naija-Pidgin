en_path = "C:/Users/lst/Desktop/Naija-Pidgin/BLOCKS_SPANS/BLOCKS_SPANS/en_bible/"
pcm_path = "C:/Users/lst/Desktop/Naija-Pidgin/BLOCKS_SPANS/BLOCKS_SPANS/pcm_bible/"

parrellel_lines = []
# C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_parrellel.txt
new_path = en_path + "/en_parrellel.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_1 = ""
with open(new_path, "r") as fb:
    data_1 = fb.read()


#############################################3
new_path = en_path + "/c_0.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_2 = ""
with open(new_path, "r") as fb:
    data_2 = fb.read()

###################################################
new_path = en_path + "/c_1.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_3 = ""
with  open(new_path, "r") as fb:
    data_3 = fb.read()
###########################################


data_4 = ""
new_path = en_path + "/chapter_19.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

with open(new_path, "r") as fb:
    data_4 = fb.read()

###############################################


new_path = en_path + "en_entire_bible.txt"

total = data_1 + "\n" + data_2 + "\n"  + data_3 + "\n"  +data_4 + "\n" 
# with open(new_path,"w") as fb:
#     for book in parrellel_lines:
#         for line in book:
#             fb.writelines(line)
new_path = en_path + "en_entire_bible_2.txt"

with open(new_path, "w") as fb:
    fb.write(total)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###############

####### for pcm we have the following

new_path = pcm_path + "pcm_parrellel.txt"

data_1 = ""
with open(new_path, "r", encoding="utf8") as fb:
    data_1 = fb.read()


#############################################3
new_path = pcm_path + "/c_0.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_2 = ""
with open(new_path, "r", encoding="utf8") as fb:
    data_2 = fb.read()

###################################################
new_path = pcm_path + "/c_1.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_3 = ""
with  open(new_path, "r", encoding="utf8") as fb:
    data_3 = fb.read()
###########################################


data_4 = ""
new_path = pcm_path + "/chapter_19.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

with open(new_path, "r", encoding="utf8") as fb:
    data_4 = fb.read()

###############################################



total = data_1 + "\n" + data_2 + "\n"  + data_3 + "\n"  +data_4 + "\n" 
# with open(new_path,"w") as fb:
#     for book in parrellel_lines:
#         for line in book:
#             fb.writelines(line)
new_path = pcm_path + "pcm_entire_bible_2.txt"

with open(new_path, "w") as fb:
    fb.write(total)



