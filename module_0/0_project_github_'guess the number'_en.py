#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


def find_predict(number):
    """We provide the function with a number from 1-100 and it needs to "guess" the number in the least number of 
    attempts. The function generates a predicted number in the given range and compares it to our input number. 
    Each time after comparing with the input number the function divides the interval in halves, to make it more 
    efficient. The function eventually returns the number of attempts made in order to "guess" the number."""
    
    att_counter = 0 
    min_num = 1 
    max_num = 101 
    while True:
        predict = min_num + (max_num - min_num)// 2
        att_counter +=1
        if number == predict:
            break
        elif number > predict:
            min_num = predict + 1 # set predicted number as lower limit 
        elif number < predict:
            max_num = predict # set predicted number as upper limit 
    return att_counter # number of attempts needed to "guess" the number


def score_game(game_core):
    """Run the game 1000 times to check the average number of attempts needed to "guess" the number from 1-100, 
    using the function 'find predict'."""
    
    att_counter = [] 
    np.random.seed(1)  # fix RANDOM SEED so the experiment is reproducible 
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        att_counter.append(game_core(number))
    score = int(np.mean(att_counter))
    print(f"Your algorithm guesses on average the number in {score} attempts.")
    return(score)


score_game(find_predict) #print the average number of attempts 


# In[ ]:




