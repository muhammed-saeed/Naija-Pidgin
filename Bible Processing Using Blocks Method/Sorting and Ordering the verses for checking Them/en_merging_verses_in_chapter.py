from asyncio import start_server
import os
import string

files = os.listdir(
    '/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/en')
# print(files)
# for file in files:
#   # do something
chapters = [i for i in range(1, 67)]
print(chapters)
verses_in_chapter = []
starter = ""
dump = []
for chapter in chapters:
    starter = str(chapter) + "_"
    for file in files:
        if file.startswith(starter):
            # print(file)
            dump.append(file)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$444")
    starter = ""
    verses_in_chapter.append(dump)
    dump = []
# print(dump)
# print(len(verses_in_chapter))
# print(verses_in_chapter)
counter = 0
for i in verses_in_chapter:
    for j in i:
        counter += 1

# print(counter)
# print(len(files))
# print(verses_in_chapter[0])
to_be_ordered_list = []
order_dump = []
for chapter in verses_in_chapter:
    for verse in chapter:
        name = verse.replace("_", "")
        name = name.replace(".txt", "")
        order_dump.append(int(name))
    to_be_ordered_list.append(order_dump)
    order_dump = []
print(len(to_be_ordered_list))


ordered_list = []
for chapter in to_be_ordered_list:
    ordered_list.append(sorted(chapter))

ordered_list_2 = []
inter = []

to_be_ordered_list_2 = []
order_dump = []


name = ""
counter = 1
for chapter in ordered_list:
    for verse in chapter:
        name = str(counter)
        string_verse = str(verse)
        name = name + "_" + string_verse[len(name):] + ".txt"
        order_dump.append(name)
    to_be_ordered_list_2.append(order_dump)
    order_dump = []
    counter += 1
print(len(to_be_ordered_list_2))
print(to_be_ordered_list_2[60])
print(ordered_list[60])
print(to_be_ordered_list_2)
counter = 1
for chapter in to_be_ordered_list_2:
    general_path = '/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/en'
    for i in chapter:
        verse_path = general_path + "/"+str(i)
        chapter_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/chapters/"
        chapter_path_counter = chapter_path + "en_" + str(counter) + ".txt"
        timer = chapter_path + str(counter)
        verse = ""
        with open(verse_path, "r") as fb:
            verse = fb.readlines()
        with open(chapter_path_counter, "a") as fb:
            fb.writelines(verse)
        verse = ""
    counter += 1


# print(files)
# for file in files:
#   # do something
