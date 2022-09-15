import json
keys = ["because", "no","hi", "house"]
values = [['bikos', 'cauz', 'cause'], ["no", "da","di"], ["hallo", "hi", "halo"], ["home","house","apartment"]]

items = {}
for index, key in enumerate(keys):
    items[key] = values[index]
print(items)

with open("/home/CE/musaeed/ov_testset/dummy.json", "w") as fb:
    json.dump(items,fb)