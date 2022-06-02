pcm = "/home/muhammed/Downloads/pcm_val.txt"
en = "/home/muhammed/Downloads/en_val.txt"

pcm_file = ""
en_file = ""
with open(pcm, "r") as fb:
    pcm = fb.readlines()
with open(en, 'r') as fb:
    en = fb.readlines()

with open("/home/muhammed/Desktop/val/val.lc.norm.tok.en", "w") as fb:
    fb.writelines(en[:int(len(en)/2)])
with open("/home/muhammed/Desktop/test/test.lc.norm.tok.en", "w") as fb:
    fb.writelines(en[int(len(en)/2):])


with open("/home/muhammed/Desktop/val/val.lc.norm.tok.pcm", "w") as fb:
    fb.writelines(pcm[:int(len(pcm)/2)])
with open("/home/muhammed/Desktop/test/test.lc.norm.tok.pcm", "w") as fb:
    fb.writelines(pcm[int(len(pcm)/2):])
