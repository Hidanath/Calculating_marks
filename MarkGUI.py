import PySimpleGUI as sg

marks = []

def openWindow(): #Функция для окна выбора оценок
    global marks

    marksCount = lambda x: marks.count(x) if marks else 0 #Функция для получения количества определённого элемента если массив не пустой, если пустой то возвращает 0
        
    layoutAdd = [
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
            marksNew = [] #Массив новый значений
            for z in range(2,6): #Перебор значений от 2 до 5 включительно
                for i in range(values[f"spin{z}"]): #Получение значения spin от 2 до 5 и перебор в радиусе его значения
                    marksNew.append(z)  #Добавление значения из первого перебора

            marks = marksNew #Замещение старого массива новым

            break

    window.close() #Закрытие окна

sg.theme('Default1') #Указание темы программы
layout = [
    [sg.Text("Привет это программа для подсчёта оценок")],
    [sg.InputText(key="marks", disabled=True), sg.Button("+", key="add")],
    [sg.Text("Выставите нужный коффициент и оценку которой будем исправлять: ")],
    [sg.Slider(range=(2.5,5.0), resolution=0.1, orientation="horizontal", key="coefficient"), sg.Slider((3,5), orientation="horizontal", key="markTo")],
    [sg.Output((60,10))],
    
    [sg.Submit("Посчитать", key="calculate"), sg.Cancel("Закрыть", key="cancel")]
]

window = sg.Window('File Compare', layout) #Создание окна
while True: 
    event, values = window.read() #Чтение ивентов и значений
    # sg.Print(event, values)
    if event in (None, 'Exit', 'cancel'):
        break

    if event == "add": #При нажатии на кнопку добавить, вызывает функцию для окрытия нового окна
        openWindow()