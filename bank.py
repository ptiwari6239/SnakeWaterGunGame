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
     print(file.read())
     file.close()

    except Exception:

        print(" Invalid Account Number ")

def newaccount():
    
    
     while True:
       try:  
         choice=input('   Press (Y/N) To Continue Making Account Or To Exit  ').upper()

         if choice=='Y':
            ac_no=input('  Select Your Account Number ')
     
            try:

             file = open(ac_no,'r')                                           # check if account already exit or not with given account number
             file.close()
             print("Account Number Already Exit , Please Try Something Else ")

            except Exception:                                                   # Account does'nt exit  then make a new account/file  with given account number
             Name=input("Name ")
             Age=input('Age ')
             Amount=input('Amount ')
             user=Customer(Name,Age,Amount,ac_no)
         elif choice=="N":
             print('         Thank   You      For    Baking     With    Us   ')
             exit()
         else:print('  INVALID  ENTRY ')
       except Exception:
           print(" Invalid  Entry ")     
    

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
        
        u=int(input(  " Press  1  To  Create   Account,  2  To  View   Details,  3  To  Remove   Account,  4  To  Deposite    Money,  5  To   Withdraw  and  6  to  exit :-  "))

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
           print("  No  Entry ")     


print("             WELCOME     TO    OUR     BANK   ")
option()    
 




     
