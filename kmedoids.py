import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def get_medoids(df):
  idx = [randint(0, len(df)-1) for i in range(2)]
  medoids = [[df.loc[i,'x'], df.loc[i,'y']] for i in idx]
  return medoids

def createDMatrix(df, medoids):
  for medoid in medoids:
    idx = medoids.index(medoid)
    dissimilarity_matrix = []
    for i in range(len(df)):
      x = abs(df.iloc[i,0] - medoid[0])
      y = abs(df.iloc[i,1] - medoid[1])
      dissimilarity_matrix.append(x+y)
    df['Dissimilarity C'+str(idx)] = dissimilarity_matrix
  return df

def buildClusters(df):
  clusters = dict()
  total_cost = 0
  for i in range(len(df)):
    cost = min(df.iloc[i,2], df.iloc[i,3])
    idx = 1 if(df.iloc[i,2]<df.iloc[i,3]) else 2
    total_cost += cost
    if(idx in clusters):
      clusters[idx].append([[df.iloc[i,0], df.iloc[i,1]]])
    else:
      clusters[idx] = [[df.iloc[i,0], df.iloc[i,1]]]
  return clusters, total_cost

def get_new_medoids(medoids, df):
  new_medoids = medoids
  while True:
    med_idx = randint(0, len(medoids)-1)
    new_med_idx = randint(0, len(df)-1)
    if(medoids[med_idx]!=df.iloc[new_med_idx, [0,1]].tolist()):
      new_medoids[med_idx] = df.iloc[new_med_idx, [0,1]].tolist()
      break
  return new_medoids

def get_new_cost(df, medoids, cost):
  flag = False
  new_medoids = get_new_medoids(medoids, df)
  new_df = createDMatrix(df, new_medoids)
  new_clusters, new_cost = buildClusters(new_df)

  if(new_cost<=cost):
    flag = True    
  else:
    flag = False

  return new_medoids, new_clusters, new_df, new_cost, flag

#implementation

df = pd.read_csv('data.csv')
print(df.head())

medoids = get_medoids(df)
df = createDMatrix(df, medoids)
clusters, total_cost = buildClusters(df)
print('Medoids:', medoids)
print('DataFrame:\n', df.head())
print('Clusters:', clusters)
print('Cost:', total_cost)

flag = True
while(flag!=False):
  new_medoids = get_new_medoids(medoids, df)
  new_medoids, new_clusters, new_df, new_cost, flag = get_new_cost(df, medoids, total_cost)
  print('New Medoids:', new_medoids)
  print('New Cost:', new_cost)

  if flag==False:
    print('Costly')
    break
  else:
    medoids = new_medoids
    clusters = new_clusters
    df = new_df
    total_cost = new_cost
  print('Medoids:', medoids)
  print('DataFrame:', df.head())
  print('Clusters:', clusters)
  print('Cost:', total_cost)