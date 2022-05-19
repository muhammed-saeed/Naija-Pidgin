import re
file = None
with open("/home/muhammed/Desktop/pcm_en_parrellel/pcm_chapters/pcm_chapter_1_.txt") as fb:
    # with open("/home/muhammed/Desktop/pcm_en_parrellel/en_chapters/en_chapter_1_.txt") as fb:

    file = fb.readlines()

file_list = file[0].split()
sub_str = ""

for i, m in enumerate(file_list):
    if m.isdigit():
        sub_str += "_verse_break_ "
    else:
        sub_str += m + " "

file[0] = file[0].strip()

pcm_splitted_verse = re.sub(
    r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])", "_VERSE_BREAK_", file[0])
print("the number of pcm sentences is ", len(pcm_splitted_verse))
# print(pcm_splitted_vers


file = ""
with open("/home/muhammed/Desktop/pcm_en_parrellel/en_chapters/en_chapter_1_.txt") as fb:

    file = fb.readlines()

file_list = file[0].split()
sub_str = ""
file[0] = file[0].strip()

en_splitted_verse = re.sub(
    r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])", "_VERSE_BREAK_", file[0])
print("the number of en sentences is  ", len(en_splitted_verse))

print(en_splitted_verse[-1])
print(pcm_splitted_verse[-1])

print("##################################333")
print(en_splitted_verse[2])

print(pcm_splitted_verse[2])

print("#############33")
# print(en_splitted_verse)
