import datetime
import time

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# фаил = DocxTemplate("шаблон_1.docx")    #   DocxTemplate-> обрабатывает фаил указанный в скобках
# context = { 'Чего_Чего' : "КАКОЙ ТО текст, КАКОЙ ТО текст, КАКОЙ ТО текст, " }  # context -> указываем в какое место(за место {{Чего_Чего}} ) нужно вставить нужную инфу ('КАКОЙ ТО текст')
# фаил.render(context)                           # render -> рендерим (передаем данные) из contex в фаил( в наш шаблон_1.docx)
# фаил.save("что_то_получилось_1.docx")            # save -> создаем новый фаил (что_то_получилось_1.docx), где обьединили шаблон и инфу из context
#
# print()
# # Хочу заменить несколько пунктов в документе
# print('   Хочу заменить несколько пунктов в документе')
#
# фаил = DocxTemplate("шаблон_2.docx")    #   DocxTemplate-> обрабатывает фаил указанный в скобках
# context = { 'Чего_Чего' : 'КАКОЙ ТО текст', 'а_если':'исче', 'а_ещё':' да, возможно ' }  # context -> указываем в какое место(за место {{Чего_Чего}} ) нужно вставить нужную инфу ('КАКОЙ ТО текст')
# фаил.render(context)                           # render -> рендерим (передаем данные) из contex в фаил( в наш шаблон_1.docx)
# фаил.save("что_то_получилось_2.docx")            # save -> создаем новый фаил (что_то_получилось_1.docx), где обьединили шаблон и инфу из context
#
#
#
#
# ''''
# Встроенное изображение
# myimage = InlineImage(tpl,'test_files/python_logo.png',width=Mm(20))
#
# Вам просто нужно указать объект шаблона, путь к файлу изображения и,
# необязательно, ширину и / или высоту. Для высоты и ширины вы должны
# использовать миллиметры (Mm), дюймы (Inches) или точки (Pt).
# Пожалуйста, смотрите tests / inline_image.py для примера.
#
# '''
#
#
# # Хочу что бы автоматически данные брали из  документа csv и создавали новый документ вставляя в него данные
# print('   Хочу что бы автоматически данные брали из  документа csv\n и создавали новый документ вставляя в него данные')
#
#
# print()
# # csv.DictReader
# print('  пробую прочитать мой csv при помощи csv.DictReader')
#
# import csv
#
# with open('пример_csv_для_ДЗ.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
# print('   Словарь с данными в csv готов!!!   А ЗАЧЕМ НАМ СЛОВАРЬ???')
# print()
#
#
#
# print('Возможно мне нужен csv.reader')
#
# with open('пример_csv_для_ДЗ.csv') as f:
#     мои_данные = list(csv.reader(f))
#     print(мои_данные)
#     print('получилось, теперь это нужно вставить в код!!!')
#
#



print()
# Проба, код берет доки из csv и создант на их основе локументы в формате docx
print('    Проба, код берет доки из csv и создант на их основе локументы в формате docx')

def generate_report(label, model, fuel, price,img):
    template = 'template.docx'
    signature = img
    template = DocxTemplate(template) # а можно сразу написать  'template.docx'
    context = {'label':label, 'model':model, 'fuel':fuel, 'price':price} # а можно в столбик

    img_size = Cm(10)
    acc = InlineImage(template, signature, img_size)
    context['acc'] = acc  # а почему здесь не брекеты?

    template.render(context) # мы же здесь не только картинку передаем?
    template.save(label+'_'+model+'_'+str(datetime.datetime.now().date()) + '_' + 'тачкиНаБумаге.docx')

    with open('пример_csv_для_ДЗ.csv') as f:
        мои_данные = list(csv.reader(f))
        for i in мои_данные:
            label= i[0]
            model= i[1]
            fuel= i[2]
            price= i[3]
            img = i[4]

            generate_report(label, model, fuel, price, img)





# А если расход будет с запятой, делимитер менять?


