en_path=r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.en"
pcm_path = r"C:\Users\lst\Documents\Naija-Pidgin\nmt_only_bible\train\train.pcm"

def to_lower(string_list):
    string_list = [each_string.lower() for each_string in string_list]
    return string_list

pcm_words = []
en_words = []
with open(pcm_path, 'r', encoding='utf-8') as f:
    pcm_words = f.read().split()

with open(en_path, 'r', encoding='utf-8') as f:
    en_words = f.read().split()

# print(words)  # 👉️ ['one', 'one', 'two', 'two', 'three', 'three']
en_words = to_lower(en_words)
pcm_words = to_lower(pcm_words)
pcm_unique_words = set(pcm_words)
en_unique_words = set(en_words)
print(len(pcm_unique_words))  # 👉️ 3
print(len(en_unique_words))  # 👉️ 3

print(len(set(en_unique_words).intersection(pcm_unique_words)))
# print(unique_words)  # {'three', 'one', 'two'}
