class coffee:
    def __init__(self,water,milk,coffee,money):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.money=money
        
    def display_ini(self):
        print("\n*****The report of the coffee machine *****")
        print("\n Current resource values are :")
        print(" ----WATER = ",self.water,"ML\n",
              "----MILK  = ",self.milk,"ML\n",
              "----COFFEE  = ",self.coffee,"ML\n",
              "----MONEY = $",self.money)
        
    def cof_val(self):
        self.cof_w=int(input("\nEnter The Amount of Water You Want To Add In Your Drink(in ml) : "))
        self.cof_m=int(input("\nEnter The Amount of Milk You Want To Add In Your Drink(in ml) : "))
        self.cof_c=int(input("\nEnter The Amount of Coffee You Want To Add In Your Drink(in ml) : "))

        if(self.cof_w > self.water):
            print("Sorry there is not enough water resource ")
        if(self.cof_m > self.milk):
            print("Sorry there is not enough milk resource ")
        if(self.cof_c > self.coffee):
            print("Sorry there is not enough coffee resource ")

    def set(self):
        self.check=0
        if(self.cof_w > self.water or self.cof_m > self.milk or self.cof_c > self.coffee):
            self.check=1
            
        

    def mon_val(self):

        print("\n ***** THE COST OF YOUR COFFEE IS  $10 *****") 
        print("\n ENTER THE SUFFICIENT MONEY TO GET YOUR DRINK ")
        print("\n The acceptable money notations are : \nquarter ($0.25)\ndimes (0.10)\nnickles ($0.05)\npennies ($0.01)")
        qu=int(input("\nEnter the money in  terms of quarter....(for example, if you have 4 coins of quarter ....enter 4) : "))
        di=int(input("\nEnter the money in  terms of dimes (IF ENTERED SUFFICIENT AMOUNT PLEASE ENTER 0): "))
        ni=int(input("\nEnter the money in  terms of nickles (IF ENTERED SUFFICIENT AMOUNT PLEASE ENTER 0): "))
        pe=int(input("\nEnter the money in  terms of pennies (IF ENTERED SUFFICIENT AMOUNT PLEASE ENTER 0): "))
        tot=(0.25*qu)+(0.10*di)+(0.05*ni)+(0.01*pe) 

        if( tot == 5):
            self.money = self.money+10
            if(self.cof_w <= self.water and self.cof_m <= self.milk and self.cof_c <= self.coffee):
                self.water=self.water - self.cof_w
                self.milk=self.milk - self.cof_m
                self.coffee=self.coffee - self.cof_c
            self.tran="success"
            
        elif(tot < 5):
            print("\nSorry that's not enough money...Please try it again")
            self.tran="failure"

        elif(tot > 5):
            print("\n Here is your change: "+"{:.2f}".format(tot-5),"$")
            self.money=self.money+10
            if(self.cof_w <= self.water and self.cof_m <= self.milk and self.cof_c <= self.coffee):
                self.water=self.water - self.cof_w
                self.milk=self.milk - self.cof_m
                self.coffee=self.coffee - self.cof_c
            self.tran="success"


    def chec(self):
        self.msg="no load"
        if(self.water <=50 or self.milk <= 50 or self.coffee <= 50):
            self.msg="reload the machine"
            self.water=self.water+500
            self.milk=self.milk+500
            self.coffee=self.coffee+500
                               

C = coffee(500,500,500,100)



run=100

print("\nThe Machine Will Serve The Customers for 100 times")

machine=input("\nStatus of the coffee machine (on/off): ")

while(run>=1):
    while(machine.lower()=='on'):
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("\n***ENTER 1 FOR ESPRESSO \n***ENTER 2 FOR LATTE \n***ENTER 3 FOR CAPPUCCINO")
        cof_choi=int(input("\n ENTER YOUR CHOICE OF COFFEE : "))
        C.display_ini()

        if(cof_choi==1):
            C.cof_val()
            C.set()
            if(C.check==1):
                print("Please enter again")
            else:
                C.mon_val()
                if(C.tran=="success"):
                    print("\n Here is your ESPRESSO. ENJOY!!!!! ")

        elif(cof_choi==2):
            C.cof_val()
            C.set()
            if(C.check==1):
                print("Please enter again")
            else:
                C.mon_val()
                if(C.tran=="success"):
                    print("\n Here is your LATTE. ENJOY!!!!! ")

        elif(cof_choi==3):
            C.cof_val()
            C.set()
            if(C.check==1):
                print("Please enter again")
            else:
                C.mon_val()
                if(C.tran=="success"):
                    print("\n Here is your CAPPUCCINO. ENJOY!!!!! ")

        elif(cof_choi>3 or cof_choi==0):
            print("\n:(  You have choosed wrong choice of coffee....Please try it again  :(")

        C.chec()
        if(C.msg=="reload the machine"):
            print("\nONE OF THE RESOURCE IS VERY MUCH LOW IN MACHINE")
            print( "\nSO THE MACHINE RELOADING ")
            print("\nTHE MACHINE RELOADED SUCCESSFULLY")

        run=run-1
        if(run==0):
            print("\nTHE MACHINE IS UNDER MAINTENANCE \n THE MACHINE IS ENJOYING HIS OWN COFFEE")
            machine="off"

if(machine.lower()=="off"):
    print("\nPLEASE TURN ON THE MACHINE TO START THE SERVICE")
