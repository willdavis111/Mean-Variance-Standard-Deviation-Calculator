import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  npArray = np.array(list, dtype=float)
  matrix = npArray.reshape(3, 3)
  meanM = matrix.mean()
  varM = matrix.var()
  stdM = matrix.std()
  maxM = matrix.max()
  minM = matrix.min()
  sumM = matrix.sum()

  mean1 = matrix.mean(axis=0).tolist()
  var1 = matrix.var(axis=0).tolist()
  std1 = matrix.std(axis=0).tolist()
  max1 = matrix.max(axis=0).tolist()
  min1 = matrix.min(axis=0).tolist()
  sum1 = matrix.sum(axis=0).tolist()

  mean2 = matrix.mean(axis=1).tolist()
  var2 = matrix.var(axis=1).tolist()
  std2 = matrix.std(axis=1).tolist()
  max2 = matrix.max(axis=1).tolist()
  min2 = matrix.min(axis=1).tolist()
  sum2 = matrix.sum(axis=1).tolist()

  calulations = {
  'mean': [mean1, mean2, meanM],
  'variance': [var1, var2, varM],
  'standard deviation': [std1, std2, stdM],
  'max': [max1,max2, maxM],
  'min': [min1,min2, minM],
  'sum': [sum1,sum2, sumM]
    }



  print(calulations)
  return calulations



list1 = [0,1,2,3,4,5,6,7,8]
calculate(list1)
