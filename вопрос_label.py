''''

Почему то в этой версии кода, при выведении отчета о времени
генерации отчета, python не хочет заплнить {label} в (стр 40)

Не знаю почему???
'''

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
print(f'Время создания отчета по модели { label } : %.2f' %(time.time() - start) + 'секунды')