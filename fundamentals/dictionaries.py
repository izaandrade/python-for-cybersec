# dictionaries

# key - name it whatever you want
# value - also

# 'key':value

person = {
    'name' : 'iza',
    'job' : 'cybersec analyst',
    'age' : 21,
    'is_employeed' : True,
    'hobbies' : ['jogging', 'running', 'dancing']
}

hobbies_list = person['hobbies']

print(hobbies_list[2])
print(person['hobbies'][0])
#print(person)
#person['eats_cheese'] = True
#print(person)

people = [{'name' : 'Lloyd'}, {'name' : 'Iza'}, {'name' : 'Josh'}]
for person in people:
    print(person['name'])