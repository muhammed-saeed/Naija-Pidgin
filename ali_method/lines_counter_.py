import os
path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/pcm_bible/pcm/"
# path = "/home/muhammed/Desktop/pcm_en_parrellel/BLOCKS_SPANS/en_bible/en/"

# Change the directory
os.chdir(path)

# Read text File


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return len(f.readlines())


# iterate through all file
global counter
counter = 0
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}{file}"
        # print(file_path)
        # print(file)

        # call read text file function
        counter += read_text_file(file_path)

print(counter)

# os.chdir(en_path)

# counter = 0
# for file in os.listdir():
#     # Check whether file is in text format or not
#     if file.endswith(".txt"):
#         file_path = f"{path}{file}"
#         # print(file_path)
#         # print(file)

#         # call read text file function
#         counter += read_text_file(file_path)
