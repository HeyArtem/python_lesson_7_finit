# 7.4. Формат JSON

import json

dict_ex = {'brand' : 'Volvo', 'Price' : 1.5, 'Vol' : 2.0}

# dumps поможет нам из словаря получить json

print('dump поможет нам из словаря получить json')

dict_to_json = json.dumps(dict_ex)
print(type(dict_to_json), dict_to_json)


print()
# dump запишет данные в фаил
print('   dump запишет данные в фаил')

with open('dict_to_json.txt', 'w') as f:
    json.dump(dict_ex, f)



print()
# load, loads для обратной конвертации
print('   load, loads для обратной конвертации')

with open('dict_to_json.txt') as f:
    data = json.load(f)
print(type(data), data)

print()
# loads
print('   loads -> из строки в словарь')

data_1 = json.loads(dict_to_json)
print(type(data_1), data_1)
print(type(dict_to_json), dict_to_json)



print()
# Реальный пример, ответ по API
print('    Реальный пример, ответ по API')

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data_2 = json.loads(response.text)
print(data_2)
