# Погружение в Python -> Неделя 2 -> Key-value хранилище
#https://www.coursera.org/learn/diving-in-python/programming/nc6Ce/key-value-khranilishchie
# Kamaldinov Maksim 2021

import argparse
import tempfile
import json

path_storage = tempfile.gettempdir() + "\\storage.txt"
# we will make storage file in temporary directory

def read(k):
    with open(path_storage, 'r') as f:
        temp = json.load(f) #read all data from file
        for key, v in temp.items():
            if key == k:
                print(f"{key}: {v}")
                exit()
        print("No such key")
        exit()

def write(k, v):
    with open(path_storage, 'r') as f:
        temp = json.load(f) #read all data from file
    print(temp)
    if k not in temp: temp[k] = v #find "key", if no - make "key"
    else: temp[k] = temp[k] + ", " + v
    print(temp)
    with open(path_storage, 'w') as f:
        json.dump(temp, f) # save new version data to file


"""
Start programm
"""

parse = argparse.ArgumentParser() #Создаем обьект парсер
parse.add_argument("--key") #добавляем необходимык аргументы
parse.add_argument("--val")
args = parse.parse_args() # считываем свойства обьекта полученные из командной строки
print("--key ", args.key)
print("--val ", args.val)

key = args.key
val = args.val

if key == None: # define all variants arguments of utility
    print("Plese enter argument '--key'")
    exit()
elif key != None and val != None:
    print("I will storage yours data.")
    write(key, val) # if exist "key" and "value" call - write()
else: read(key) # if exist only key - call read() func