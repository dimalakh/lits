def flatten(lst):
     for x in lst:
         if isinstance(x, list):
             for x in flatten(x):
                 yield x
         else:
             yield x
 
 
lst = [1, [2, 3], 4, [[6, 7]]]
print list(flatten(lst)) 