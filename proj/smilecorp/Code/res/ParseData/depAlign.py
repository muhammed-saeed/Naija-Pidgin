with open('dog_sentencest.txt', 'w') as out:
  with open('txt/feed_a_pet_dog.txt') as txt:
    with open('dep/feed_a_pet_dog.dep') as dep:
      for line in dep:
        if not line.strip():
          t = txt.readline()
          out.write(t)
          out.write('\n\n')
        else:
          out.write(line)



