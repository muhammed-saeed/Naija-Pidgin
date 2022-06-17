import random
single_mono = []
output_files = "/home/CE/musaeed/pcm_roberta/pcm_text.txt"
speeh_data = "/home/CE/musaeed/pcm_roberta/enrich_spec_rec.txt"
sentiment_analysis = "/home/CE/musaeed/pcm_roberta/clean_enrich_senti_text.txt"
tree_bank = "/home/CE/musaeed/pcm_roberta/pcm_parrellel.txt"
senti_file = "/home/CE/musaeed/pcm_roberta/senti_text.txt"


train_file = "/home/CE/musaeed/pcm_roberta/data/pcm.train.raw"
val_file = "/home/CE/musaeed/pcm_roberta/data/pcm.val.raw"
test_file = "/home/CE/musaeed/pcm_roberta/data/pcm.test.raw"

aa= ""
bb = ""
cc = ""
dd= ""
pcm_data_ = ""
with open(tree_bank,"r") as fb:
  aa = fb.read()

with open(sentiment_analysis,"r") as fb:
  bb = fb.read()

with open(speeh_data,"r") as fb:
  cc = fb.read()
with open(output_files,"r") as fb:
  pcm_data_ = fb.read()

with open(senti_file, "r") as fb:
  dd = fb.read()
with open(output_files, "w") as fb:
  fb.write(pcm_data_)
  fb.write("\n")
  fb.write(bb)
  fb.write("\n")
  fb.write(sentiment_analysis)
  fb.write("\n")
  fb.write(cc)
  fb.write("\n")
  fb.write(aa)
  fb.write("\n")
  fb.write(dd)
  fb.write("\n")

text_ = ""
with open(output_files, "r") as fb:
  text_ = fb.read()


import re
clean_text = re.sub(r'[^\x00-\x7f]',r' ',text_)  

with open(output_files, "w") as fb:
  fb.write(clean_text)


lines = open(output_files).readlines()
random.shuffle(lines)
open(output_files, 'w').writelines(lines)

with open(output_files, "r") as fb:
  single_mono = fb.readlines()


total_length = len(single_mono)
test_data = int(0.15*total_length)
val_data = 2*test_data
print(f"the total data lenght is {total_length} the test is {test_data} and val is {val_data}")
with open(test_file,"w") as fb:
  fb.writelines(single_mono[-test_data:])
with open(val_file, "w") as fb:
  fb.writelines(single_mono[-val_data:-test_data])

with open(train_file, "w") as fb:
  fb.writelines(single_mono[:-val_data])