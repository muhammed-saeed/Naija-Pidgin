pcm_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/pcm_bible/chapters/"
en_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/chapters/"

pcm_output_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/pcm_bible/pcm_parrellel.txt"
en_output_path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/en_parrellel.txt"
books = [i for i in range(1, 67)]
en_bible = ""
pcm_bible = ""
files_with_problems = [4, 19, 64, 66]
for book in books:
    if book not in files_with_problems:
        path = pcm_path + "pcm_"+str(book) + ".txt"
        with open(path, "r") as fb:
            pcm_bible = fb.readlines()
        with open(pcm_output_path, "a") as fb:
            fb.writelines(pcm_bible)
        pcm_bible = ""

for book in books:
    if book not in files_with_problems:
        path = en_path + "en_"+str(book) + ".txt"
        with open(path, "r") as fb:
            en_bible = fb.readlines()
        with open(en_output_path, "a") as fb:
            fb.writelines(en_bible)
        en_bible = ""
