from matplotlib import pyplot as plt   
# import matplotlib.pyplot as plt
import random
# Задача 1. Постройте график функции
# 𝑓(𝑥)=5𝑥^2 + 10𝑥 − 30
# По графику определите, при каких значения x значение функции отрицательно.
def Graph_find():
    x = []
    y = []
    for i in range(-15,15):
        x.append(i)

    for i in range(len(x)):
        y.append(5 * x[i] * x[i] + 10 * x[i] - 30)
    
    plt.plot(x,y)   
    
    plt.title("Line graph") 
    plt.xlabel('X')    
    plt.ylabel('Y')    
    plt.show()  
# Отрицательно при х <= -1,6
Graph_find()


# 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
def House_analitics():
    area_of_house = [random.randint(100, 300) for i in range(0,15)]
    priсes = [random.randint(3000000, 20000000) for i in range(0,15)]
    priсe_of_meter = []
    low_priсe = []
    x = []
    sorted_houses = []

    for i in range(0,15):
        x.append(i+1)

    for i in range(len(area_of_house)):
        priсe_of_meter.append(round(priсes[i]/area_of_house[i]))

    print(area_of_house)
    print(priсe_of_meter)

    for i in range(len(priсe_of_meter)):
        if priсe_of_meter[i] < 50000:
            low_priсe.append(priсe_of_meter[i])
            sorted_houses.append(area_of_house[i])

    for i in range(len(sorted_houses)-1):
        for j in range(len(sorted_houses)-i-1):
            if sorted_houses[j] > sorted_houses[j+1]:
                low_priсe[j], low_priсe[j+1] = low_priсe[j+1], low_priсe[j]
                sorted_houses[j], sorted_houses[j+1] = sorted_houses[j+1], sorted_houses[j]

    print('\nДома, со стоимостью квадратного метра меньше 50000 рублей: ')
    for i in range(len(low_priсe)):
        print(f'Дом с площадью {sorted_houses[i]} кв. метра, стоимость квадратного метра {low_priсe[i]}')

    plt.title('Стоимость квадратного метра каждого дома')
    plt.xlabel('Номер дома')    
    plt.ylabel('Стоимость квадратного метра')  
    plt.grid(which='major')

    plot2 = list(50000 for a in range(1, 16))
    plt.plot(x, plot2)
    plt.plot(x, priсe_of_meter, 'go')
    plt.show()
House_analitics()