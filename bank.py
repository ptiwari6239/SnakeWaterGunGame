import os 
import ast


class Customer:
    def __init__(self,name,age,amount,accountNo):
        self.Name=name
        self.Age=age
        self.Amount=amount
        self.ac_no=accountNo
    
        file=open(str(accountNo),'a')           # creating a file with account number 
        detail="{'name':" + f"'{self.Name}'" + ", 'age': " +str(self.Age)+ ", 'Amount': " + self.Amount + "}"
        file.write(detail)                    # closing the file 
        file.close()

def view():
    details=input("Enter Account Number:- ")

    try:

     file=open(details,'r')               # checking if account already exit or not 
     info=file.read()
     file.close()
     print('This is what we have found ')
     print("\n")
     print(info)
     print('\n')
     

    except Exception:

        print(" Invalid Account Number ")

def newaccount():
    
    
     while True:
       
         choice=input('Press (Y/N) To Continue Making Account Or To Exit  ').upper()
         try:

          if choice=='Y':
            ac_no=int(input('Select Your Account Number '))
     
            try:

             file = open(str(ac_no),'r')                                           # check if account already exit or not with given account number
             file.close()
             print("Account Number Already Exit , Please Try Something Else ")

            except Exception:                                                   # Account does'nt exit  then make a new account/file  with given account number
             Name=input("Name ")
             Age=input('Age ')
             Amount=input('Amount ')
             user=Customer(Name,Age,Amount,str(ac_no))
          elif choice=="N":
             option()
            #  print('         Thank   You      For    Baking     With    Us   ')
             
          else:print('  INVALID  ENTRY ')
         except Exception:
             print("Something is wrong please try again")    
    

def remove():
    r=input("Enter Account Number To Remove ")
    try:

        os.remove(r)
        print(" YOUR ACCOUNT IS REMOVED SUCCESFULLY")
    except Exception:

        print(" Invalid  Account  Number ")
def deposite():
    acc_no=input(" Enter Your Account Number ")
    depo =int(input(" Enter  The   Amount "))
    try:                                        # deposite money only when account already exits !!
     file=open(str(acc_no),'r')
     info=file.read()  
     res=ast.literal_eval(info)                  # convert string to dictionary 
     a=int(res['Amount'])                         # fetch the value of amount 
     res['Amount']=(a+depo)
     file.close()
     file=open(str(acc_no),'w')
     file.write(str(res))   
     file.close()
    
     
    except Exception:
        print("  Invalid   Account   Number  ")         
def Withdraw():
    acc_no=input("Enter Your Account Number ")
    draw =int(input("Enter The Amount  "))
    try:
     file=open(str(acc_no),'r')
     info=file.read()  
     res=ast.literal_eval(info)
     ORI_AMO=int(res['Amount'])
     if ORI_AMO<draw:
         print("  NOT  ENOUGH  FUND :( ")
     else:    
      res['Amount']=(ORI_AMO-draw)
      file.close()
      file=open(str(acc_no),'w')
      file.write(str(res))   
      file.close()
    
     
    except Exception:
        print("  Invalid   Account   Number  ")

def option():

    while True:
      try:
        print("Press 1 to create new account     Press 2 to view details")
        print('Press 3 to remove account         press 4 to deposite ')
        print("Press 5 to withdraw               Press 6 to exit")
        
        
        u=int(input())

        if u==1:
          newaccount()
        elif u==2:
           view()
        elif u==6:
            print("Thank you for banking with us ")
            exit()
        elif u==3:
            remove()  
        elif u==4:
            deposite()   
        elif u==5:
            Withdraw()       
        else:print(' Invalid  Entry ')
      except Exception:
           print("  Wrong  Entry ")     


print("             WELCOME     TO    OUR     BANK   ")
option()
