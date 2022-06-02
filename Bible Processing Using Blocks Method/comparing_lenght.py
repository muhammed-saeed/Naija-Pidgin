pcm_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/pcm_bible/chapters/"
en_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/chapters/"
number_of_chapters = [i for i in range(1, 67)]
pcm_length = ""
en_length = ""
files_with_problems = []
for i in number_of_chapters:
    pcm_file = pcm_path + "pcm_" + str(i) + ".txt"
    en_file = en_path + "en_" + str(i) + ".txt"
    with open(pcm_file, "r") as fb:
        pcm_length = fb.readlines()
    with open(en_file, "r") as fb:
        en_length = fb.readlines()
    if len(en_length) != len(pcm_length):
        print(i)
        files_with_problems.append(i)
    pcm_length = ""
    en_length = ""

pcm_length = ""
en_length = ""
total_pcm_length = 0
for i in number_of_chapters:
    pcm_file = pcm_path + "pcm_" + str(i) + ".txt"
    with open(pcm_file, "r") as fb:
        pcm_length = fb.readlines()
        total_pcm_length += len(pcm_length)

total_en_length = 0
for i in number_of_chapters:
    en_file = en_path + "en_" + str(i) + ".txt"
    with open(en_file, "r") as fb:
        pcm_length = fb.readlines()
        total_en_length += len(pcm_length)

print(f"the total pcm length is {total_pcm_length}")
print(f"the total en_length is {total_en_length}")

total_pcm_length = 0
for i in number_of_chapters:
    if i not in files_with_problems:
        pcm_file = pcm_path + "pcm_" + str(i) + ".txt"
        with open(pcm_file, "r") as fb:
            pcm_length = fb.readlines()
            total_pcm_length += len(pcm_length)

total_en_length = 0
for i in number_of_chapters:
    if i not in files_with_problems:
        en_file = en_path + "en_" + str(i) + ".txt"
        with open(en_file, "r") as fb:
            pcm_length = fb.readlines()
            total_en_length += len(pcm_length)

print(f"the total good parrallel length is {total_pcm_length}")
print(f"the total parrellel en_length is {total_en_length}")


total_pcm_length = 0
for i in files_with_problems:
    pcm_file = pcm_path + "pcm_" + str(i) + ".txt"
    with open(pcm_file, "r") as fb:
        pcm_length = fb.readlines()
        total_pcm_length += len(pcm_length)


total_en_length = 0
for i in files_with_problems:
    en_file = en_path + "en_" + str(i) + ".txt"
    with open(en_file, "r") as fb:
        pcm_length = fb.readlines()
        total_en_length += len(pcm_length)
print(f"the pcm files with problems length is {total_pcm_length}")
print(f"the en files with problems length is {total_en_length}")
