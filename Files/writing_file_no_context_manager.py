

my_string = "I love to program Python language"

# example 1

# my_f = open('./sample_files/sample_output_1.txt', 'w') #w - override the file
# my_f.write(my_string)
# my_f.close()

# example 2
my_f = open('./sample_files/sample_output_1.txt', 'w')
my_f.write(my_string)
my_f.write('\n') #add new line
my_f.write(my_string + '\n') #add new line
my_f.write(my_string)
my_f.close()