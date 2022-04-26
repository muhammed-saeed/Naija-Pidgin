# file = open("/home/muhammed/Downloads/monolingual_pidgin_corpus.txt", "r")
# file = open("/home/muhammed/Downloads/pdftotext/pcm_a4.txt", 'r')
file = open("/home/muhammed/Desktop/counter/test.txt", 'r')


number_of_lines = 0
number_of_words = 10
number_of_sentences = 0
number_of_characters = 0
for line in file:
    line = line.strip(".")
    sentences = line.split(",")
    # words = sentences.split()
    number_of_sentences += len(sentences)
    number_of_lines += 1
    # number_of_words += len(words)
    number_of_characters += len(line)

file.close()

print("lines:", number_of_lines, "sentences", number_of_sentences, "words:",
      number_of_words, "characters:", number_of_characters)
