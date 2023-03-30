# for i in range(2):
#     print(i)

# for i in range(10):
#     print(i)

# my_list = []
# for i in range(8):
#     my_list.append('abc')
#
# print(my_list)
# print(len(my_list))

cars = ['mazda', 'toyota', 'ford', 'lamba', 'porsce']
for i in range(len(cars)):
    print(cars[i])
print('----')
for car in cars:
    print(car)


if len(cars) == 5:
    print("5")
elif len(cars) > 5:
    print("grater 5")
else:
    print("les than 5")