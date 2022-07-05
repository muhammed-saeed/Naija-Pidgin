Afri_bert_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\AFRI_BERT Mono-Data\AFRI_BERT_MONO.txt"
bbc_scrapped_data = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\bbc_scrapper\bbc_scrapped_data.txt"
enrich_speech_processing = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\Enrich_speec_rec\enrich_spec_rec.txt"
pidunmt = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\PidUNMT\pidgin_corpus.txt"
sentimenet_anaylsis = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\SA\naijasenti_dataset_v1.0\naijasenti_dataset_v1.0\pidgin\senti_text.txt"
enrich_sentiment_analysis = r"C:\Users\lst\Desktop\Naija-Pidgin\SA\naijasenti_dataset_v1.0\towards_enrich_sentiment_analysis\clean_enrich_senti_text.txt"
data = []
with open(Afri_bert_path, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())

with open(bbc_scrapped_data, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())

with open(enrich_speech_processing, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())

with open(pidunmt, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())

with open(sentimenet_anaylsis, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())

with open(enrich_speech_processing, "r", encoding='utf-8') as fb:
    data.extend(fb.readlines())


large_mono = r"C:\Users\lst\Desktop\Naija-Pidgin\Others Dataset\other mono-pcm\PCM_MONO_TEXT.txt"

with open(large_mono, "w", encoding="utf-8") as fb:
    fb.writelines(data)

print(f" the number of mono-lines those not include bible and jw300 is {len(data)}")