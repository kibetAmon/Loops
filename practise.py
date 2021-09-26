fw = open('sample.txt', 'w')
fw.write('i am amon kibet\n')
fw.write('i like random things\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()