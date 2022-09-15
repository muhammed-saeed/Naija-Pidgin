import json
import random
ov_file = '/home/CE/musaeed/ov_testset/dummy.json'
ov_out_of_td_file = "/home/CE/musaeed/ov_testset"
test_file = "/home/CE/musaeed/ironside_2/ironside/Machine_Translation/JW300_with_bible_joined_embeddings/test/test.pcm"

english_test_data = "/home/CE/musaeed/ironside_2/ironside/Machine_Translation/JW300_with_bible_joined_embeddings/test/test.en"
english_ov_output_file = ""
pcm_ov_outupt_file = ""

number_of_ov_examples_each = 10
total_number_of_text_samples = 1000

file = open(ov_file)
data = json.load(file)

ov_values = []
ov_lenght = 0
for key in data.keys():
    ov_lenght += len(data[key])
    ov_values.extend(data[key])

print(ov_lenght)
print(ov_values)
# print(data)
ov_out_of_test_data = []
ov_in_test_data_index = {}
test_data = []


with open(test_file, "r") as fb:
    test_data = fb.readlines()

generated_test_data = []
for ov_index, ov_word in enumerate(ov_values):
    key = ov_word
    temp = []
    occured = False
    for index, line in enumerate(test_data):
        if ov_word in line:
            temp.append(index)
            ov_in_test_data_index[key] = temp 
            generated_test_data.append(line)
            occured = True
            # break
    if not occured:
        ov_out_of_test_data.append(ov_word)

# print(len(generated_test_data))
# print(ov_in_test_data_index)
# print(len(ov_in_test_data_index))
# print(ov_out_of_test_data)



ov_index_to_output = []
final_test_data = []
total_ov_indexes = []
for ov_in_test in ov_in_test_data_index.keys():
    total_ov_indexes.extend(ov_in_test_data_index[ov_in_test])

print(f"total ov extended are {len(total_ov_indexes)}")


for ov_in_test in ov_in_test_data_index.keys():
    if len(ov_in_test_data_index[ov_in_test]) > number_of_ov_examples_each :
        ov_index_to_output.extend(random.sample(ov_in_test_data_index[ov_in_test], number_of_ov_examples_each))
    else :
        ov_index_to_output.extend(ov_in_test_data_index[ov_in_test])

print(len(ov_index_to_output))

not_ov_data_in_test_set = [x for x in range(0,len(test_data)) if x not in ov_index_to_output]
print(len(not_ov_data_in_test_set))

final_test_data.extend(ov_index_to_output)
remaining_to_generate = total_number_of_text_samples - len(ov_index_to_output)
final_test_data.extend(random.sample(not_ov_data_in_test_set, remaining_to_generate))

print(f"the length of the generated {len(final_test_data)}")


english_lines = open(english_test_data, "r").readlines()
pcm_lines = open(test_file, "r").readlines()

english_out = [ ]
pcm_out =[]

for index in final_test_data:
    english_out.append(english_lines[index])
    pcm_out.append(pcm_lines[index])

with open("/home/CE/musaeed/ov_testset/en.txt", "w") as fb:
    fb.writelines(english_out)

with open("/home/CE/musaeed/ov_testset/pcm.txt", "w") as fb:
    fb.writelines(pcm_out)
















