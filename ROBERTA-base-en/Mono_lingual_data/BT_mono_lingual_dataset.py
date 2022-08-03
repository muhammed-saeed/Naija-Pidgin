import random
single_mono = []
afri_bert = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\PCM_MONO_TEXT.txt"
tree_bank = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\pcm_parrellel.txt"
senti_data = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\senti_text.txt"
enrich_speech_reco = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\enrich_spec_rec.txt"
aa= ""
bb = ""
cc = ""
dd= ""
pcm_data_ = ""
output_file = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\mono_for_BT_no_jw300_no_bible.txt"
with open(afri_bert,"r", encoding="utf-8") as fb:
  aa = fb.read()

with open(tree_bank,"r", encoding="utf-8") as fb:
  bb = fb.read()

with open(senti_data,"r", encoding="utf-8") as fb:
  cc = fb.read()

with open(enrich_speech_reco,"r", encoding="utf-8") as fb:
  pcm_data_ = fb.read()





with open(output_file, "w", encoding="utf-8") as fb:
  fb.write(pcm_data_)
  fb.write("\n")
  fb.write(bb)
  # fb.write("\n")
  # fb.write(sentiment_analysis)
  fb.write("\n")
  fb.write(cc)
  fb.write("\n")
  fb.write(aa)
  fb.write("\n")
  fb.write(dd)
  fb.write("\n")

text_ = ""
with open(output_file, "r", encoding="utf-8") as fb:
  text_ = fb.read()


import re
clean_text = re.sub(r'[^\x00-\x7f]',r' ',text_)  

with open(output_file, "w", encoding="utf-8") as fb:
  fb.write(clean_text)


lines = open(output_file).readlines()
random.shuffle(lines)
open(output_file, 'w').writelines(lines)

with open(output_file, "r", encoding="utf-8") as fb:
  single_mono = fb.readlines()


# total_length = len(single_mono)
# test_data = int(0.15*total_length)
# val_data = 2*test_data
# print(f"the total data lenght is {total_length} the test is {test_data} and val is {val_data}")
# with open(test_file,"w") as fb:
#   fb.writelines(single_mono[-test_data:])
# with open(val_file, "w") as fb:
#   fb.writelines(single_mono[-val_data:-test_data])

# with open(train_file, "w") as fb:
#   fb.writelines(single_mono[:-val_data])