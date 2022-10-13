afri_pcm_mono = r"C:\Users\lst\Documents\Naija-Pidgin\Others Dataset\other mono-pcm\AFRI_BERT Mono-Data\AFRI_BERT_MONO.txt"
bbc_pcm_mono = r"C:\Users\lst\Documents\Naija-Pidgin\Others Dataset\other mono-pcm\bbc_scrapper\bbc_scrapped_data.txt"
enrich_speech_to_text_path = r"C:\Users\lst\Documents\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\enrich_spec_rec.txt"
unmt = r"C:\Users\lst\Documents\Naija-Pidgin\Others Dataset\other mono-pcm\PidUNMT\pidgin_corpus.txt"
def intersection_words(en_unique_words, pcm_unique_words):
    return set(en_unique_words).intersection(pcm_unique_words)

def to_lower(string_list):
    string_list = [each_string.lower() for each_string in string_list]
    return string_list

def word_reader(pcm_path):
    with open(pcm_path, 'r', encoding='utf-8') as f:
         pcm_wordss = f.read().split()
    return pcm_wordss

afri_bert_data = word_reader(afri_pcm_mono)
afri_bert_data = to_lower(afri_bert_data)


bbc_mono = word_reader(bbc_pcm_mono)
bbc_mono = to_lower(bbc_mono)

enrich_speech_to_text = word_reader(enrich_speech_to_text_path)
enrich_speech_to_text = to_lower(enrich_speech_to_text)

unmt_data = word_reader(unmt)
unmt_data = to_lower(unmt_data)

# print(f"the afri-bert data is {len(afri_bert_data)}")
afri_bert_data_unique = set(afri_bert_data)
print(f"the unique afri-bert data is {len(afri_bert_data_unique)}")

# print(f"the bbc-mono data is {len(bbc_mono)}")
bbc_mono_unique = set(bbc_mono)
print(f"the unique bbc-mono data is {len(bbc_mono_unique)}")

# print(f"the enrich_speech_totext data is {len(enrich_speech_to_text)}")
enrich_speech_to_text_unique = set(enrich_speech_to_text)
print(f"the unique enrich_speech_totext data is {len(enrich_speech_to_text_unique)}")

# print(f"the unmt data is {len(unmt_data)}")
unmt_data_unique = set(unmt_data)
print(f"the unique unmt data is {len(unmt_data_unique)}")