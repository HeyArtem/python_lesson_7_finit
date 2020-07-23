# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
print('   1) Вручную создать текстовый файл с данными')
print(' Я создал фаил template')


# 2) Создать doc шаблон, где будут использованы данные параметры.
print('   2) Создать doc шаблон, где будут использованы данные параметры.')

print()
# 3) Автоматически сгенерировать отчет о машине в формате docx (как в видео 7.2).
print('   3) Автоматически сгенерировать отчет о машине в формате docx (как в видео 7.2).')



import datetime
import time


from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage



def get_context(label, model, fuel, price):  # возвращает словарь аргументов
    return {
        'label': label,
        'model': model,
        'fuel': fuel,
        'price': price
    }


def from_template(label, model, fuel, price, template, signature):
    template = DocxTemplate(template)  # Формируем сам шаблон
    context = get_context(label, model, fuel, price)  # Dict с обьектами в словаре, получает контекст, используемый
    # для визуализации документа

    img_size = Cm(15)  # устанавливает размер изображения
    acc = InlineImage(template, signature, img_size)  # Обьект картинки

    context['acc'] = acc  # добавляет объект InlineImage в контекст
    template.render(context)  # Передаем картинку в обьект шаблона
    template.save(
        label + '_' + model + '_' + str(datetime.datetime.now().date()) + '_' 'тачка.docx')  # Сохраням обьект шаблона

start = time.time() # Начинаем замерять время работы функции
def generate_report(label, model, fuel, price):
    template = 'template.docx'
    signature = 'mzd.jpg'
    from_template(label, model, fuel, price, template, signature)


generate_report('Mazda', 'X-9', '11,5', '1900000')
print(f'Время создания отчета по модели : %.2f' %(time.time() - start) + 'секунды')



print()
# 4) Создать csv файл с данными о машине.
print('   4) Создать csv файл с данными о машине.')

import csv

''''
функция csv.reader -> Чтение в тип list
функция csv.writer -> Запись из листа

'''
start_4 = time.time()
car_data = [['brand', 'model', 'volume', 'fuel'], ['Kia', 'Rio', '1,4', '8'], ['Reno', 'Fluence', '1,6', '8,5'], ['Volkswagen', 'Polo', '1,5', '8,7'], ['Hyundai', 'solaris', '1,4', '7,8']]



with open('список_тачек.csv', 'w', newline='') as f:  # newline-> делает, что бы запись делалась каждую строку, а не через одну
    writer = csv.writer(f, delimiter = '>')  # Разделитель(delimiter), по умолчанию ','
    writer.writerows(car_data)
print('Writing complete!')



print(' * ')
print('ПРочитаю csv фаил "список_тачек"')

with open('список_тачек.csv') as f:
    читаю = csv.reader(f, delimiter = '>')
    for row in читаю:
        print(row)

print(f'Время создания csv отчета : %.3f' % (time.time() - start_4) + 'секунды')





print()
# 5) Создать json файл с данными о машине.
print('   5) Создать json файл с данными о машине. ')

start_time_5 = time.time() # часть задания 6 -> вычислить время выполнения кода


import json

dict_ex = {'brand':'Toyota', 'model':'Hilux', 'car type':'pickup', 'volume':'2.0'}

тачки_в_json = json.dumps(dict_ex) # с помощью метода dumps приводим к формату json
print(type(тачки_в_json), тачки_в_json)


with open('тачки_в_json_из_dict_ex.json', 'w') as f: # с помощью метода dump запишем в текстовый фаил
    json.dump(dict_ex, f)

print(f'Время выполнения кода по созданию json файла : %.3f' %(time.time() - start_time_5) + 'секунды' )


print()
# 6) Замерить время генерации отчета (время выполнения пункта 3).
# В каждый файл пунктов 4 и 5 добавить параметр: время, затраченное на генерацию отчета.
print('   6) Замерить время генерации отчета (время выполнения пункта 3).\n В каждый файл пунктов 4 и 5 добавить параметр: время, затраченное на генерацию отчета.')






