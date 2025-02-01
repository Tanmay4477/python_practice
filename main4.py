users = [
    { 'user_id': 1, 'name': "Priyanka", 'email': "priyanka@gmail.com" },
    { 'user_id': 2, 'name': "Tanmay", 'email': "tanmay@gmail.com"},
    { 'user_id': 3, 'name': "Isha", 'email': "isha@gmail.com"},
    { 'user_id': 4, 'name': "Yagya", 'email': "yagya@gmail.com"},
    { 'user_id': 5, 'name': "Ragini", 'email': "ragini@gmail.com"},
    { 'user_id': 6, 'name': "Anushka", 'email': "annu@gmail.com"},
    { 'user_id': 7, 'name': "Prerna", 'email': "prerna@gmail.com"},
    { 'user_id': 8, 'name': "Sakshi", 'email': "sakshi@gmail.com"},
]

address = [
    { 'address_id': 1, 'user_id': 1, 'address': 'Sector 62', 'pincode': 201301 },
    { 'address_id': 2, 'user_id': 1, 'address': 'Sector 137', 'pincode': 201304 },
    { 'address_id': 3, 'user_id': 2, 'address': 'Sector 15', 'pincode': 201301 },
    { 'address_id': 4, 'user_id': 3, 'address': 'Sector 50', 'pincode': 201305 },
    { 'address_id': 5, 'user_id': 5, 'address': 'MG Road', 'pincode': 560011 },
    { 'address_id': 6, 'user_id': 7, 'address': 'MG Road', 'pincode': 201304 },
    { 'address_id': 7, 'user_id': 6, 'address': 'MG Road', 'pincode': 201301 },
    { 'address_id': 8, 'user_id': 8, 'address': 'MG Road', 'pincode': 560011 },

]

pincodes = [
    { 'pincode': 201301, 'city': 'Noida', 'state': 'Uttar Pradesh', 'country': 'India' },
    { 'pincode': 201304, 'city': 'Noida', 'state': 'Uttar Pradesh', 'country': 'India' },
    { 'pincode': 201305, 'city': 'Noida', 'state': 'Uttar Pradesh', 'country': 'India' },
    { 'pincode': 560011, 'city': 'Bangalore', 'state': 'Karnataka', 'country': 'India' },
]

globalCity = input("Tell the city name: ").capitalize()
pincodeList = []
userList = []
userName = []


for x in pincodes:
    if (x['city'] == globalCity):
        pincodeList.append(x['pincode'])

for x in address:
    if x['pincode'] in pincodeList:
        userList.append(x['user_id'])
        
    continue


for x in set(userList):
    for y in users: 
        if y['user_id'] == x:
            userName.append(y['name'])
    continue

print(userName)