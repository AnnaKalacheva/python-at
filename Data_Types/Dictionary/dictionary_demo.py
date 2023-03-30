

capitals = {"USA": "Washington DC", "France": "Paris", "Belarus": "Minsk"}
print(type(capitals))

# # Getting items from the dictionary
# france_capital = capitals["France"] # 1dictionary name + key
# print(france_capital)
#
# france_capital2 = capitals.get("France") # 2dictionary name.get
# print(france_capital2)

# get key that doesn't exist
# albania_capital = capitals["Albania"] #will fall
# print(albania_capital)

# print("========")
# albania_capital = capitals.get("Albania")
# print(albania_capital)
#
# # retun a default value if key doesn't exist
# albania_capital2 = capitals.get("Albania", "Not exist")
# print(albania_capital2)

##########
# Adding item to dictionary
# Option_1

# capitals = {"USA": "Washington DC", "France": "Paris", "Belarus": "Minsk"}
# print("Before add")
# print(capitals)
# capitals["Cuba"] = "Havana" #var+key
# print("After add")
# print(capitals)

# # Option_2
# capitals.update({"Egypt": "Kairo"}) #+update
# print("Add option2")
# print(capitals)

# Assignment: what if you try to add a key that already exist - the value is updated (overwritten) with the new value
# capitals = {"USA": "Washington DC", "France": "Paris", "Belarus": "Minsk"}
# capitals["USA"] = 'Washington'
# print("after add")
# print(capitals)


# # space key added using setdefault() method
# capitals.setdefault(' ', 'Peru')
# print(capitals)


#########
capitals = {"USA": "Washington DC", "France": "Paris", "Belarus": "Minsk"}
all_keys = capitals.keys()
all_values = capitals.values()
print(all_values)
print(all_keys)

# Another example of a dictionary
employee = {"name" : 'Anna Kalacheva', #string
            "age": 33, #int
            "phone": 116372547, #int
            "title": "Web Designer", #string
            "skills": ["Composition","Software for design","Color theory"] #value.list
            }

e_name = employee ['name']
e_age = employee ['age']
e_skills = employee ['skills']
print(type(e_skills))
user_skill_count = len(e_skills)
print(user_skill_count)
print(f"User {e_name} has {user_skill_count} skills.")
# or
print("User {} has {} skills".format(e_name, user_skill_count))
