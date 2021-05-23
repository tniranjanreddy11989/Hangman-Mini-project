#!/usr/bin/env python
# coding: utf-8

#          
# 
# 
# 
# 
# 

# #                                         Hangman-Mini Project

# # Code Flow Diagram

# ![code%20flow%20dia.jpg](attachment:code%20flow%20dia.jpg)

# # Concepts used
# 1)split() 
# 2)Loops(while and for)
# 3)"not in" and "in"
# 4)len()
# 5)if,elif (conditional statements)
# 6)print and input functions
# 7)Functions(display())
# 8)string indexing

# # Instructions to run the program
# 
# 1)Run the code and the program shows the length of word by displaying '_'.
# 2)The program asks for user input
# 3)Type a character that you think the word to be predicted has and click on enter.
# 4)The program shows you weather your guess is write or wrong and the number of wrong attempts you can make.
# 5)If your guess in right then the program places the character, that you have given, in its place .
# 6)If your guess is wrong or you have given an empty input then you will loose an attempt.
# 7)Keep on giving the input untill you guess the word correctly or yours attempts get exhausted.

# In[5]:


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




