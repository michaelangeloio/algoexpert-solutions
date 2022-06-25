def twoNumberSum(array, targetSum):
  i = 0
  validIndexList = []
  while i < len(array):
      for index, num in enumerate(array):
          if i != index:
              if array[i] + num == targetSum and i not in validIndexList:
                      validIndexList += [num]
      i +=1
  return validIndexList
    