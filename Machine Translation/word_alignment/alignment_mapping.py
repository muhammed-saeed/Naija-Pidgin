final_algin_path = r"C:\Users\lst\Downloads\tofrancs copy\final.align"
tgt_addbegin_path = r"C:\Users\lst\Downloads\tofrancs copy\enfr.lc.tgt.bpe.addbegin"
src_addbegin_path = r"C:\Users\lst\Downloads\tofrancs copy\enfr.lc.src.bpe.addbegin"
mapped_data_path = r"C:\Users\lst\Downloads\tofrancs copy\enfr_mapped.txt"

final_algin_data = []
tgt_addbegin_data = []
src_addbegin_data = []


final_mapped = []



with open(final_algin_path, "r", encoding="utf-8") as fb:
    final_algin_data = fb.readlines()

with open(tgt_addbegin_path, "r", encoding='utf-8') as fb:
    tgt_addbegin_data = fb.readlines()

with open(src_addbegin_path, "r", encoding="utf-8") as fb:
    src_addbegin_data = fb.readlines()

for counter in range(len(final_algin_data)):
    final_align_line = str(final_algin_data[counter].strip()).split(" ")
    # print(final_algin_data)
    tgt_addbegin_line = str(tgt_addbegin_data[counter].strip()).split(" ")
    src_addbegin_line = str(src_addbegin_data[counter].strip()).split(" ")
    final_mapped_line = []
    for map in final_align_line:
        elements = map.split("-")
        src_word = src_addbegin_line[int(elements[0])]
        tgt_word = tgt_addbegin_line[int(elements[1])]
        mapped = src_word + "-" + tgt_word
        # print("############################33")
        # print(mapped)
        final_mapped_line.append(mapped)
    final_mapped_line.append("\n")
    final_mapped.append(" ".join(final_mapped_line))


with open(mapped_data_path, "w", encoding="utf-8") as fb:
    fb.writelines(final_mapped)



# print(final_algin_data[:10])

# print(final_mapped[:10])

# final_align_str = str(final_algin_data[8].strip()).split(" ")
# tgt_str = str(tgt_addbegin_data[8].strip()).split(" ")
# src_str = str(src_addbegin_data[8].strip()).split(" ")
# for map in final_align_str:
#     elements = map.split("-")
#     src_word = src_str[int(elements[0])]
#     tgt_word = tgt_str[int(elements[1])]
#     mapped = src_word + "-" + tgt_word
#     final_mapped.append(mapped)
# print(final_mapped)



    