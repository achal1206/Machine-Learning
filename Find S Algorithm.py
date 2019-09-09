#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
a=[]
with open('/home/cmruuser/Documents/ex.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes=len(a[0])-1
print("The most general hypothesis:",["?"]*num_attributes)
print("The most specific hypothesis:",["0"]*num_attributes)
hypothesis=a[0][:-1]
print("\n Find S: Finding a maximally specific hypothesis")
for i in range (len(a)):
    if a[i][num_attributes] == "1":
        for j in range(num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
    print("The taining example no:",i+1," the hyposthesis is:",hypothesis)
print("\n The maximally specific hypohthesis for training set is")
print(hypothesis)


# In[ ]:




