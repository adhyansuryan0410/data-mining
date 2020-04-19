import pandas as pd
import numpy as np
import itertools

min_sup = 4
min_conf = 0.6

data = pd.read_csv('GroceryStoreDataSet.csv')
print('Data Overview')
print(data.head())
print('\n----------------------------------------------------------------------------------------------------\n')

l = len(data['items'])
ck1 = dict()
l1 = dict()
for i in data['items']:
    item = list(i.split(','))
    for j in item:
      if(j not in ck1):
        ck1[j]=1
      else:
        ck1[j]+=1
print('MIN_SUP = 3 \n')
print('CK1')
for i in ck1:
  print(i, ck1[i])
print('\n----------------------------------------------------------------------------------------------------\n')
for candidate in ck1:
  if ck1[candidate]>=min_sup:
    l1[candidate]=ck1[candidate]
print('L1')
for i in l1:
  print(i, l1[i])
print('\n----------------------------------------------------------------------------------------------------\n')

temp_list = list(itertools.combinations(l1,2))
#print(temp_list)
ck2 = dict()
l2 = dict()
for i in temp_list:
  for j in data['items']:
    if i[0] in j and i[1] in j:
      if i not in ck2:
        ck2[i] = 1
      else:
        ck2[i]+=1
print('CK2')
for i in ck2:
  print(i, ck2[i])
print('\n----------------------------------------------------------------------------------------------------\n')
for candidate in ck2:
  if ck2[candidate]>=min_sup:
    l2[candidate]=ck2[candidate]
print('L2')
for i in l2:
  print(i, l2[i])
print('\n----------------------------------------------------------------------------------------------------\n')

temp_list = list(itertools.combinations(l1,3))
#print(temp_list)
ck3 = dict()
l3 = dict()
for i in temp_list:
  for j in data['items']:
    if i[0] in j and i[1] in j and i[2] in j:
      if i not in ck3:
        ck3[i] = 1
      else:
        ck3[i]+=1
print('CK3')
for i in ck3:
  print(i, ck3[i])
print('\n----------------------------------------------------------------------------------------------------\n')
for candidate in ck3:
  if ck3[candidate]>=min_sup:
    l3[candidate]=ck3[candidate]
print('L3')
for i in l3:
  print(i, l3[i])
print('\n----------------------------------------------------------------------------------------------------\n')

print('FREQUENT ITEMSETS')
fq_items = l2
for i in fq_items:
  print(i)
print('\n----------------------------------------------------------------------------------------------------\n')

print('ASSOCIATION RULES')
for i in fq_items:
  conf = l2[i]/l1[i[0]]
  if conf>=min_conf:
    print(i[0],'-->',i[1],'\t',conf*100,'%')

