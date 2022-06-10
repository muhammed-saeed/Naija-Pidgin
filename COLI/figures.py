import enum
from hashlib import new
import os 
training = []
validation = []

file = []
with open(r"C:\Users\lst\Desktop\COLI\models\7.69_blue_score\training_log.txt", "r") as fb:
    file = fb.readlines()

for line in file:
    if "| INFO | train | epoch" in line:
        training.append(line)
    if "| INFO | valid | epoch" in line:
        validation.append(line)
# print(len(training))
# print(len(validation))
# print(training[0])
# print(validation[0])

for num, epoch in enumerate(training):
    epoch_ = epoch.split("|")
    training[num] = epoch_

for num, epoch in enumerate(validation):
    epoch_ = epoch.split("|")
    validation[num] = epoch_


st = training[0][3]
print(st)
print(st.strip())
new_st = st.strip()
print(new_st.split(" "))
a = []

for num,item in enumerate(training):
    b = []
    # print(item)
    for element in item[3:]:
        # print(item[3:])
        # print(element)
        element = element.strip()
        element_ = element.split(" ")
        element_[1] = float(element_[1])
        b.append(element_)
    a.append(b)
    item = a


new_aa = []
for i in range(len(a)):
    flat_list = [x for xs in  a[i] for x in xs]
    new_aa.append(flat_list)


import pandas as pd
df = pd.DataFrame(new_aa)
# print(df.head())
print(df.columns.values)
new_columns = [item[0] for item in a[0]]
print(new_columns)
new_df = pd.DataFrame(columns=new_columns)
odd_number = list(filter(lambda x: (x % 2 != 0), df.columns.values))
new_df_2 = df.filter(odd_number,axis=1)
print(new_df_2.head())
new_df_2.columns = new_columns
print(new_df_2.head())
new_df_2.to_csv(r"C:\Users\lst\Desktop\training_epochs.csv")


a = []
print(validation[0])
for num,item in enumerate(validation):
    b = []
    # print(item)
    for element in item[5:]:
        # print(item[3:])
        # print(element)
        element = element.strip()
        element_ = element.split(" ")
        element_[1] = float(element_[1])
        b.append(element_)
    a.append(b)
    item = a


new_aa = []
for i in range(len(a)):
    flat_list = [x for xs in  a[i] for x in xs]
    new_aa.append(flat_list)


import pandas as pd
df = pd.DataFrame(new_aa)
# print(df.head())
print(df.columns.values)
new_columns = [item[0] for item in a[0]]
print(new_columns)
new_df = pd.DataFrame(columns=new_columns)
odd_number = list(filter(lambda x: (x % 2 != 0), df.columns.values))
new_df_2 = df.filter(odd_number,axis=1)
print(new_df_2.head())
new_df_2 = new_df_2.drop(15, axis=1)
print(new_df_2.head())

new_df_2.columns = new_columns
print(new_df_2.head())
cp = pd.read_csv(r"C:\Users\lst\Desktop\training_epochs.csv")
new_df_2['epoch'] = cp['epoch']
print(new_df_2.head())
new_df_2.to_csv(r"C:\Users\lst\Desktop\validation_epoch.csv")

train_x = cp.epoch.values
train_y_ppl = cp.ppl.values