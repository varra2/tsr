# tsr
В файле tsp.py записан код решения симметричной замкнутой задачи коммивояжера с пятью (включая точку отправления) предзаданными точками. Для нахождения оптимального пути был применен метод прямого перебора с отсечениями (которые, однако, не понадобились на данном наборе точек) без использования рекурсивных функций.

В файле recursion.py код решения той же задачи для произвольного набора точек, в качестве метода снова использован перебор с отсечениями. Программа ожидает ввода от пользователя. Необходимо ввести координаты x,y всех точек через пробел. Ожидается, что первая точка в строке соответствует точке отправления. Получив данные, программа вызывает рекурсивную функцию для поиска оптимального пути.

