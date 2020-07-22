'''

Код берет данные из из  'пример_csv_для_ДЗ.csv'
вставляет в шаблон  'template.docx' и
генерируются нескоколько новых документов
с расширением '....................тачкиПоточно.docx'

Это версия без множества функций.

'''


def generate_report(label, model, fuel, price,img):
    template = 'template.docx'
    signature = img
    template = DocxTemplate('template') # а можно сразу написать  'template.docx'
    context = {'label':label, 'model':model, 'fuel':fuel, 'price':price} # а можно в столбик

    img_size = Cm(10)
    acc = InlineImage(template, signature, img_size)
    context['acc'] = acc

    template.render(context) # мы же здесь не только картинку передаем?
    template.save(label+'_'+model+'_'+str(datetime.datetime.now().date()) + '_' + 'тачкиПоточно.docx')

    with open('пример_csv_для_ДЗ.csv') as f:
        lst = list(csv.reader(f))
        for elem in lst:
            label= elem[0]
            model= elem[1]
            fuel= elem[2]
            price= elem[3]
            img = elem[4]

            generate_report(label, model, fuel, price, img)



# Код исполняется (code 0), но файлы не изготавливает??!!?!?!?!?


# А если расход будет с запятой, делимитер менять?