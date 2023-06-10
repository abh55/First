#!/usr/bin/env python
# coding: utf-8

# # LOOP STATEMENTS

# In[10]:


#1. WAP to print all elements of a list using a for loop. Take the elements of the list from the user.

li = []
n = int(input("Enter length of the list: "))
for i in range(n):
    a = input("Enter element: ")
    li.append(a)
for j in range(n):
    print(li[j])


# In[18]:


#2. WAP to take inputs from user to make a list. Length of the list has to be taken from the user.
#   Again take one input from user and search it in the list and delete that element, if found.
#   If not found, print "Element not present".
li = []
n = int(input("Enter length of the list: "))
for i in range(n):
    a = input("Enter element: ")
    li.append(a)
element = input("Enter element to be deleted: ")
c = 0
i = 0
length = len(li)
while(i<n):
    if(element in li):
        li.remove(element)
        c = 1
    i = i + 1
if (c==0):
    print("Element not present")
else:
    print(li)


# In[23]:


#3. Make a grading system for a school based on the marks of the students using the following criteria.
# Marks 0 - 40 : Grade F
#      41 - 50 : Grade E
#      51 - 70 : Grade D
#      71 - 80 : Grade C
#      81 - 90 : Grade B
#      91 - 100: Grade A
# Continuously take marks as input from the user and print the grade. 
# The user can enter "Stop" to stop the loop.

i = 0
while(i == 0):
    marks = input("Enter marks: ")
    if(marks == "Stop"):break
    else:
        marks = int(marks)
        if(marks<=40):print("Grade F")
        elif(marks>=41 and marks<=50):print("Grade E")
        elif(marks>=51 and marks<=70):print("Grade D")
        elif(marks>=71 and marks<=80):print("Grade C")
        elif(marks>=81 and marks<=90):print("Grade B")
        elif(marks>=91 and marks<=100):print("Grade A")


# In[27]:


#4. WAP to save the cube of all numbers from 1 to a number n in list, where n is taken as input from the user.

n = int(input("Enter the last number: "))
li = []
for i in range(n):
    li.append((i+1)*(i+1)*(i+1))
print(li)


# In[27]:


#5. WAP to print even numbers in a given range in reverse order. Take the range from the user.

start = int(input("Enter Start: "))
end = int(input("Enter End: "))
li = []
for i in range(start,end+1):
    if(i%2 == 0):
        li.append(i)
c = len(li) - 1
for i in range(c+1):
    print(li[c], end = " ")
    c = c - 1


# In[28]:


#6. WAP to print odd numbers in a given range in reverse order. Take the range from the user.

start = int(input("Enter Start: "))
end = int(input("Enter End: "))
li = []
for i in range(start,end+1):
    if(i%2 != 0):
        li.append(i)
c = len(li) - 1
for i in range(c+1):
    print(li[c], end = " ")
    c = c - 1


# In[30]:


#7. WAP to print multiplication table of a number taken as input from the user.

n = int(input("Enter number: "))
for i in range(1,11):
    p = n*i
    print(f"{n} * {i} = {p}")


# In[34]:


#8. WAP to print the following pattern.

n = int(input("Enter range: "))
for i in range(1,n+1):
    for j in range(i):
        print(j+1, end = "")
    print()


# In[46]:


#9. Write a program to calculate the sum of series up to n terms for a digit d. n & d are taken as input from the user.

d = input("Enter digit: ")
n = int(input("Enter iterations: "))
s = 0
for i in range(1,n+1):
    s = s + int(d*i)
print(s)\












# In[40]:


#10. WAP that keeps on accepting numbers from the user until the user enters Zero(0) as input. Display the sum and average of all the numbers.

s = 0
c = 0
while(i == 0):
    n = int(input("Enter a Number: "))
    if(n == 0):break
    else:
        s = s + n
        c = c + 1
print("Sum = ",s)
print("Average = ",(s/c))


# In[41]:


#11. Accept n numbers from the user and display their average. n is input from the user.

n = int(input("Enter range: "))
c = 0
s = 0
for i in range(n):
    num = int(input("Enter number: "))
    s = s+num
    c = c+1
print("Average = ",(s/c))


# ## String Questions

# In[21]:


#1. Write a Python program to count the number of each of the characters (character frequency) in a string input by the user. Ignore the case.

s = input("Enter String: ")
s = s.upper()
l = []
for i in s:
    if i in l:
        pass
    else:
        if i != " ":
            print(i,"=",s1.count(i),end = ' ')
            l.append(i)


# In[25]:


#2. Write a Python program to find the digits which are absent in a given mobile number.

number = input("Enter mobile number: ")
if(len(number) == 10):
    for i in range(10):
        i = str(i)
        if i not in number:
            print(i, end = " ")
else:
    print("Enter a valid mobile number")


# In[1]:


#3. WAP in python to find average of n numbers taken as input from the user in realtime.

n = int(input("Enter range: "))
s = 0
for i in range(n):
    num = int(input("Enter number: "))
    s = s + num
avg = s/n
print("Average: ", avg)    


# In[6]:


#4. WAP in python that accepts a hyphen-separated sequence of alphabets as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

string = input("Enter hyphen-separated word: ")
list1 = string.split('-')
list1 = sorted(list1)
print(list1)


# In[ ]:





# In[ ]:




