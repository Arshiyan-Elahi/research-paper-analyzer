""" Declare and initialize two variables, num1 and num2, with integer values. Calculate and print 
their sum." """ 

num1 = 5
num2 = 6
#print(num1 + num2)


message = 'hello'
message = message + " World!"

#print(message)

"""
Write a program that takes user input for their age and prints a message addressing their age 
group (e.g., "Teenager," "Adult").

"""


"""
User se 10 numbers lo
Positive, Negative, Zero ka count print karo

import string
vowels = ['a','e','i','o','u']

aplha=string.ascii_lowercase

name=aplha
count=0
for item in name:
    if item in vowels:
        print(f'vowels:  {(item)}')
        count=count+1

print(count)



even= len([i for i in range(1,51) if i % 2 == 0])
odd= len([i for i in range(1,51) if i % 2 != 0]) 

print(even,'\n',odd)


pass_counter=0
fail_counter=0

for i in range(3):
    marks=int(input(f'Enter marks of student {i+1}: '))
    if marks>=50 and marks<=100:
        pass_counter+=1

    elif marks<50:
        fail_counter+=1    

    else:
        print('invalid number')
print(f"Pass students: {pass_counter} \nFail Students: {fail_counter}")



num=input('enter num: ')
count=0

for i in num:
    if i.isdigit():
        count+=1

    else:
        print(f"'{i}' is not a digit")
    

print(count)



msg = '@$%&1234 abc de '

letters = [ch for ch in msg if ch.isalpha()]
digits  = [ch for ch in msg if ch.isdigit()]
spaces  = sum(ch.isspace() for ch in msg)
special = len(msg) - len(letters) - len(digits) - spaces
special_ch = [ch for ch in msg if not ch.isalpha() if not ch.isdigit() if not ch.isspace() ]

print("Letters:", len(letters), letters)
print("Digits :", len(digits), digits)
print("Spaces :", spaces)
print("Special:", special)
print("Special Char:", special_ch)




prime_count = len([n for n in range(2, 101) if all(n % i != 0 for i in range(2, n))])
print("Prime numbers between 1 and 100:", prime_count)




# --> RuNS DoG
def reverse_words_order_and_swap_cases(sentence:str):
    for ch in sentence:
        if ch.lower():
            ch.upper()
            
            
        
        elif ch.upper():
            ch.lower()
            print(ch.lower())
            

    
#print(reverse_words_order_and_swap_cases("rUns dOg" ))





def reverse_words_order_and_swap_cases(sentence: str) -> str:
    # 1️⃣ Words ka order reverse karo
    words = sentence.split()[::-1]  # list of words, reversed order
    swapped_sentence = ' '.join(words)
    
    return swapped_sentence


if __name__ == '__main__':
    result = reverse_words_order_and_swap_cases("rUns dOg")
    print(result)  # Output: DoG RuNS







# --> RuNS DoG
def reverse_words_order_and_swap_cases(sentence:str):
    splitted_sentence = sentence.split()[::-1]
    splitted_sentence = ' '.join(splitted_sentence)
    print(splitted_sentence)
    print('Actual Sentence: ',sentence)
    modified_sentence = ''
    for ch in splitted_sentence:
        if ch.islower():
            ch.upper()
            modified_sentence +=ch.upper() 
            #print('After: ',ch.upper())


        elif ch.isupper():
            ch.lower()
            modified_sentence +=ch.lower()
            #print('After: ',ch.lower())

        else:
            modified_sentence +=ch

    return f"Modified Sentence: {modified_sentence}"
        
print(reverse_words_order_and_swap_cases('Hi TheRe'))

    
    """


def group_by_owners(files):
    pass

if __name__ == "__main__":    
    pass




files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
#print((files.values()))



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
    'utils.py': 'Randy'
}

result = {}

for k, v in files.items():
    result.setdefault(v, []).append(k)
    pass

#print(result)
'''
2. Find the difference between the biggest and smallest values in the list
[4, 3, -9, 21, 0]
'''


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    days = ['mon' , 'tue','wed','thur','fri','sat','sun' ]

    for day in days:
        print(day)






nums = [1, 2, 4, 3, 8]
maxi = nums[0]

n=[]
for i in range(len(nums)):
    if nums[i] < maxi:
        print(nums[i], "==>", maxi)
        maxi = nums[i]

    else:
        n.append(nums[i])

print("Maximum:", maxi)
print("Not Maximum:", n)



