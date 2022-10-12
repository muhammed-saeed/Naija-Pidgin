en_path=r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.en"
pcm_path = r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.pcm"
en_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300.en"
pcm_jw300 = r"C:\Users\lst\Documents\Naija-Pidgin\JW300 data\jw300.pcm"
en_treebank = r"C:\Users\lst\Documents\Naija-Pidgin\Treebank_test\testing_Data\en_parrellel.txt"
pcm_treebank = r"C:\Users\lst\Documents\Naija-Pidgin\Treebank_test\testing_Data\pcm_parrellel.txt"

def to_lower(string_list):
    string_list = [each_string.lower() for each_string in string_list]
    return string_list

def word_reader(pcm_path):
    with open(pcm_path, 'r', encoding='utf-8') as f:
         pcm_wordss = f.read().split()
    return pcm_wordss
pcm_words = []
en_words = []
pcm_words = word_reader(pcm_path)

en_words = word_reader(en_path)

en_words = to_lower(en_words)
pcm_words = to_lower(pcm_words)
pcm_unique_words = set(pcm_words)
en_unique_words = set(en_words)


print(len(pcm_unique_words))  # 👉️ 3
print(len(en_unique_words))  # 👉️ 3

print(len(set(en_unique_words).intersection(pcm_unique_words)))
# print(unique_words)  # {'three', 'one', 'two'}
