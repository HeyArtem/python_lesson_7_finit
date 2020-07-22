import datetime
import time
from docxtpl import DocxTemplate
import csv

'''

Код берет данные из из  'пример_csv_для_ДЗ.csv'
и шаблон 'template.docx' 
после генерирует нескоколько новых документов
с расширением '....................ТачкиПоточно.docx'

'''



from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(label, model, fuel, price): # возвращает словарь аргументов
 return{
  'label': label,
  'model': model,
  'fuel': fuel,
  'price': price,
 }
 print('1') #test

def from_template(label, model, fuel, price, template, signature):
 template = DocxTemplate(template) # объект шаблона

 context = get_context(label, model, fuel, price) # Запустит первую функцию ->get_context

 img_size = Cm(15) #полотно картинки (размер)
 acc = InlineImage(template, signature, img_size) # объект картинки
 context['acc'] = acc # словарь, содержащий объект картинки

 template.render(context) # передаем картинку в объект шаблона и не только картинку??

 template.save(label + '_' + model + '_' + str(datetime.datetime.now().date()) + '_' + 'ТачкиПоточно.docx')

def generate_report(label, model, fuel, price, img):
 shablon = 'template.docx'
 signature = img
 from_template(label, model, fuel, price, shablon, signature) # Запускает функцию -> def from_template

#lst = [['BMW','320i','10','2000000', 'bmw.jpg'], ['Kia','Rio','8','800000','subaru.jpg']]
lst = []
 with open('пример_csv_для_ДЗ.csv') as f:
  lst = list(csv.reader(f))



for elem in lst:
 start = time.time() # замеряем время начала

 label = elem[0]
 model = elem[1]
 fuel = elem[2]
 price = elem[3]
 img = elem[4]

 generate_report(label, model, fuel, price, img) # формируем отчет

 end = time.time() # замеряем время окончания
 print(f"Время выполнения отчета для а/м {label} {model}: %.2f" %(end - start) + " секунд")




'''
- Почему созданные документы датируются датой 11.07.20?





'''