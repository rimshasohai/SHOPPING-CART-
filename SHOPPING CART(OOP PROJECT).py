####ABSTRACT CLASS
##from abc import ABC, abstractmethod
##class Filing(ABC):
##    @abstractmethod
##    def saveToFile(self):
##        pass
##
####FOR THE CUSTOMER WHICH IS BASICALLY A USER
##class User(Filing):
##    account_holder_list=[ ]
##    def __init__(self):
##        self.d={ }
##
##        
####CREATE AN ACCOUNT FOR USER    
##    def userinfo(self):
##        print('*****CREATE  ACCOUNT*******')
##        self.username=input('ENTER THE USERNAME:')
##        self.password=input('ENTER THE PASSWORD:')
##        self.email=input('ENTER EMAIL:')
##        self.first_name=input('ENTER YOUR FIRST NAME:')
##        self.last_name=input('ENTER YOUR LAST NAME:')
##        self.name=self.first_name+self.last_name
##        self.address=input('ENTER YOUR ADDRESS:')
##        self.d.update({'USERNAME':self.username,'PASSWORD':self.password,'EMAIL':self.email,'FIRST NAME':self.first_name,'LAST NAME':self.last_name,'NAME:':self.name,'ADDRESS':self.address})
##        User.account_holder_list.append(self.name)
##        return self.d
##
####HOLDING NAME OF THE USERS
##    def accountholders(self,fileName):
##        de=open(fileName,'w')
##        for e in  User.account_holder_list:
##            de.write(e+'\n')
##        de.close()
##
####SAVING DATA INTO FILE
##    def  saveToFile(self,fileName):
##        g=open(fileName,'w')
##        for info in self.d:
##            g.write(info+':'+self.d[info]+'\n')
##        g.close()
##
##    
####READING SAVED INFORMATION FROM FILE
##    def readFromFile(self,fileName):
##             q=open(fileName,'r')
##             for line in q:
##                 mos=q.readlines()
##             return((mos))
##
##
##
##            
##
##
####CLASS STORING JUST PRODUCTS PRICE AND INHERITING FROM CLASS FILING
##class Product(Filing):
##    prod = {'BUBBLEGUM': 10, 'BISCUITS': 30, 'CHIPS': 20, 'TEA': 20, 'TOFFEES': 5, 'MANGOES': 100, 'APPLES': 200,
##            'PENCILS': 20, 'ERASER': 10, 'GRAPES': 200}
##    rod={'bubblegum': 10, 'biscuits': 30, 'chips': 20, 'tea': 20, 'toffees': 5, 'mangoes': 100, 'apples': 200,
##            'pencils': 20, 'eraser': 10, 'grapes': 200}
##
##
####SHOWING PRICES OF PRODUCTS TO THE USERS
##    def showingproducts(self):
##        print('***********PRODUCTS PRICE LIST*****************')
##        for item in Product.prod:
##            print(item +':'+ str(Product.prod[item]))
##            
####SAVING PRODUCTS PRICES TO FILE
##    def saveToFile(self, fileName):
##        f = open(fileName, 'w')
##        for item in Product.prod:
##            f.write(item + ':' + str(Product.prod[item]) + '\n')
##        f.close()
##
####CLASS IS FOR THE STOCK OF THE PRODUCTS AVAILABLE IN SHOP BASICALLY I MADE THIS CLASS SO THAT ONLINE WORKER CAN ADJUST
####STOCK BY CALLING THIS CLASS IF THEY DONT CALL THIS CLASS PREVIOUS STOCK CAN BE USED TO BE SHOWN AND FOR CALCULATION OF BILLS
####OF USER        
##class Product_in_stock:
##    def __init__(self):
##             self.products_quantity = {}
##             self.t= Product.prod
##             self.q_low=Product.rod
##             for tell in self.products_quantity:
##                 if  self.products_quantity[tell]<=0:
##                     pen=self.updatestock()
##                     self.updateproductsquantity(tell,pen)
##                     
####UPDATE STOCK IF THE  QUANTITY OF PRODUCTS IS LESS THAN 0,THEN THIS METHOD HAS BEEN CALLED INTO INITIATOR OF PRODUCT_IN_STOCK
##    def updatestock(self):
##         no=int(input('ENTER THE PRODUCTS:'))
##         return no
##         
####UPDATE THE QUANTITY OF PRODUCTS IN STOCK
##    def updateproductsquantity(self,product,quantity):
##        self.gon=self.products_quantity.update({product:quantity})
##        return self.gon
##    def stockinfo(self): 
##        print('***********STOCK INFORMATION********************')
##        try:
##            for item in self.t:
##                items = item
##                quantity = int(input('ENTER THE STOCK OF ' + ' ' + items.upper() + ':'))
##                self.updateproductsquantity(item,quantity)
##                for tell in self.products_quantity:
##                    if  self.products_quantity[tell]<=0:
##                        pen=self.updatestock()
##                        self.updateproductsquantity(tell,pen)
##
##            
##        except:
##                print('THE QUANTITY MUST BE A INTEGER NOT IN ALPHABETICAL FORM')
##
##            
####CLASS CART IS BASICALLY THE SHOPING CART OF USER.HERE WE ARE CALLING PRODUCT_IN_STOCK WITHIN CLASS CART AND INHERITING
####FROM USER AND FILING    
##class Cart(User,Filing):
##    def __init__(self):
##       self.call = Product_in_stock()
##       self.call.stockinfo()
##       self.l = { }##(DICT THAT THE STOCK OF QUANTITY THAT USER WANTS)
##       self.price = self.call.t##(THE PRICES OF THE STOCK)
##       self.quantity = self.call.products_quantity##(THE STOCK AVAILABLE IN THE MARKET)
##       for tel in self.quantity:
##           if  self.quantity[tel]<=0:
##               pen=self.updatestock()
##               self.updatequantity(tell,pen)
##       self.edge=self.call.q_low##(LIST CONTAINS SMALL LETTERS)
##       self.userfinalprices={ }##(DICT FOR THE ITEMS WITH PRICES)
##       self.userfinalquantity={ }##(DICT FOR THE ITEMS WITH QUANTITY)
##       
##     
##         
####METHOD FOR READING THE STOCK WHICH IS AVAILABLE IN ONLINE SHOP
##    def  readstock(self):
##        strg=' '
##        print('PRODUCTS:STOCK')
##        for item in self.quantity:
##            strg+=item+':'+str(self.quantity[item])+'\n'
##        return strg
##
####METHOD FOR SAVING STOCK INFORMATION INTO FILE
##    def saveFile(self, fileName):
##        f = open(fileName, 'w')
##        for item in self.quantity:
##            f.write(item + str(self.quantity[item]) + '\n')
##        f.close()
##
####METHOD FOR UPDATING THE STOCK THAT USER WANTS
##    def updatel(self,product,quantity):
##        self.l.update({product:quantity})
##
####METHOD FOR UPDATING THE QUANTITY OF PRODUCTS IN STOCK
##    def updatequantity(self,item,quantity):
##        self.quantity.update({item:quantity})
##        
####METHOD FOR UPDATING THE PRICES OF PRODUCTS WHICH USER HAS PURCHASED
##    def updatefinalprice(self,item,price):
##        k=self.userfinalprices.update({item:price})
##        return k
##
####METHOD FOR UPDATING THE QUANTITY OF PRODUCTS THAT USER WANTS
##    def updatefinalquantity(self,item,quantity):
##        joke=self.userfinalquantity.update({item:quantity})
##        return joke
##
####FUNCTION FOR ADDING ITEMS AND INPUT QUANTITIES OF PRODUCT FROM USER.
##    def additems(self):
##        while True:
##            choice = input('ENTER a or A TO CONTINUE OR ENTER q or Q TO EXIT:')
##            if choice == 'a' or choice == 'A':
##                product_need = input('ENTER PRODUCT NAME:')
##                for i in self.price:
##                    if product_need in self.price:
##                        if product_need not in self.l:
##                            print(product_need + ' ' + 'IS AVAILABLE')
##                            quantity=int(input('ENTER THE STOCK YOU NEED OF ' + ' ' + product_need + ':'))
##                            self.l.update({product_need:quantity})
##                            break
##                        if product_need in self.l:
##                            print(product_need + ' ' + 'IS AVAILABLE')
##                            quantity=int(input('ENTER THE STOCK YOU NEED OF ' + ' ' + product_need + ':'))+self.l[product_need]
##                            self.l.update({product_need:quantity})
##                            break
##                    if product_need in self.edge:
##                        if product_need.upper() in self.l:
##                            print(product_need + ' ' + 'IS AVAILABLE')
##                            quantity=int(input('ENTER THE STOCK YOU NEED OF ' + ' ' + product_need + ':'))+self.l[product_need.upper()]
##                            self.l.update({product_need.upper():quantity})
##                            break
##                            
##                        if product_need.upper() not in self.l:
##                            print(product_need.upper() + ' ' + 'IS AVAILABLE')
##                            quantity = int(input('ENTER THE STOCK YOU NEED OF ' + ' ' + product_need + ':'))
##                            self.l.update({product_need.upper(): quantity})
##                            break
##
##
##                    elif product_need not in self.price or i.lower() not in self.edge:
##                        print(product_need+' '+'IS NOT AVAILABLE')
##                        break
##
##            elif choice=='q' or choice=='Q':
##                break
####RETURN THE DICTIONARY OF THE PRODUCTS USER WANT
##        return (self.l)
##    
####METHOD FOR REMOVING ITEMS FROM CART
##    def removeitems(self):
##         try:
##            ite_m = input('ENTER ITEM TO REMOVE FROM CART:')
##            amount = int(input('ENETR QUANTITY OF ITEM YOU WANT TO REMOVE:'))
##            upper = ite_m.upper()
##            if self.l[upper] == amount:
##                del self.l[upper]
##            elif self.l[upper] > amount:
##                s = self.l[upper] - amount
##                self.updatel(upper,s)
##                return self.l
##                
##            
##            elif amount > self.l[upper]:
##                print('YOU HAVE ENTER GREATER NUMBERT OF ITEMS TO REMOVE BUT THERE IS LESSER ITEMS THAT IS ONLY',
##                      self.l[upper],'WE REMOVE ALL ITEMS NOW YOU HAVE LEFT WITH ZERO ITEMS')
##                del self.l[upper]
##
##
##         except KeyError:
##            print('THE ITEM YOU ENTER  IS NOT  IN YOUR CART THAT YOU WANT TO REMOVE IT AND TRY TO ENTER ITEM THAT IS IN YOUR CART')
##    
##
##
##
####METHOD FOR ADJUSTING QUANTITIES IN USER CART
##    def quantities(self):
##        for item in self.quantity:
##            if item in self.l:
##                user=self.l[item]
##                shop=self.quantity[item]
##                if user>shop:
##                    quil=shop
##                    self.updatefinalquantity(item,quil)
##                    for kimoo in self.price:
##                        if kimoo==item:
##                            item_p=self.price[item]
##                            ans=quil*item_p
##                            self.updatefinalprice(item,ans)
##                            shop=0
##                            self.updatequantity(item,shop)
##
##                            
##                if user<shop:
##                    shop-=user
##                    self.updatequantity(item,shop)
##                    ne=user
##
##                    for te in self.price:
##                        if te==item:
##                            ze=self.price[te]
##                            jem=ne*ze
##                            self.updatefinalprice(item,jem)
##                            self.updatefinalquantity(item,ne)
##                            
##                if user==shop:
##                    user=shop
##
##                    for ke in self.price:
##                        if ke==item:
##                            moo=self.price[ke]
##                            lek=moo*user
##                            self.updatefinalprice(item,lek)
##                            self.updatefinalquantity(item,user)
##                            shop = 0
##                            self.updatequantity(item,shop)
##
####METHOD FOR CALCULATING TOTAL
##    def total(self):
##        count=0
##        self.gym=self.userfinalprices
##        for i in self.gym:
##            count+=self.gym[i]
##        return count
##
####METHOD FOR SHOWING CART DETAILS
##    def cartdetails(self):
##        print('******CART DETAILS*********')
##        stre=' '
##        j=self.userfinalquantity
##        for i in j:
##            stre+=i+':'+str(j[i])+'\n'
##        return stre
##
####METHOD FOR SHOWING SHOPPING HISTORY           
##    def checkout(self):
##        print('****USER INFORMATION*******')
##        super().__init__()
##        t=self.readFromFile('C:/Users/SRK/OneDrive/Desktop/USER1INFORMATION.txt')
##        print(t[2].rstrip('\n'))
##        print(t[3].rstrip('\n'))
##        print(t[4].rstrip('\n'))
##        print(t[5].rstrip('\n'))
##        print(t[1].rstrip('\n'))
##        
##        
##
##        print('******SHOPPING BILL*********')
##        print('PRODUCT      QUANTITY           PRICE')
##        strw=' '
##        q=self.userfinalprices
##        m=self.userfinalquantity
##        for i in m:
##            strw+=i+'     '+str(m[i])+'       '+str(q[i])+'\n'
##        print(strw)
##        print('TOTAL BILL:',Cart.total(self))
##        
####SAVING THE USER CART DETAILS
##    def saveToFile(self,fileName):
##        eel=open(fileName,'a')
##        for go in  self.userfinalprices:
##                  eel.write(go+':'+str(self.userfinalquantity[go])+' :'+str(self.userfinalprices[go])+'\n')
##        eel.close()
##
##
##     
##class UserInterface:
##    def displaymenu(self):
##        print('1.CREATE ACCOUNT\n2.SHOW PRODUCTS PRICE THAT IS IN OUR STOCK\n3.SHOW THE STOCK OF THE PRODUCTS'
##              +' '+'IN STOCK\n4ADD ITEMS TO THE CART\n5.REMOVE ITEMS FROM CART\n6.SHOW CART DETAILS \n7.PROCEED TO CHECKOUT\n')
##
##    def enterstock(self):
##        print('***STOCK CAN BE ENTERED BY SHOP PERSONS ONLY****')
##        self.nut=Cart()
##        
##    def get(self):
##        while True:
##             choice=input('ENTER CHOICE:')
##             if choice=='1':
##                 self.ele=User()
##                 self.ele.userinfo()
##                 self.ele.saveToFile('C:/Users/SRK/OneDrive/Desktop/USER1INFORMATION.txt')
##                 self.ele.accountholders('C:/Users/SRK/OneDrive/Desktop/ACCOUNTHOLDERINFORMATION.txt')
##             elif choice=='2':
##                 self.kit=Product()
##                 self.kit.showingproducts()
##                 self.kit.saveToFile('C:/Users/SRK/OneDrive/Desktop/PRODUCTSPRICE.txt')
##             elif choice=='3':
##                print(self.nut.readstock())
##                self.nut.saveFile('C:/Users/SRK/OneDrive/Desktop/PRODUCTSSTOCK.txt')
##             elif choice=='4':
##                self.nut.additems()
##             elif choice=='5':
##                 self.nut.removeitems()
##            ##USER CAN SELECT THIS METHOD ONLY ONCE IF IT KEEP PRESSING '6' AND '7',IT WILL CHANGE THE DESIRED RESULT.
##             elif choice=='6':
##                self.nut.quantities()
##                print(self.nut.cartdetails())
##                self.nut.saveToFile('C:/Users/SRK/OneDrive/Desktop/USER1INFORMATION.txt')
##             elif choice=='7':
##                 self.nut.checkout()
##                 self.nut.saveToFile('C:/Users/SRK/OneDrive/Desktop/USER1INFORMATION.txt')
##                 break
##             else:
##                 break
##
##
####b=UserInterface()
####b.enterstock()
####b.displaymenu()
####b.get()
##d=UserInterface()
##d.enterstock()
##d.displaymenu()
##d.get()






