#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


def find_predict(number):
    """Угадываем число от 1 до 100 за наименьшее количество попыток. Функция принимает загаданное число и 
    возвращает число попыток, при этом интервал, в котором может находится загаданное число, после каждой попытки
    (сравнение предполагаемого числа с загаданным) делит пополам."""
    
    att_counter = 0 
    min_num = 1 
    max_num = 101 
    while True:
        predict = min_num + (max_num - min_num)// 2 
        att_counter +=1
        if number == predict:
            break
        elif number > predict:
            min_num = predict + 1 # минимально возможное число
        elif number < predict:
            max_num = predict # максимально возможное число
    return att_counter # количество попыток для угадывания числа


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать cреднее количество попыток, требующихся алгоритму для угадывания 
    числа от 1 до 100, с помощью функции 'find predict'."""
    
    att_counter = [] 
    np.random.seed(1)  # фиксируем RANDOM SEED
    random_array = np.random.randint(1,101, size=(1000)) 
    for number in random_array:
        att_counter.append(game_core(number))
    score = int(np.mean(att_counter))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    return(score)


score_game(find_predict) #выводим среднее число попыток для угадывания числа 


# In[ ]:




