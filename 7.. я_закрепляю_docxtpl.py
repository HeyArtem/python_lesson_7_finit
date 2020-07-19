from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

фаил = DocxTemplate("шаблон_1.docx")    #   DocxTemplate-> обрабатывает фаил указанный в скобках
context = { 'Чего_Чего' : "КАКОЙ ТО текст" }  # context -> указываем в какое место(за место {{Чего_Чего}} ) нужно вставить нужную инфу ('КАКОЙ ТО текст')
фаил.render(context)                           # render -> рендерим (передаем данные) из contex в фаил( в наш шаблон_1.docx)
фаил.save("что_то_получилось_1.docx")            # save -> создаем новый фаил (что_то_получилось_1.docx), где обьединили шаблон и инфу из context