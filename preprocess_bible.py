import fitz  # install using: pip install PyMuPDF
# reads the pdf files
import re
import os

title_pattern = r' \d+:\d+\n'
# the title of the paper
header_pattern = r'[a-zA-Z]+ \d+-*\d*:\d+-*\d*\n\d+\n.+ \d+-*\d*:\d+-*\d*\n'
# * means 0 or more (maybe zero dash or more)
# + for sure there is decimal
# any type of character
verse_pattern = r'\n*\d+\n'
# the verse_ is number 4 and the aya is 2:30
remove_num_pattern = r' *\d+ *'
# removing the number_pattern
quote_start_pattern = "“"
# exchange the double qoute into asciis one
quote_end_pattern = "”"
s_quote_start_pattern = "‘"
s_quote_end_pattern = "’"
sep = " "
# the dot within the same versa is transferred int space

counter = 0
# can be removed not used
paths = ["./naijia part", "./Engllish Bible"]

for path in paths:
    files = os.listdir(path)
    files = list(filter(lambda x: x.endswith(".pdf"), files))
    # print(*files)
    for file in files:
        with fitz.open(path+'/'+file) as doc:
            # total_text = ""
            verse_counter = 1
            text = ""
            text_array = []  # the verse after being splitted
            # the title of the phrase  is anything before Decimal:Decimal
            title = re.split(title_pattern, doc[0].get_text())[0]
            folder_path = path+"/"+title
            try:
                os.mkdir(path+"/"+title)
            except:
                print("folder {} is already there".format(title))
            splits = []
            # the number of the phrases
            for page in doc:
                # total_text += page.get_text()
                l = re.split(header_pattern, page.get_text())
                # store the header in variable l and then remove the header from the string
                if len(l) == 2:
                    l[1] = l[1].replace(quote_start_pattern, "\"")
                    l[1] = l[1].replace(quote_end_pattern, "\"")
                    l[1] = l[1].replace(s_quote_start_pattern, "'")
                    l[1] = l[1].replace(s_quote_end_pattern, "'")
                    # l[1] is the text in the page after the header

                    # pre-process the verse (single_code_end_, single_code_start, double_qoute_start, double_code_end)
                    matches = re.findall(verse_pattern, l[1])
                    # verse patter is just number and is always followed by newline
                    # matches is a text, contains the the verse_number followed by \n and the text
                    for i in matches:
                        # the verse start from 2, as the first verse is not in numbered in the list in the first
                        # remove the spaces and the newline in both beginning and ending #verses are in oreder # verses followed by newline
                        if int(i.strip()) == verse_counter + 1:
                            # if this number followed by new
                            splits.append(i)
                            verse_counter += 1

                    text += l[1]
                    # text is all the data in the pdf without the header, text is appending of the pages l[1]
                    #
                    # verses = re.split(verse_pattern, l[1])
                    # print(len(verses)-1)
                    # text_array[-1] += verses[0]
                    # for i in verses[1:]:
                    # text_array.append(i)
                else:
                    print("Something is wrong")

            remaining_text = text
            # this is one used to divided the text into verse
            # print(splits)
            for splt in splits:
                # splits are strings \n decimal \n
                verses = remaining_text.split(splt)
                text_array.append(verses[0])
                # text_array contains the verse text

                # print(splt.strip())
                if len(verses) > 1:
                    remaining_text = verses[1]
            text_array.append(remaining_text)

            # text_array contain the text for the entire verses
            # the online_text contains the data in single verse

            # with open(folder_path+"/all.txt", "w") as f:
            # print(len(doc)) # debugging
            # print(len(total_text) - len(text))
            # print((len(total_text) - len(text))/len(doc))
            # print((len(total_text) - len(text) - 2*len(title)*len(doc))/len(doc))
            # s = sum([len(i) for i in text_array])
            # print(len(text) - s)
            # print(len(text) - s - (len(text_array)-1)*2)
            # f.write(text)
            # print(text_array[0])

            print(title, "number of verses:", len(text_array))
            for i, txt in enumerate(text_array):
                nonum_txt = re.sub(remove_num_pattern, " ", txt)
                # get rid of the numbers inside the phrase
                lines_txt = [i.strip() for i in nonum_txt.split("\n")]
                # get rid of the strips inside each verse, so I will be able to collect them into single line
                oneline_txt = ""
                # the the verse text in online_string"ended_with_\n
                for j, line in enumerate(lines_txt):
                    if len(line) > 0:
                        if oneline_txt != "":
                            if line[0].isupper() and not oneline_txt.endswith("."+sep) and not oneline_txt[-1] in ";,'\"":
                                oneline_txt += "."+sep
                                # check the cases where coming from different pages and the first line in the page is new line "started with capitial"
                            if oneline_txt[-1] in ";,'\"":
                                oneline_txt += " "
                                # add space between the :,'\" a"
                        if line.endswith("."):
                            oneline_txt += line
                            oneline_txt += sep
                        elif line.endswith("-"):
                            oneline_txt += line[:-1]
                            # if line ended with - add the line without the dash
                        else:
                            oneline_txt += line
                            # the first line, or good shape line
                oneline_txt = oneline_txt.strip()
                text_array[i] = oneline_txt
                with open(folder_path+"/{}.txt".format(i+1), "w") as f:
                    f.write(oneline_txt)
            with open(folder_path+"/all.txt", "w") as f:
                f.write("\n".join(text_array))
            print("finished file {} of title {}".format(file, title))
