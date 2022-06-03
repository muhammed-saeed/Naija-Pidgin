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

path_64 = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\chapters\en_64.txt"
data_chapter_64 = ""
with open(path_64, "r") as fb:
    data_chapter_64 = fb.read()

#######################################3

new_path = en_path + "en_entire_bible.txt"

total = data_1 + "\n" + data_2 + "\n"  + data_3 + "\n"  +data_4 + "\n"  +data_chapter_64
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
with open(new_path, "r", encoding="ISO-8859-1") as fb:
    data_1 = fb.read()


#############################################3
new_path = pcm_path + "/c_0.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_2 = ""
with open(new_path, "r", encoding="ISO-8859-1'") as fb:
    data_2 = fb.read()

###################################################
new_path = pcm_path + "/c_1.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

data_3 = ""
with  open(new_path, "r", encoding="ISO-8859-1'") as fb:
    data_3 = fb.read()
###########################################


data_4 = ""
new_path = pcm_path + "/chapter_19.txt"
# with open(new_path, "r") as fb:
#     parrellel_lines.append(fb.readlines())

with open(new_path, "r", encoding="ISO-8859-1") as fb:
    data_4 = fb.read()

###############################################

path_64 = r"C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\pcm_bible\chapters\pcm_64.txt"

data_64 = ""
with open(path_64, "r", encoding="ISO-8859-1") as fb:
    data_64 = fb.read()
    #read read the file as str not list


####################################
total = data_1 + "\n" + data_2 + "\n"  + data_3 + "\n"  +data_4 + "\n"  +data_64
# with open(new_path,"w") as fb:
#     for book in parrellel_lines:
#         for line in book:
#             fb.writelines(line)
new_path = pcm_path + "pcm_entire_bible_2.txt"

with open(new_path, "w", encoding="ISO-8859-1") as fb:
    fb.write(total)



