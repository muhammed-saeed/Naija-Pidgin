pcm = "/home/muhammed/Downloads/pcm_val.txt"
en = "/home/muhammed/Downloads/pcm_val.txt"

pcm_file = ""
en_file = ""
with open(pcm, "r") as fb:
    pcm = fb.readlines()
with open(en, 'r') as fb:
    en = fb.readlines()

with open("/home/muhammed/Desktop/en_valid.txt", "w") as fb:
    fb.writelines(en[:int(len(en)/2)])
with open("/home/muhammed/Desktop/en_test.txt", "w") as fb:
    fb.writelines(en[int(len(en)/2):])


with open("/home/muhammed/Desktop/pcm_valid.txt", "w") as fb:
    fb.writelines(pcm[:int(len(pcm)/2)])
with open("/home/muhammed/Desktop/pcm_test.txt", "w") as fb:
    fb.writelines(pcm[int(len(pcm)/2):])
