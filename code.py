# --------------
#Code starts here




def palindrome_check(num):
    num=str(num)
    return (num[::-1]==num)




def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
        


print(palindrome(123))


# --------------
#Code starts here


def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)



print(a_scramble("labratory","bat"))

    




# --------------
#Code starts here
import math

def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 

def check_fib(num):
     return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4) 




check_fib(145)


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here




def k_distinct(string,k):
    string=string.lower()
    all_freq = {} 
    
    for i in string: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    
    if len(all_freq)==k:
        return True
    else:
        return False










k_distinct('banana',4)



