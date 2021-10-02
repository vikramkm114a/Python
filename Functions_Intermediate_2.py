x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x[1][0])
x[1][0] = 15
print(x[1][0])

# Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students[0]['last_name '])
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name '])
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory['soccer'])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# 2. Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for item in some_list:
        print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")



iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

for key, value in students[0].items():
    print('key: ', key)
    print('value: ', value)