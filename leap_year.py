year = int(input("Which year do you want to check? "))
           
f = year/4
print("{:.2f}".format(f))

h = year/100
print("{:.2f}".format(h))

fh =year/400
print("{:.2f}".format(fh))
  
if  f % 2 == 0 :
    print("it is a leap year")
  
elif  h % 2 ==0 :
    print("it is not a leap year")
    
elif  fh % 2 == 0 :
    print("it is a leap year")
      
else :
    print("it is not a leap year")
       
