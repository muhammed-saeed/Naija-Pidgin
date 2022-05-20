
import fitz  # install using: pip install PyMuPDF
# reads the pdf files
import re
import os
import sys
import json

# file_big[5].get_text()

#########
# English Bible


file_big = fitz.open(
    "/home/muhammed/Desktop/pcm_en_parrellel/engBBE_a4 (1).pdf")
# print(file_big[360].get_text())
# print(file_big.get_toc())

bible_info = file_big.get_toc()
# print("file toc is ", bible_info)
en_chapters_start = []
for item in bible_info:
    # print(item[2])
    en_chapters_start.append(item[2])
    # the third item of hte bible_info is always the starting page

# louai

doc2 = fitz.open("/home/muhammed/Desktop/pcm_en_parrellel/Untitled 1 (1).pdf")
print("the en_chapters starts at the following positions, ", en_chapters_start)


# for page in range(len(en_chapters_start)-1):
new_aa = ""
for i in range(4, 49):

    text = file_big.getPageText(i)

    vtext = text.find("\n")
    text2 = text[vtext+1:]

    vtext2 = text2.find("\n")
    text3 = text2[vtext2+1:]

    vtext3 = text3.find("\n")
    textFinal = text3[vtext3+1:]

    if textFinal[0].isdigit():
        # remove the chapter number, note bible is composed of many books,each is divided into chapters and then verses
        vtext4 = textFinal.find("\n")
        textFinal = textFinal[vtext4+1:]
    # print("##########$$$$$$$$$$$$$$$$$$$$$4")
    # print(textFinal)
    # print("##########$$$$$$$$$$$$$$$$$$$$$4")
    aa = textFinal.split('\n')
    # print("############################")
    for item in aa:
        if len(item) > 3:
            # print(item)
            item += " "
            new_aa = new_aa + item
        else:
            new_aa = new_aa + "#Splitter#"
            online_text = new_aa

FF = new_aa.split("#Splitter#")
# split the page into verses
FF[0] = FF[0][FF[0].find("1"):]
chatper_text = FF
chapter_path = "/home/muhammed/Desktop/pcm_en_parrellel/en_chapter_" + \
    str(1)+"_.txt"
with open(chapter_path, "w") as fb:

    for item in FF:
        fb.write(item)
