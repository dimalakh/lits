
str = '((((((((((((((2, 3)))))))))))))'

str1 = '((((((((((((((2, 3)))))))))))})'

str2 = '(([{((}(((((((((2, 3)))))))))))))'

str3 = '({}[])'

def parenthes(str):
  storage = []
  openP = "({[" 
  closeP =  ")}]"
  for c in str :
    if c in openP :
      storage.append(c)
    elif c in closeP :
      if not len(storage) :
        return False
      else :
        storageP = storage.pop()
        balancingParenthes = openP[closeP.index(c)]
        if storageP != balancingParenthes :
          return False
    else :
      return False
  return not len(storage)

print(parenthes(str3))