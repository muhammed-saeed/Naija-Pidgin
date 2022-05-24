from asyncio import start_server
import os

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
# counter = 0
# for i in to_be_ordered_list:
#     for j in i:
#         counter += 1
# print(counter)


# print(to_be_ordered_list)


ordered_list = []
for chapter in to_be_ordered_list:
    ordered_list.append(sorted(chapter))

print(ordered_list)
print(len(ordered_list))
