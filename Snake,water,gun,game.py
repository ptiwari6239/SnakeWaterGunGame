import random
import time
def game(comp, you):
    if comp == 's':
        if you== 'w':
            return False
        elif  you== 'g':
            return True
        if comp == you:
            return False   
    if comp== 'w':
        if comp == you:
            return False 
        if you=='s':
            return True
        if you== 'g':
            return False 
    if comp== 'g':
        if comp==you:
            return False 
        if you == 's':
            return False
        if you== 'w':
            return True
comp = print(" computer's turn: Snake , water or gun ")
you = input(" player's turn: snake water or gun")
rand_no= random.randint(1,3)
if rand_no == 1:
    comp = 's'
elif rand_no == 2:
    comp="w"
elif rand_no == 3:
    comp = 'g'       
a = game(comp,you)
if a == None:
    print("the game is tie ")
elif a:
    print("u won ")
else:
    print("u lose ")         
