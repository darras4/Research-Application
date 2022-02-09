#Omar Darras
#OPD5033

from tkinter import *
from tkinter import messagebox
import itertools
from random import randrange
import random

def stablemarriage(men,women):
    n = len(men)
    taken = []
    matched_list = [] #what the function returns

    mFree = [True for i in men] #mfree[i] is True if men[i] is free

    while len(men) > 0 or len(matched_list = n): #Repeat until every man is free or matched_list has n matches
        for i in range(len(men)):
            mans_id = men[i][0]
            if mFree[i]:
                pref = men[i][1] -1 #mans first preference
                if pref == 0:
                    pref = randrange((len(women)-1)) #If indifferent, provide a random preference
                matched_list.append([men[i],women[pref]]) #match them together
                mFree[i] = False #set man as not free
                for x in range(1,len(men[i])):
                    for y in women[pref]:
                        if women[pref][y] == mans_id: #stop when we reach the matched man
                            break
                        if [men[y-1][0],women[pref][0]] in matched_list: #if there is an engagement with man that the woman prefers more, break engagement
                          matched_list.remove([men[i][0],women[pref][0]])
                        
                          taken.append(men[y])

            
        
        if len(matched_list) != n: #For every match where man is at the tail of w's list, break engagement
            for i in range(0,len(matched_list)):
                for x in range(1,len(matched_list[i][1])):
                    if (matched_list[i][1][x] != matched_list[i][0][0]):
                        matched_list.remove(matched_list[i])
    
        else:
            break

                
    print(matched_list)


                

#This function takes in a random number n and returns a list of men and women
#where each man and each women has a order of preference for the other gender
def randomgenerator(n):
    n = n+1
    men=[]
    women=[]
    randomnumbers = []
    
    #This part adds the ID of the man, then generates n random numbers between 0 and n
    #then appends them to the list of preferences for the man
    for i in range(1,n):
        men.append([i])
        men[i-1].append(random.sample(range(n),n))
        for x in men[i-1][1]:
            men[i-1].append(x)
        men[i-1].remove(men[i-1][1])

    #This part adds the ID of the woman, then generates n random numbers between 0 and n
    #then appends them to the list of preferences for the woman
    for i in range(1,n):
        women.append([i])
        women[i-1].append(random.sample(range(n),n))
        for x in women[i-1][1]:
            women[i-1].append(x)
        women[i-1].remove(women[i-1][1])
    
    return(men,women)
            
        


#driver code
#Change number to n to generate n men and n women
men,women = randomgenerator(5)
stablemarriage(men,women)


'''
GUI Code

top = Tk()
L1 = Label(top, text = "Input n")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

n = tk.

top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Run", command = helloCallBack()
B.place(x = 50,y = 50)
top.mainloop()
'''

            
            

'''
First Attempt
for i in range(len(men)):
        checker = 0 #No other man has the same preference
        if men[i][1] == 0:
            unmatched_men.append(men[i])
            continue
        if mFree[i]:
            pref1 = men[i][1]
            pref2 = men[i][2]
            
            for x in range(i+1, len(men)): #check for common preferences
                if checker == 2:
                   break
                if pref1 == men[x][1]:
                    checker = 1 #Atleast one other man has the same 1st preference
                    if pref2 == men[x][2]:
                        checker = 2 #Atleast one other man has the same 2 preferences                            
                        unmatched_men.append(men[i])
                        unmatched_men.append(men[x]) #adds both of them to unmatched list

            if (checker == 0 and wFree[pref1] == False): #if woman1 prefers man1, match
                if women[pref1][1] == men[i][0]:
                    matched_list.append([men[i][0],women[pref1][1]])
                    mFree[i] = True                        
                    wFree[pref1] = True

            if (checker == 1 and wFree[pref2] == False) or (checker == 0 and wFree[pref1] != False): #if woman2 prefers man1 or woman1 is not free, match
                if women[pref2][1] == men[i][0]:
                    matched_list.append([men[i][0],women[pref2][1]])
                    mFree[i] = True
                    wFree[pref2] = True
'''



                    



                




