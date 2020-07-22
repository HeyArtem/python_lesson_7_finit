import datetime
import time
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def generate_report(label, model, fuel, price, img):
     template = 'template.docx'
     signature = img

     template = DocxTemplate(template) # объект шаблона
     context = {'label': label, 'model': model, 'fuel': fuel, 'price': price, }



     img_size = Cm(10) #полотно картинки (размер)
     acc = InlineImage(template, signature, img_size) # объект картинки

     context['acc'] = acc # словарь, содержащий объект картинки

     template.render(context) # передаем картинку в объект шаблона
     template.save(label + '_' + model + '_' + str(datetime.datetime.now().date()) + '_' 'DEMO.docx')

lst = [['BMW','320i','10','2000000', 'bmw.jpg'], ['Subaru','Forester','8','800000','subaru.jpg']]
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