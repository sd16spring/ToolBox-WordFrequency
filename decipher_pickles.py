from pickle import load, dump
a = load(open('dickens_texts.pickle'))
new_file = open('great_expectations.txt', 'w')
print type(a[0])
new_file.write(a[0])