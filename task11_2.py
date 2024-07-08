
from collections import deque
from copy import deepcopy

pets = {} 

# Проверка есть ли id питомца в списке
def checkIdInList(id: int):
  if id in pets:
    return True
  else:
    print("питомца с таким id нет в списке")
    return False

# Подстановка правильного суффикса к занчению возраста
def get_suffix(age):
    strAge = str(age)
    lastNum = int(strAge[len(strAge) - 1])

    l1 = [5, 6, 7, 8, 9, 0]
    l2 = [2, 3, 4]

    if 5 <= age % 100 <= 20:
        return f'{age} лет'
    elif lastNum in l1:
        return f'{age} лет'
    elif lastNum in l2:
        return f'{age} года'
    else:
        return f'{age} год'
     
# вывод информации о питомце по id
def printData(data, nickname, id):
  print(f'Это {data["species"]} c id: {id} по кличке "{nickname}". Возраст питомца: {get_suffix(data["age"])}. Имя владельца: {data["owner"]}')

# создание нового питомца
def create():
  a_deque = deque(pets, maxlen=1)
  last = 0
  if a_deque:
    last = a_deque[0] + 1

  species = input('Введите породу питомца: ')
  nickname = input('Введите кличку питомца: ')
  age = int(input('Введите возраст питомца: '))
  owner = input('Имя владельца питомца: ')

  dataPet = {}
  dataPet['species'] = species
  dataPet['age'] = age
  dataPet['owner'] = owner
  pets[last] = {}
  pets[last][nickname] = dataPet
  print(f'питомец {nickname} добавлен')
  return last

# получение данных питомца по id
def get_pet(id: int):
  if checkIdInList(id):
    dataPet = pets[id]
    for k in dataPet.keys():
        printData(dataPet[k], k, id)


# получение данных всех питомцев
def pets_list():
  for k in pets.keys():
    get_pet(k)

# обновление данных питомца по id
def update(id: int):
  if checkIdInList(id):
    dataPet = deepcopy(pets[id])
    currentNickname = deque(dataPet, maxlen=1)[0]
    while True:
      command = input('введите поле(species/age/owner/nickname или save для сохранения изменений):')
      if command == 'species':
        species = input('Введите породу питомца: ')
        dataPet[currentNickname]['species'] = species
      elif command == 'age':
        age = int(input('Введите возраст питомца: '))
        dataPet[currentNickname]['age'] = age
      elif command == 'owner':
        owner = input('Имя владельца питомца: ')
        dataPet[currentNickname]['owner'] = owner
      elif command == 'nickname':
        nickname = input('Введите кличку питомца: ')
        dataPet[nickname] = dataPet[currentNickname]
        dataPet.pop(currentNickname)
      elif command == 'save':
        pets[id] = dataPet
        break

# удаление данных питомца по id
def delete(id: int):
  if checkIdInList(id):
    a = pets.pop(id)
    print(a)


# запуск бесконечного цикла выполнения программы
while True:
  command = input('введите команду(create/read/read_all/update/delete/stop):')
  if command == 'create':
    create()
  elif command == 'read':
    id = int(input('введите id питомца:'))
    get_pet(id)
  elif command == 'read_all':
    pets_list()
  elif command == 'update':
    id = int(input('введите id питомца:'))
    update(id)
  elif command == 'delete':
    id = int(input('введите id питомца для удаления:'))
    delete(id)
  elif command == 'stop':
    print('программа завершена')
    break
