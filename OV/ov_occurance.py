file = open("/home/CE/musaeed/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt", "r")

bible_pd_ov = {"kon":"con","pipol":"people", "bi":"by", "en":"im", "yu":"you","bikos":["cos", "because"], "kom":"come",
"mi":"me", "wi":"we", "yu":"you", "yor":"your", "si":"see","rish":"reach", "doz":["those", "dose"], "awa":"our","won":"wan","karry":"carry","komot":["comot", "come out"],"evritin":["everytin","everything","everyting"], "destroy":"distroy", "people,":"people", "koll":"call"}
#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
bible_pd_ov_dict = list(bible_pd_ov.keys())
occurrences_ = {}
occurrences = []
for i in bible_pd_ov_dict:
    occurrences.append(data.count(i))

print(bible_pd_ov_dict)

mono_ov = {}
for i,j in enumerate(occurrences):
    mono_ov[bible_pd_ov_dict[i]] = j
    print(f"{bible_pd_ov_dict[i]} occurred {j} times")
print(f"the length of the occurance data is {len(bible_pd_ov_dict)}")
print(mono_ov)



