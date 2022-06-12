bible_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Bible Processing Using Blocks Method\Machine Translation Data (FairSeq)\text_files\en_shuffled.txt"
train = r"C:\Users\lst\Downloads\train (1).en"
dev = r"C:\Users\lst\Downloads\dev.en"
test = r"C:\Users\lst\Downloads\test.en"
ours = []
thiers = []
with open(bible_path, "r") as fb:
    ours = fb.readlines()

with open(train, "r", encoding="utf-8") as fb:
    thiers = fb.readlines()

with open(test, "r",encoding="utf-8") as fb:
    thiers.extend(fb.readlines())

with open(dev, "r", encoding="utf-8") as fb:
    thiers.extend(fb.readlines())


# different_lines = []
# for our_line in ours:
#     for thier_line in thiers:
#         if not thier_line in our_line:
            
#             different_lines.append(thier_line)

list_difference = [element for element in thiers if element not in ours]

print(f"the total thiers is {len(thiers)} different lines is {len(list_difference)}")