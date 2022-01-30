# можно было бы обойтись без библиотек, но с numpy удобнее
import numpy as np

# Координаты точек
dots =[(0,2), (2,5), (5,2), (6,6), (8,3)]
#dots =[(0,1), (0,5), (0,2), (0,4), (0,3)] #для теста 

# Количество точек заношу в отдельную переменную, чтобы не считать заного каждый раз, как понадобится
lendots = len(dots)

# функция для расчёта расстояния между точками
def distance(point_1, point_2):
    return np.sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)

# Массив хранит расстояния между каждыми двумя точками
distances = np.empty([lendots, lendots])
for i in range(lendots):
    for j in range(lendots):
        distances[i,j] = distance(dots[i],dots[j])

# Начальное значение "оптимального пути" задаётся таким, что любое расстояние из возможных его не превысит
optway = np.sum(np.amax(distances, axis=0))

#Номера пунктов, доступных для выбора первой (не нулевой) точки маршрута заносятся в сет
choice1 = set(range(1,lendots))

for point_1 in choice1:
    #После выбора первой точки маршрута, длина пути равна расстоянию между нулевой точкой и первой
    myway = distances[0, point_1]
    #Сохраняем в отдельную переменную путь пройденный до сего момента - для удобства выведения ответа
    step_1 = myway

    #Для выбора каждой следующей точки доступны оставшиеся после выбора предыдущих пункты
    choice2 = choice1.difference({point_1})
    for point_2 in choice2:
        #Расстояние между предыдушей и нынешней точкой заносятся в переменную с коротким названием "звено" для удобства
        link = distances[point_1, point_2]
        #Если добавление выбранной точки увеличивает длину маршрута т.о., что она уже больше предела - отбрасываем этот вариант
        if myway+link >= optway:
            continue
        #Если нет - добавляем "звено" в общую длину пути
        myway+=link
        step_2 = myway

        choice3 = choice1.difference({point_1, point_2})
        for point_3 in choice3:
            #Те же действия повторяем при выборе следующих точек
            link = distances[point_2, point_3]
            if myway+link >= optway:
                continue
            myway+=link
            step_3 = myway

            choice4 = choice1.difference({point_1, point_2, point_3})
            for point_4 in choice4:
                #Так как эта точка - последняя в маршруте, проверки больше не имеют смысла, смотрим конечную длину пути
                step_4 = myway + distances[point_3, point_4]
                myway = step_4 + distances[point_4, 0]
                #Если полученный путь короче предыдущего оптимального пути, запоминаем его как оптимальный и сохраняем путь со всеми промежуточными точками и расстояниями для ответа
                if myway < optway:
                    optway = myway
                    answer = f"{dots[0]} -> {dots[point_1]} [{step_1}] -> {dots[point_2]} [{step_2}] -> {dots[point_3]} [{step_3}] -> {dots[point_4]} [{step_4}] -> {dots[0]} [{optway}] = {optway}"
            #откатываем пройденный путь к тому значению, которое у нас было до последней развилки
            myway = step_2
        #откатываемся на шаг назад
        myway = step_1

print(answer)