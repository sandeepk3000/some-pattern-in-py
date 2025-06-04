for i in range(1, 7):
  for j in range(1, 7):
    if (i == 1 or i == 6):
      print("*", end=" ")
    else:
      if j == 1 or j == 6:
        print("*", end=" ")
      else:
        print(" ", end=" ")
  print()

# number triangular
for i in range(1, 5):
  for j in range(4,0,-1):
    if j - i <= 0 :
      print(f" {i} " , end=" ")
    else:
      print(" ", end=" ")  
  print()
      