from math import sqrt
print ("Welcome to Pythagoras calculator...")
Side = input("What side would u like to calculate? (a, b or c): ")

if Side == "a":
  side_b = int(input("What is the measurement of side b? "))
  side_c = int(input("What is the measurement of side c? "))
  side_a_ans = sqrt(side_c * side_c - side_b * side_b)
  print (f"The answer is {side_a_ans}")
  
elif Side == "b":
  side_c = int(input("What is the measurement of side c? "))
  side_a = int(input("What is the measurement of side a? "))
  side_b_ans = sqrt(side_c * side_c - side_a * side_a)
  print (f"The answer is {side_b_ans}")
  
elif Side == "c":
  side_a = int(input("What is the measurement of side a? "))
  side_b = int(input("What is the measurement of side b? "))
  side_c_ans = sqrt(side_a * side_a + side_b * side_b)
  print (f"The answer is {side_c_ans}")
  
else:
  print ("You must enter in lowercase from the following options (a,b,c)")
  
  
  
  
  
  
  
  
  
  
 
  
  
 
  
