data_path = "/home/CE/musaeed/t5_translation/data"
with open(f'{data_path}/train.en', "r") as fb, open(f'{data_path}/train.en', "w") as fp:
    data = fb.read()
    data = data.lower()
    fp.write(data)