#!/usr/bin/env python
# coding: utf-8

# Practical 1: It will take position value from user until both the seqyence have have equal number of value

# In[23]:


set1=list(input("Enter the 1st Sequence-->  "))
set2=list(input("Enter the 2nd Sequence-->  "))
score=[]
def Pairwise_alignment(a,b):
    gap(a,b)
    print(a)
    print(b)
    value=0
    length=len(a)
    for i in range(0, length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    print(score)
    print(value)
    
def gap(a,b):
    while len(a)!=len(b):
        if(len(a)==len(b)):
            print()
        else:
            k=int(input('Enter the position to insert-->  '))
            if(len(a)>len(b)):
                b.insert(k,'-')
            else:
                a.insert(k,'-')    
    return(a,b)
Pairwise_alignment(set1,set2)


# Practical 2: 

# In[22]:


set1=list(input("Enter the 1st Sequence-->  "))
set2=list(input("Enter the 2nd Sequence-->  "))
def find_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score=0
    length=len(a)
    total_element=len(a)*len(b)
    for i in range(0, length):
        for j in range (0, length):
            if(a[i]==b[j]):
                score=score+1
    identity=(score/total_element)*100
    print('Matching Score--> ',score)
    print('Identity of the sequence--> ',identity)
    
def gap(a,b):
    while len(a)!=len(b):
        if(len(a)==len(b)):
            print()
        else:
            k=int(input('Enter the position to insert-->  '))
            if(len(a)>len(b)):
                b.insert(k,'-')
            else:
                a.insert(k,'-')    
    return(a,b)
find_identity(set1,set2)


# Practical 3:

# In[ ]:


set1=input("Enter the 1st Sequence-->  ")
set2=input("Enter the 2nd Sequence-->  ")
similarity_calculation=int(input('Type the no. of element for similarity calculation-->  '))
similarities=[]
for i in range(0,similarity_calculation):
    element=input('Enter an Element-->  ')
    similar_element=int(input('No. of element it is similar-->  '))
    similarities.append([])
    similarities[i].append(element)

    for j in range(0,similar_element):
        b=input('What is it similar to-->  ')
        similarities[i].append(b)
        
def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score=score+1
    similarity=(score*100)/len(o)
    return similarity

print(compare(list(set1),list(set2),similarities),'%')


# In[ ]:




