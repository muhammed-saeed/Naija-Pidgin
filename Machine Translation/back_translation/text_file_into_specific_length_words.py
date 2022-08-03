
max_length = int(input("Max length of your line = "))
origin_file = "/home/CE/musaeed/back_translation_mono_text_pcm.txt"
file = open(origin_file,"r") #open the file to edit and read the data
content = file.read()
content_split = content.split()
file.close()
output_file = "/home/CE/musaeed/ironside/Machine_Translation/back_translation/text_with_specific_max_length.txt"
file_out = open(output_file,"w+") #create the output file

# for i in range(len(content_split)):
for i,j in enumerate(content_split):
    a = j + " "
    file_out.write(a)
    # print(f"###################33{j}")
    if (i + 1) % max_length == 0: #add line break each time pgcd equal 0
         file_out.write('\n')
    a = ""
file_out.close()