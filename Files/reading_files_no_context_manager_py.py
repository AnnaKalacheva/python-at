

sample_file = './sample_files/programming_language_wikipedia.txt'

# demo 1
# my_file = open(sample_file, 'r')
# content = my_file.read()
# my_file.close()
# my_content_list = content.split('\n')
# print(content)

# demo 2
my_file = open(sample_file, 'r')
content = my_file.readline() #вывод только первой
my_file.close()
print(content)

# demo 3
# my_file = open(sample_file, 'r')
# content = my_file.readlines() #вывод всего текста в одну линию
# my_file.close()
# print(content)

# gotcha
# the .seek()

my_file = open(sample_file, 'r')
content = my_file.read() #read everything
print(content)
my_file.seek(0)
print("-------")
content_2 = my_file.read()
print(content_2)
print("2------")
my_file.close()
