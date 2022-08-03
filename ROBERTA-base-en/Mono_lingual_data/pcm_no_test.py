test = r"C:\Users\lst\Desktop\Naija-Pidgin\JW300 data\test\test.pcm"
mono = r"C:\Users\lst\Desktop\Naija-Pidgin\ROBERTA-base-en\Mono_lingual_data\pcm_entire_mono.txt"

mono_ = []
test_ = []
mono_data = open(mono, "r", encoding="utf-8")
test_data = open(test, "r", encoding="utf-8")

mono_ = mono_data.readlines()
test_ = test_data.readlines()
pure_mono = []
for a in mono_:
    if a not in test_:
        pure_mono.append(a)

print(f"{len(mono_)} and the length of {len(pure_mono)} and difference is {len(mono_) - len(pure_mono)} and lenght is {len(test_)}")
mono_back_translation_text_file = r"C:\Users\lst\Desktop\Naija-Pidgin\BT Data\back_translation_mono_text_pcm.txt"
with open(mono_back_translation_text_file, "w", encoding="utf-8") as fb:
    fb.writelines(pure_mono)