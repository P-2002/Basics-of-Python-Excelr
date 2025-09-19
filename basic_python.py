"""
**Prime Numbers**
"""

num=int(input("Enter any number: "))

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
             print(num, "is not a prime number")
             break
    else:
      print(num, "is a prime number")

else:
        print(num, "is not a prime number")

"""**Product of Random Numbers**"""

import random
num1=random.randint(1,10)
num2=random.randint(1,10)
correct_product=num1*num2
user_product=int(input(f"What is the product of {num1} and {num2}? "))
if user_product == correct_product:
   print("Correct Answer!!")
else:
      print(f"Wrong Answer!! The correct answer is {correct_product}.")

"""**Squares of Even/Odd Numbers**"""

for num in range (100,201,2):
  square= num**2
  print(f"Square of {num} is {square}")

"""**Choice:** Even Numbers are chosen becoz they are divisible by 2 and can be efficiently iterated over using a step of 2.

**Word counter**
"""

input_text="This is a sample text. This text will be used to demonstrate the word counter."
words=input_text.split()
word_count={}
for word in words:
  word_count[word]=word_count.get(word,0)+1
for word, count in word_count.items():
  print(f"{word}: {count}")

"""**Check for Palindrome**"""

def check_palindrome(string):
  cleaned=''.join(char.lower() for char in string if char.isalnum())
  return cleaned==cleaned[::-1]
input_string=input("Enter a string: ")
print(check_palindrome(input_string))
