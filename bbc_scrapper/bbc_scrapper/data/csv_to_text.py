from cgitb import text
import csv

csv_file = "./bbc_pidgin_corpus.csv"
text_file = "./text_data"

with open(text_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
lines = ""
with open(text_file, "r") as fb:
    lines = fb.readlines()

lines = lines.strip()
with open("text_zero_blank", "w") as fb:
    fb.writelines(lines)