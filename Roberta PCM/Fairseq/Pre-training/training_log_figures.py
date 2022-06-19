log_lines = []
log_file_path = r"C:\Users\lst\Desktop\Naija-Pidgin\Roberta PCM\Fairseq\Pre-training\hydra_train.log"
with open(log_file_path, "r") as fb:
    log_lines = fb.readlines()


print(log_lines[1000])
train_data = []
valid_data = []
for line in log_lines:
    if "[train][INFO] " in line:
        middle = line.split("-")
        train_data.append(middle[3])
        
    if "[valid][INFO]" in line:
        middle = line.split("-")
        valid_data.append(middle[3])


print(train_data[10])
print(valid_data[10])
train_figures = []
train_ppl = []
float_train_ppl = []
for line in train_data:
    train_figures.append(line.split(","))
for line in train_figures:
    train_ppl.append(line[2])

for lin in train_ppl:
        
   
    aa=train_ppl[10][14:][1:]
    aa = aa[:-1]
    float_train_ppl.append(aa)

# print(train_figures[10])
# print(train_ppl[10][14:])
# aa=train_ppl[10][14:][1:]
# aa = aa[:-1]
# print(float(aa))
# print(float_train_ppl[10])
total_epoch = []
for i in range(len(float_train_ppl)):
    total_epoch.append(i+1)

import matplotlib.pyplot as plt
plt.plot(total_epoch, float_train_ppl)
plt.show()