from abc import ABC
class user:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        

class Admin (user):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)
        
    def add_employee(self,Restaurant,employee):
        Restaurant.add_employee(employee)
        
    def view_employee(self,Restaurant):
        Restaurant.view_employee()
    
    def add_item(self,Restaurant,item):
        Restaurant.mn.add_item(item)
    def remove_item(self,Restaurant,item):
        Restaurant.mn.remove_item(item)
        
    def show_menu(self,Restaurant):
        Restaurant.mn.show_menu()
    
    
class Employees(user):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary
    
    
    
class Customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=order()
    def add_cart(self,restaurant,item_name,quantity):
        if restaurant.mn.find_item(item_name)!=None:
            z=restaurant.mn.find_item(item_name)
            if quantity<=z.quantity:
                z.quantity=quantity
                self.cart.add_to_cart(z)
            else:
                print(f'Not available in stocks')
        else:
            print("Not available in the menu.")
    def view_menu(self,restaurant):
        restaurant.mn.show_menu()
    def remove_cart(self,item_name,quantity):
        if item_name in self.cart.ordr:
            self.cart.remove_from_cart(item_name,quantity)
        else:
            print(f'Item not in cart.')
    def pay_price(self):
        print(f'Total Bill was {self.cart.ttl_prc()} Taka. It was paid Successfully.')
        self.cart.clear_cart()
    def view_cart(self):
        self.cart.view_cart()
class restaurant:
    def __init__(self,name):
        self.name=name
        self.employee=[]
        self.mn=menu()
    
    def add_employee(self,employee):
        self.employee.append(employee)
        
    def view_employee(self):
        print("The list of employees is given below: ")
        for i in self.employee:
            print(f'{i.name}\t{i.email}\t{i.phone}\t{i.address}')
            
            
            
class menu:
    def __init__ (self):
        self.itm=[]
        
    def add_item(self,item):
        self.itm.append(item)
        
    def find_item(self,item):
        for i in self.itm:
            if item.lower()==i.name.lower():
                return i
        else:
            return None
        
    def remove_item(self,item):
        z=self.find_item(item)
        if z!=None:
            self.itm.remove(z)
            print("Item deleted.")
        else:
            print("Item not found!")
            
    def show_menu(self):
        print("*****Menu*****")
        print(f'Item Name\tItem Price\tQuantity')
        for i in self.itm:
            print(f'{i.name}\t{i.price}\t{i.quantity}')
class Fooditem:
    def __init__(self,name,quantity,price):
        self.name=name
        self.price=price
        self.quantity=quantity

class order:
    def __init__(self):
        self.ordr={}
    def add_to_cart(self,item_name):
            if item_name in self.ordr:
                self.ordr[item_name]+= item_name.quantity
                
            else:
                self.ordr[item_name]=item_name.quantity
                
        
    def remove_from_cart(self,item_name,quantity):
            if self.ordr[item_name]==quantity:
                del self.ordr[item_name]
            else:
                self.order-=quantity
        
    def ttl_prc(self):
        total_price=0
        for k,v in self.ordr.items():
            total_price+= v * k.price 
        return total_price
    def clear_cart(self):
        self.ordr={}
        
    def view_cart(self):
        print("Item Names\tQuantity")
        for k,v in self.ordr.items():
            print(f'{k.name}\t{v}')
naam=restaurant("Hotel Italy")
def Customer_interface():
    name=input("Enter your name: ")
    phone=input("Enter your phone number: ")
    email=input("Enter your email address: ")
    address=input("Enter your address: ")
    cust=Customer(name,phone,email,address)
    
    while True:
        print(f"Welcome {cust.name} to our restaurant!!!!")
        print("1. View Menu ")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")
        usr_inp=int(input(("Enter your choice: ")))
        if usr_inp==1:
            cust.view_menu(naam)
        elif usr_inp==2:
            item_name=input("Enter the name of the item: ")
            quantity=int(input("Enter how much do you want: "))
            cust.add_cart(naam,item_name,quantity)
        elif usr_inp==3:
            print(f'{cust.name} here is your cart: ')
            cust.view_cart()
        elif usr_inp==4:
            cust.pay_price()
        elif usr_inp==5:
            break
        else:
            print("Wrong input given. Please try again ;)")
    


def admin_interface():
    name=input("Enter your name: ")
    phone=input("Enter your phone number: ")
    email=input("Enter your email address: ")
    address=input("Enter your address: ")
    adm=Admin(name,phone,email,address)
    
    while True:
        print(f"Welcome {adm.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")
        usr_inp=int(input(("Enter your choice: ")))
        if usr_inp==1:
            ite_name=input("Enter the name of the item: ")
            item_quantity=int(input("Enter the number of quantity: "))
            item_price=float(input("Enter the price of the item: "))
            notun=Fooditem(ite_name,item_quantity,item_price)
            adm.add_item(naam,notun)
        elif usr_inp==2:
            nme=input("Enter your name: ")
            pone=input("Enter your phone number: ")
            eail=input("Enter your email address")
            adress=input("Enter your address: ")
            age=int(input("Enter your age: "))
            desig=input("Enter your designation: ")
            salary=float(input("Enter your salary: "))
            kormi=Employees(nme,pone,eail,adress,age,desig,salary)
            adm.add_employee(naam,kormi)
        elif usr_inp==3:
            adm.view_employee(naam)
        elif usr_inp==4:
            adm.show_menu(naam)
        elif usr_inp==5:
            itm=input("Enter the name of the item: ")
            qnt=int(input("Enter the quantity to be reomved: "))
            adm.remove_item(itm)
        elif usr_inp==6:
            break
        else:
            print("Wrong input given. Please try again ;)")
            
            


while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        Customer_interface()
    elif choice == 2:
        admin_interface()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")

