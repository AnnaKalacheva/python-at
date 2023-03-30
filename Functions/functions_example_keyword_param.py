#
#
# # Examples of using keyword parametrs
# # Example 1: write a function that will return the number of words that have X length, given a string
#
# def get_count_of_small_words(input_string, max_size=1):
#
#     small_words = [] #string
#     for word in input_string.split(): #becomes a list
#         if len(word) <= max_size:
#             small_words.append(word)
#     return len(small_words)
# my_string = "Why do we need to learn Python?"
# num_small = get_count_of_small_words(my_string) #default value 1 letter
# num_small = get_count_of_small_words(my_string,max_size=3) #count by 3 letters
# num_small = get_count_of_small_words(my_string,3) #the same action
# print(num_small)


#Example_2
def connect_to_database(host='test.com', username='testuser', password='none'):
    print(f"Connecting to host: {host}")
    print(f"Username: {username}")
    print(f"Password: {password}")

#connect_to_database() #default value
#connect_to_database(host='staging.com',password='dhdj') #changes for host and password
connect_to_database ("test")

