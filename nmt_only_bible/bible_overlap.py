en_path=r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.en"
pcm_path = r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.pcm"
en_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300\jw300.en"
pcm_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300\jw300.pcm"
en_treebank = r"C:\Users\lst\Documents\Naija-Pidgin\Treebank_test\testing_Data\en_parrellel.txt"
pcm_treebank = r"C:\Users\lst\Documents\Naija-Pidgin\Treebank_test\testing_Data\pcm_parrellel.txt"

def intersection_words(en_unique_words, pcm_unique_words):
    return set(en_unique_words).intersection(pcm_unique_words)

def to_lower(string_list):
    string_list = [each_string.lower() for each_string in string_list]
    return string_list

def word_reader(pcm_path):
    with open(pcm_path, 'r', encoding='utf-8') as f:
         pcm_wordss = f.read().split()
    return pcm_wordss
bible_pcm_words = []
bible_en_words = []

bible_pcm_words = word_reader(pcm_path)
bible_en_words = word_reader(en_path)

bible_en_words = to_lower(bible_en_words)
bible_pcm_words = to_lower(bible_pcm_words)
bible_pcm_unique_words = set(bible_pcm_words)
bible_en_unique_words = set(bible_en_words)

##############
jw300_pcm_words = word_reader(pcm_jw300)
jw300_en_words = word_reader(en_jw300)

jw300_en_words = to_lower(jw300_en_words)
jw300_pcm_words = to_lower(jw300_pcm_words)
jw300_pcm_unique_words = set(jw300_pcm_words)
jw300_en_unique_words = set(jw300_en_words)

#################
treebank_pcm_words = word_reader(pcm_treebank)
treebank_en_words = word_reader(en_treebank)

treebank_en_words = to_lower(treebank_en_words)
treebank_pcm_words = to_lower(treebank_pcm_words)
tree_pcm_unique_words = set(treebank_pcm_words)
tree_en_unique_words = set(treebank_en_words)



print(f"Bible English and PCM intersetion {(len(set(bible_en_unique_words).intersection(bible_pcm_unique_words)))/len(bible_en_unique_words)}")
print(f"JW300 English to PCM intersetciotn {(len(set(jw300_en_unique_words).intersection(jw300_pcm_unique_words)))/len(jw300_en_unique_words)}")
print(f"TreeBank English to PCM intersection {(len(set(tree_en_unique_words).intersection(tree_pcm_unique_words))/len(tree_en_unique_words))}")
print("#####################################")
print(f"Bible English and JW00 PCM intersetion {(len(set(bible_en_unique_words).intersection(jw300_pcm_unique_words)))/len(bible_en_unique_words)}")
print(f"Bible English to Tree PCM intersetciotn {(len(set(bible_en_unique_words).intersection(tree_pcm_unique_words)))/len(bible_en_unique_words)}")
print("#########################################")
print(f"JW00 English and bible PCM intersetion {(len(set(bible_en_unique_words).intersection(bible_pcm_unique_words)))/len(jw300_en_unique_words)}")
print(f"JW300 English to tree PCM intersetciotn {(len(set(jw300_en_unique_words).intersection(tree_pcm_unique_words)))/len(jw300_en_unique_words)}")
print("############################33")
print(f"Tree English and Bible PCM intersetion {len(set(tree_en_unique_words).intersection(bible_pcm_unique_words))/len(tree_en_unique_words)}")
print(f"TreeBank English to JW300 PCM intersection {len(set(tree_en_unique_words).intersection(jw300_pcm_unique_words))/len(tree_en_unique_words)}")


# print(unique_words)  # {'three', 'one', 'two'}
