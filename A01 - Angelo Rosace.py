#!/usr/bin/env python
# coding: utf-8

# Advanced Statistics: Assignment 1
# 
# Angelo Rosace
# 
# 1. Write a function that list all the possible outcomes with five dice.

# In[6]:

import random

#The function fills up a list with lists containing all possible results that could be obtained by throwing 5 dice.
#In this sense there is room for repetitions of outcomes.
def get_outcomes_with_5_dice():
    #empty starting list of outcomes
    possible_outcomes = [[]]
    #for loop iterating through a range of numbers from 0 to n, n being excluded, that is the number of the dice that are rolled.
    for flip in range(5):
        #a copy list is generated
        tmp = possible_outcomes.copy()
        #starting list is emptied
        possible_outcomes = []
        #for loop iterating through the results currently stored in the copy list.
        for current_outcome in tmp:
            #for each one of the already computed intermidiate outcomes the result of another die is added.
            for outcome in range(6):
                possible_outcomes.append(current_outcome + [outcome+1])
    #the complete list is returned
    return possible_outcomes
    

#result = get_outcomes_with_5_dice()
#print("All possible outcomes length:", len(result))
#for a in result:
#    print(a)


# We know that all the possible combinations of results of throwing 5 dice simultaneously are 6 to the power of 5. This calculation gives 7776 as a result which corresponds to the length of our list of outcomes. This means that all the possible outcomes have been correctly generated.

# 2. Write a function that takes a number of dices and return all the possible outcomes for that amount of dices.
# 
# The function implemented is the same as the one of the chunk above with the addition of a paramenter that let us state how many dice are we throwing. I could have just implemented this function also for the question above but I wanted to separated for the purpose of answering both question as completely as I could.
# 
# Here are some examples of the result of throwing 3, 15 and 50 dice.
# For a metter of readability just the length of the generated lists are printed below.

# In[ ]:


#the function takes as an input a number describing the number of the dice we are rolling simultaneously.
#It fills up a list with lists containing all possible results that could be obtained by throwing n dice.
#In this sense there is room for repetitions of outcomes.
#n is the number of dice we are rolling.
def get_outcomes(n):
    #empty starting list of outcomes
    possible_outcomes = [[]]
    #for loop iterating through a range of numbers from 0 to n, n being excluded, that is the number of the dice that are rolled.
    for flip in range(n):
        #a copy list is generated
        tmp = possible_outcomes.copy()
        #starting list is emptied
        possible_outcomes = []
        #for loop iterating through the results currently stored in the copy list.
        for current_outcome in tmp:
            #for each one of the already computed intermidiate outcomes the result of another die is added.
            for outcome in range(6):
                possible_outcomes.append(current_outcome + [outcome+1])
    #the complete list is returned
    return possible_outcomes
    
#print("All possible outcomes length for the throw of 3 dice:", len(get_outcomes(3)))
#print("All possible outcomes length for the throw of 4 dice:", len(get_outcomes(4)))
#print("All possible outcomes length for the throw of 5 dice:", len(get_outcomes(5)))


# In[ ]:


#3. Write functions that return, given five dice, True or False if we have Straight, Full,Poker or Generala.


# In[32]:


def check_equal(lst):
    return lst[1:] == lst[:-1]


def is_straight(result):
    for i in result:
        if result.count(i) > 1:
            #print(result,"is not a straight")
            return 0
    #print(result, "is a straight")
    return 1


#is_straight([1,2,3,4,5])
#is_straight([1,1,3,4,5])
#is_straight([1,2,3,5,5])

def is_full(result):
    result.sort()
    full = 0
    if check_equal(result[0:2]):
        if check_equal(result[2:5]):
            full = 1
    if (full == 0) and check_equal(result[0:3]):
        if check_equal(result[3:5]):
            full = 1
    #if full == 1:
        #print(result,"is a full")
    #else:
        #print(result,"is not a full")
    return full


#is_full([1,3,3,1,3])
#is_full([1,3,1,3,1])
#is_full([1,1,3,2,4])
#is_full([1,1,1,4,5])
#is_full([3,4,5,6,1])


def is_poker(result):
    result.sort()
    poker = 0
    if check_equal(result[0:4]) or check_equal(result[1:5]):
        poker = 1
        #print(result,"is a poker")
    #else:
    #    print(result,"is not a poker")
    return poker


#is_poker([1,1,1,1,3])
#is_poker([1,3,3,3,3])
#is_poker([2,2,3,3,3])
#is_poker([3,4,5,6,2])

def is_generala(result):
    generala = 0
    if check_equal(result):
        generala = 1
        #print(result, "is a generala")
    #else:
        #print(result, "is not a generala")
    return generala


#is_generala([1, 1, 1, 1, 1])
#is_generala([1, 1, 1, 1, 4])


# In[ ]:


#4. Compute the probabilities that you already computed by hand by counting the
#outcomes describing each roll result in the list of all possible hands served.

def is_served_probability():
    total_outcomes = get_outcomes_with_5_dice()
    n_total_outcomes = len(total_outcomes)
    n_generala = 0
    n_full = 0
    n_poker = 0
    n_straight = 0
    for i in total_outcomes:
        if is_generala(i):
            n_generala = n_generala + 1
        if is_full(i):
            n_full = n_full + 1
        if is_poker(i):
            n_poker = n_poker + 1
        if is_straight(i):
            n_straight = n_straight + 1
    probabilities = {
        "generala" : (n_generala/n_total_outcomes),
        "full" : (n_full/n_total_outcomes),
        "poker" : (n_poker/n_total_outcomes),
        "straight" : (n_straight/n_total_outcomes)
    }
    #print("the calculated probabilities for a served hand are:")
    #for key in probabilities:
    #    print(key, " = ", probabilities[key])
    return probabilities

is_served_probability()

#5. Compute the probabilities that you already computed by hand by counting the
#outcomes describing each roll result in the list of all possible hands.

def is_not_served_probability():
    probabilities = is_served_probability()
    print("the calculated probabilities for a non served hand are:")
    for key in probabilities:
        probabilities[key] = (probabilities.get(key)*3)
    for key in probabilities:
        print(key, " = ", probabilities[key])
    return probabilities

is_not_served_probability()

#6. Write a function that simulate a roll with n fair dices.

#this function simulates the roll of n fair dices by using random numbers in a range from one to six as result of a thorw of dice.
#the parameter n is the number of dice that are thrown simultaneously

def roll(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 6))
    return result

#7. Write a function that plays automatically, always looking for a Generala with a greedy
#strategy (always keeping the most dices of the same kind and rolling the others) that
#returns True if we get a Generala and a False otherwise. Which kind of distribution
#follow this function results? Explain your reasoning within the delivered python
#notebook.


def get_longest_matched_sequence(list):
    longest_seq = {}
    for i in list:
        if not i in longest_seq:
            longest_seq[i] = 1
        else:
            longest_seq[i] = longest_seq.get(i) + 1
    max_value = max(longest_seq, key=longest_seq.get)
    seq = [max_value] * longest_seq[max_value]
    return seq

#n is the number of dice we are rolling
#k is the maximum amount of time we can reroll all or some of the dice

def get_generala(n,k):
    return get_generala_aux([],[],n,k,5)

def get_generala_aux(result,keep,n,k,expected_len):
    if is_generala(result) and len(result) == expected_len:
        print("You got a generala!", result)
        return True
    else:
        if k == 0 and (not is_generala(result)):
            print("maximum number of re-rolls reached without a generala", result)
        else:
            intermediate_result = roll(n)
            for i in intermediate_result:
                keep.append(i)
            result = keep
            keep = get_longest_matched_sequence(keep)
            new_n = expected_len - len(keep)
            return get_generala_aux(result, keep, new_n, (k-1), expected_len)

#8. Write a function that plays until it gets a Generala, count how many times it had to
#play to get it and return this number. Which kind of distribution follow this function
#results? Explain your reasoning within the delivered python notebook.

def play_until_generala():
    number_of_attempts = 0
    while True:
        number_of_attempts = number_of_attempts + 1
        if get_generala(5, 3):
            break
    print("You had to play ", number_of_attempts, "times before getting a generala")
    return number_of_attempts


#play_until_generala()



