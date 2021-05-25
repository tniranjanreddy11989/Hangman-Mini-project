#!/usr/bin/env python
# coding: utf-8

# In[ ]:


choose = 'Watch the ABC Shows online at abc com Get exclusive videos and free episodes'.split()
#A random word will be taken from the above sentence using the below code written for word.

from random import randint
word = choose[randint(0,len(choose))] #word is selected randomly
lst = ['_' for i in range(len(word))]
def display():
    [print(lst[i],end=' ') for i in range(len(word))]
display()
 #initially the length of word is conveyed to the player by printing '_'s(no:of '_'=length of word selected) by using above code.
print('\n')#control goes to next line.
count =0
count1 =0
#defining two variables for further use. 
while count!=(len(word)+2) and count1 != len(word) : #initiating while loop with two conditions which help in breaking the loop.
    print('\n')
    user = input('user input:')#player is asked to give an input
    if user not in word:#if the given input character is not in the word then the below print statement and the no: of attepts left.
        count += 1 #for every wrong attempt count increases and when it reaches 2 more than length of word the while loop breaks.
        print ('oops! It is not present in the word.','\n','No of wrong guesses left:', (len(word)+2)-count)
    elif user!=''and user in word:#if the given input character is present in the word then the below statement is printed.
        print('It is present in the word. Hurrey!','\n','No of wrong guesses left:',(len(word)+2)-count)
    
        for i in range(0,len(word)):#this for loop replaces '_' with the user input which matches with the characters in the word.
            if word[i] == user:
                lst[i] = user
                count1 += 1 #for every replacement made in lst the count1 increases.
        
    display()
if count1 == len(word): #when the count1 is equal to length of word i.e all the replacements are made the below print statement is printed.
    print ('\n','You guessed the word correctly')
elif count == (len(word)+2):#when the user uses 2 more wrong attepts than the length of word then the below prrint statement is printed.
    print('\n', 'You have failed to guess the word')


# In[ ]:




