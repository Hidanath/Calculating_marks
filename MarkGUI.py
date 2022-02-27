import PySimpleGUI as sg

marks = []

def openWindow(): #Функция для окна выбора оценок
    global marks

    marksCount = lambda x: marks.count(x) if marks else 0 #Функция для получения количества определённого элемента, если массив не пустой, если пустой - то возвращает 0
        
    layoutAdd = [ #Интерфейс
        [sg.Text("Введите ваши оценки: ")],
        [sg.Text("5"), sg.Spin([i for i in range(0, 1000)], key=("spin5"), initial_value=marksCount(5))],
        [sg.Text("4"), sg.Spin([i for i in range(0, 1000)], key=("spin4"), initial_value=marksCount(4))],
        [sg.Text("3"), sg.Spin([i for i in range(0, 1000)], key=("spin3"), initial_value=marksCount(3))],
        [sg.Text("2"), sg.Spin([i for i in range(0, 1000)], key=("spin2"), initial_value=marksCount(2))],
        [sg.Submit("Сохранить", key="save"), sg.Cancel("Закрыть", key="cancel")]
    ]    

    window = sg.Window("Second Window", layoutAdd, modal=True) #Создание окна
    while True:
        event, values = window.read() #Чтение ивентов и значений
        if event in (None, 'Exit', 'cancel'):
            break

        elif event == "save": #При нажатии на кнопку "сохранить"
            marksNew = [] #Массив новых значений
            for z in range(2,6): #Перебор значений от 2 до 5 включительно
                try:
                    if int(values[f"spin{z}"]) > 0: #Конвертирует строку в число и проверяет больше ли оно 0
                        for i in range(values[f"spin{z}"]): #Получение значения spin от 2 до 5 и перебор в радиусе его значения
                            marksNew.append(z)  #Добавление значения из первого перебора
                    

                except ValueError: #Возникает, если пользователь ввёл не число
                    pass #Срабатывает если введено нецелое положительное число

            marks = marksNew #Замещение старого массива новым

            break

    window.close() #Закрытие окна

def commaSlice(number, slice): #Функция оставняет нужное количество знаков после запятой
    comma = "1"
    for i in range(0, slice):
        comma += "0"
    
    return int(number * int(comma)) / int(comma)

def rounding(marksNow, coefficientTo, markTo): #Функция привидения к нужному коэффициенту
    marksAmount = len(marksNow) #Количество оценок
    marksSum = 0
    for i in marksNow: #Сумма всех оценок
        marksSum += int(i)

    coefficientNow = marksSum / marksAmount #Коэффициент сейчас
    coefficientLast = coefficientNow
    marksAmoutLast = marksAmount

    while coefficientNow < coefficientTo: #Если коэффициент сейчас меньше чем ожидаемый коэффициент
        marksNow.append(markTo) #Добавление оценки в массив
        marksAmount += 1 #Добавление оценки к общему количеству
        marksSum += markTo #Добавление оценки к общей сумме
            
        coefficientNow = marksSum / marksAmount #Новый коэффициент

    window["output"].Update(f"Старый коэффициент: {commaSlice(coefficientLast, 2)}\nНовый коэффициент: {commaSlice(coefficientNow, 2)}\nВам нужно получить: {marksAmount - marksAmoutLast}\nТип оценок: {markTo}") #Вывод всех данный в графический итерфейс



sg.theme('Default1') #Указание темы программы
layout = [ #Интерфейс
    [sg.Text("Привет! Это программа для подсчёта оценок")],
    [sg.InputText(key="marks", disabled=True), sg.Button("+", key="add")],
    [sg.Text("Выставьте нужный коффициент и оценку, на которую будем исправлять: ")],
    [sg.Slider(range=(2.5,4.9), resolution=0.1, orientation="horizontal", key="coefficient", enable_events=True), sg.Slider((3,5), orientation="horizontal", key="markTo")],
    [sg.Multiline(size=(60,10), key="output", disabled=True)],
    
    [sg.Submit("Посчитать", key="calculate"), sg.Cancel("Закрыть", key="cancel")]
]

window = sg.Window('File Compare', layout) #Создание окна
while True: 
    event, values = window.read() #Чтение ивентов и значений
    # sg.Print(event, values)
    if event in (None, 'Exit', 'cancel'):
        break

    if event == "add":
        openWindow()
        window["marks"].Update(value=marks) #Вписывание оценок в верхнюю строку

        if marks:
            marksSum = 0 #Сумма оценок
            for i in marks: #Высчитывает сумму всех оценок
                marksSum += int(i)

            coefficient = marksSum / len(marks) #Считает коэффициент
            window["coefficient"].Update(range=(commaSlice(coefficient, 1) + 0.1, 4.9)) #Обновление радиуса слайдера с желаемым коэффициентом на текущий коэффициент + 0.1

    if event == "coefficient":
        if values["coefficient"] >= 3.0 and values["coefficient"] < 4.0: #Если коэффициент больше или равен 3 и меньше 4
            window["markTo"].Update(range=(4,5)) #Обновление радиуса слайдера с оценкой. на  которую будем исправлять

        elif values["coefficient"] >= 4.0: #Если коэффициент больше или равен 4
            window["markTo"].Update(range=(5,5)) #Обновление радиуса слайдера с оценкой. на  которую  будем исправлять

        elif values["coefficient"] < 3.0: #Если коэффициент меньше 3
            window["markTo"].Update(range=(3,5)) #Обновление радиуса слайдера с оценкой. на  которую будем исправлять

    if event == "calculate":
        if marks: #Проверка введены ли оценки
            window["output"].Update("") #Очистка поля для вывода
            rounding(marks.copy(), float(values["coefficient"]), int(values["markTo"])) #Запуск функции для высчитывания коэффициента
        
        else:
            sg.popup("Введите оценки")