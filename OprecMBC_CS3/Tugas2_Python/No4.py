n = int(input("Masukkan angka yang mau dibentuk : "))
t = n
for i in range(n): 
  for j in range(t):
      if i ==0 or i == (n-1) or j == 0 or j == (t-1): 
        print("*",end ='')
      else :
        print("#",end='')
  print()