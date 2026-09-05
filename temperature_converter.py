#temperature converter

while (True):
   print("1.celsius to fahrenheit")
   print("2.fahrenheit to celsius ")
   print("3.celsius to kelvin")
   print("4.kelvin to celsius")
   print("5.fahrenheit to kelvin")
   print("6.kelvin to fahrenheit")
   try:
      a=float(input("enter the temperature:"))
      choice=int(input("enter your choice:"))
   except:
      print("enter a valid number")
      continue
   

   if(choice==1):
      if(a>=-273.15):                                  
        print("celsius to fahrenheit")
        f=(9/5)*a +32
        print("temperature in fahrenheit=",f)
      else:
          print("cannot convert to fahrenheit")

   elif(choice==2):
      if(a>=-459.67):
          print("fahrenheit to celsius")
          c=(a-32)*(5/9)
          print("temperature in celsius=",c)
      else:
          print("cannot convert to celsius")

   elif(choice==3):
      if(a>=-273.15):
         print("celsius to kelvin")
         k=a+273.15
         print("temperature in kelvin=",k)
      else:
         print("cannot convert to kelvin")

   elif(choice==4):
      if(a>=0):
         print("kelvin to celsius")
         c=a-273.15
         print("temperature in celsius=",c)
      else:
         print("cannot convert to celsius") 

   elif(choice==5):
      if(a>=-459.67):
         print("fahrenheit to kelvin")
         k=(a-32)*5/9 +273.15
         print("temperature in kelvin=",k)
      else:
         print("cannot convert to kelvin")
      
   elif(choice==6):
      if(a>=0):
         print("kelvin to fahrenheit")
         f=(a-273.15)*9/5+32
         print("temperature in fahrenheit=",f)
      else:
            print("cannot convert to fahrenheit") 

   else:
       print("invalid choice")

   ans=input("do you want to continue? yes/no:")
   if( ans=="no"):
       print("loop exited")
       break
        


        
        





