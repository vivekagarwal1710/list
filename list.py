 
list1 = [-5,48,33,-44,48,-483]  

list2= list(filter(lambda x: (x >= 0), list1)) 
  
print("Positive numbers in the list:\n", list2)  
