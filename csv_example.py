# 7.3. Формат CSV

import csv

''''
функция csv.reader - чтение в лист
функция csv.writer - запись из листа
класс csv.Dictwriter - класс записи в словарь
класс csv.DictReader - класс чтения в словарь

'''

# csv.writer
print('   csv.writer')

car_data = [['brand', 'price', 'year'],['Volvo', 1.5, 2017],['Lada', 0.5, 2018],['Audi', 2.0, 2018]]

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter = '&') # delimiter = '&'
    writer.writerows(car_data)
print('Writing complete')


print()
# csv.reader
print('   csv.reader')

with open('example.csv') as f:
    reader = csv.reader(f, delimiter = '&')
    for row in reader:
        print(row)




print()
# csv.Dictwriter
print('   csv.Dictwriter')

data_dict = [{'Name': 'Dima', 'age': '28'},
             {'age': '29', 'Name': 'Kate'},
             {'Name': 'Mike', 'age': '31'}]

fieldnames = ['Name', 'age']

with open('example_1.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter = '&', fieldnames = fieldnames)
    writer.writeheader()
    for i in range (len(data_dict)):
        writer.writerow(data_dict[i])



print()
# csv.DictReader
print('   csv.DictReader')

with open('example_1.csv') as f:
    reader = csv.DictReader(f, delimiter = '&')
    for row in reader:
        print(dict(row))



print()
# Для анализа используют Pandas
print('    Для анализа используют Pandas')

import pandas as pd

DataFrame_from_csv = pd.read_csv('example_1.csv', sep = '&')
print(type(DataFrame_from_csv))
print(DataFrame_from_csv)



# Это я для домашки тренировался

''''

функция csv.reader -> Чтение в тип list
функция csv.writer -> Запись из листа
класс csv.Dictwriter -> Класс, запись в обьект типа словарь
класс csv.DictReader -> Класс, чтение в обьект типа словарь

'''







data_school_dict = [{'Name':'Dima', 'age':'10', 'Grade':'A'},
               {'Name':'Vasia', 'age':'11', 'Grade':'C'},
               {'Name':'Hasim', 'age':'13', 'Grade':'f'},
               {'Grade':'B', 'Name':'Zoy', 'age':'14'}]
fieldnames = ['Name', 'age', 'Grade']
with open('Список_учеников.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, delimiter = '-', fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data_school_dict)):
        writer.writerow(data_school_dict[i])
print('   Writing Список_учеников.csv complete!')

print(' * ')

with open ('Список_учеников.csv') as f:
    reader = csv.DictReader(f, delimiter = '-')
    for row in reader:
        print(row) #  У меня выведется dict, у преподавателя tuple   ( [('Name','Dima'),('age','10')] )


print(' * ')

import pandas as pd
проба_pandas_from_csv = pd.read_csv('Список_учеников.csv', sep = '-')
print(type(проба_pandas_from_csv))
print(проба_pandas_from_csv)