from sys import exit

try:
    marks = input("Введите оценки через запятую: ").strip().replace(",", " ")
    isDigit = int(marks.replace(" ", ""))
    marks = marks.split()

except KeyboardInterrupt:
    exit()

except:
    print("Ошибка, возможные причины:\n1)Вы ввели не числа\n2)Вы ввели числа не разделяя их запятой\n3)Вы оставили строку пустой")
    exit()

marksAmount = len(marks)
marksSum = 0
coefficientBefore = 0
coefficientAfter = 0

def getRoundingMark():
    while True:
        try:
            markRound = int(input("Выберите до какой оценки округляем 5 или 4: ").strip())
            if markRound == 4:
                break

            elif markRound == 5:
                print("")
                break

            print("Неверное число\n")

        except KeyboardInterrupt:
            exit()

        except:
            print("Неверное число\n")

    return markRound

def Rounding(mark, marks):
    global coefficientAfter
    marksSum = 0
    marksAmount = len(marks)
    lastMarksAmount = marksAmount
    markTo = 0
    if mark == 5:
        while coefficientAfter < 4.5:
            marks.append(5)
            marksAmount += 1
            for i in marks:
                marksSum += int(i)
            
            coefficientAfter = marksSum / marksAmount
            marksSum = 0

        newMarksAmount = marksAmount - lastMarksAmount
        return newMarksAmount, 5

    elif mark == 4:
        while True:
            try:
                markTo = int(input("Выберите какой оценкой будем округлять 5 или 4: ").strip())
                if markTo == 4 or markTo == 5:
                    print("")
                    break
                print("Неверное число\n")

            except KeyboardInterrupt:
                exit()

            except:
                print("Неверное число\n")

        if markTo == 5:
            while coefficientAfter < 3.5:
                marks.append(5)
                marksAmount += 1
                for i in marks:
                    marksSum += int(i)
                
                coefficientAfter = marksSum / marksAmount
                marksSum = 0

            newMarksAmount = marksAmount - lastMarksAmount
            return newMarksAmount, 5

        elif markTo == 4:
            while coefficientAfter < 3.5:
                marks.append(4)
                marksAmount += 1
                for i in marks:
                        marksSum += int(i)
                    
                coefficientAfter = marksSum / marksAmount
                marksSum = 0

            newMarksAmount = marksAmount - lastMarksAmount
            return newMarksAmount, 4

def CommaSlice(number, slice):
    comma = "1"
    for i in range(0, slice):
        comma += "0"
    
    return int(number * int(comma)) / int(comma)

for i in marks:
    marksSum += int(i)

coefficientBefore = marksSum / marksAmount
newMarksAmount, mark = Rounding(getRoundingMark(), marks)

print(f"Базовый коэффицииент: {CommaSlice(coefficientBefore, 2)}\nКоэффицииент после исправления: {CommaSlice(coefficientAfter, 2)}\nДля исправления нужно получить: \nКоличество оценок: {newMarksAmount}\nТип оценок: {mark}")