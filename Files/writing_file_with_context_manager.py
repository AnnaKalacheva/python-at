
my_string = "I love programming in Python language"

# # ex 1
with open('./sample_output_2.txt', 'w') as my_f:
    my_f.write(my_string)

# ex 2
# my_l = ['user1','user2','user3']
# with open('./sample_output_2.txt', 'w') as my_f:
#     for i in my_l:
#         # my_f.write(i +'\n') #разделять с новой строки
#         my_f.write(i +'\t') #разделять по tab

# ex 3 (appending)
# var2 = "Also like testing"
# with open('./sample_output_2.txt', 'a') as f: #append добавляет к имеющейся
#     f.write('\n'+ var2)
#
# #ex 4
# my_langs = ['Python','JS','PHP','Java','Ruby']
# with open('./my_fav_language.csv','w') as f:
#     for i in my_langs:
#       f.writelines(i +'\n')

# ex 5
my_langs = ['Python','JS','PHP','Java','Ruby']
with open('./my_fav_language.csv','w') as f:
    str_my_langs = '\n'.join(my_langs)
    f.write(str_my_langs)

