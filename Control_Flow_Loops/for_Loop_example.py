
# Example 1

my_property = ['car', 'house', 'boat', 'bike']
print(my_property)
print(my_property[0])
# for i in my_property:
#     print(i)
#     print('-----')
# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     print(fruit)

# Example 2

# for i in range(5):
#     print(i)

# for i in range (0,7):
#     print(i)

# Example 3 Print out words that are 3 or less characters
# quote = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime." #  string
# words_list = quote.split(' ') # вывести список LIST
# print(words_list)
# for i in words_list :
#     if len(i) <= 3:
#      print(i)

# OR shorter
# quote = "Give a man a program, frustrate him"
# for i in quote.split():
#     if len(i) <= 3:
#      print(i)

# Example 4
# collect the small words (3 or less characters) into a list and print a list
# quote = "Give a man a program, frustrate him"
# small_words = []
# for word in quote.split():
#     if len(word) <= 3:
#      small_words.append(word)
# print(small_words)

# What happens if you try to loop on empty list?
# my_cars = []
# for car in my_cars:
#     print(car)