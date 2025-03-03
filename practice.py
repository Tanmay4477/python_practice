unique list

def unique_list(list_array):
    new_list = set(list_array)
    print(list(new_list))



list_array = [1, 2, 1, 1, 1, 2 ,1, 3, 2, 3, 2, 2, 2]
unique_list(list_array)


time logging decorator
import time

def timer(func):
    print("It is started")
    func()
    print("It is ended")

@timer
def print_something():
    time.sleep(2)



fetch data 
import requests

url = "https://jsonplaceholder.typicode.com/users"


try:
    response = requests.get(url)
    y = response.json()
except Exception as e:
    print(e)


for x in y:
    print(x['name'])









