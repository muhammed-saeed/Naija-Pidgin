back_Translation_file = "/home/CE/musaeed/back_translation_pcm_bpe.txt"
pcm_src_translation_file = "/home/CE/musaeed/back_translation_pcm_bpe_source.txt"
en_tgt_translation_file = "/home/CE/musaeed/back_translation_pcm_bpe_target.txt"
source_data = []
target_data = []
src_tgt_data = []
with open(back_Translation_file, "r", encoding="utf-8") as fb :
    src_tgt_data = fb.readlines()
count = 0
for i in src_tgt_data:
    if "S-" in i:
        count += 1
        a = i.split()
        string_ = " ".join(a[1:])+" \n"
        source_data.append(string_)

empty_src_index = []
for j, i in enumerate(source_data):
    if i.strip() == "":
        empty_src_index.append(j)

for i in src_tgt_data :
    if "H-" in i:
        a = i.split()
        target_data.append(" ".join(a[2:]) + " \n")

empty_src_index.reverse()

print(empty_src_index)

print(len(source_data))
print(len(target_data))
for j in empty_src_index:
    print(len(source_data), j)
    source_data.pop(j)
    target_data.pop(j)
# a = []
# b= []
# for j,i in enumerate(source_data):
#     if j not in empty_src_index:
#         a.append(i)
# for j,i in enumerate(target_data):
#     if j not in empty_src_index:
#         b.append(i)
# print(len(a))
# print(len(b))
# print(len(empty_src_index))
with open(pcm_src_translation_file, "w", encoding="utf-8") as fb:
    fb.writelines(source_data)

with open(en_tgt_translation_file, "w", encoding="utf-8") as fb:
    fb.writelines(target_data)