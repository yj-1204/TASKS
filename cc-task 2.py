l={'SPORTS':[['cricket ball',30],['table tennis racquet',250],['bat',500],['football',300],['shuttle',500]],'STATIONARY':[['pen',10],['glue',10],['ruler',5],['stapler',20],['chart paper',10]],'DAILY-USE PRODUCTS':[['bucket',50],['broomstick',150],['soap',50],['toilet paper',50]]}
r={'SPORTS':[['cricket ball',25],['table tennis racquet',220],['bat',400],['football',250],['shuttle',400]],'STATIONARY':[['pen',8],['glue',8],['ruler',3],['stapler',17],['chart paper',7]],'DAILY-USE PRODUCTS':[['bucket',45],['broomstick',140],['soap',47],['toilet paper',48]]}
k=[]
class user():

    def display(self):
        for (i,j) in zip(l,l.values()):
            print(i)
            for k in j:
                print(k)
            print('\n\n')


    def display_cart(self):
        for i in k:
            print(i)


    def search(self):
        print('SEARCH')
        a=input('Enter the category of the product:\t')
        b=input('Enter product name:\t')

        a= a.upper()
        b=b.lower()
        for i in l:
            if i==a:
                n=l[i]
                for j in n:
                    if b in j:
                        print(j)
                        v = input('Do you wish to enter the product into your shopping cart?(y/n)')
                        w = int(input('Enter the quantity:'))
                        o=j
                        o[1]=o[1]*w
                        v = v.lower()
                        if v == 'y':
                            k.append(o)
                        else:
                            pass
        x=input('Do you wish to continue (y/n):')
        if x.lower()=='y':
            print('\n\n')
            q.search()
        else:
            pass



    def final_cart(self):
        q.display_cart()
        a=input('Do you wish to add anything to the cart(y/n):')
        if a.lower()=='y':
            q.search()
        b=input('Do you wish to remove anything from the cart(y/n):')
        if b=='y':
            b = input('Enter product name:\t\t')
            for i in k:
                if b==i[0]:
                    k.remove(i)
        print('Your current shopping cart:\n')
        q.display_cart()

    def bill(self):
        l = 0
        for i in k:
            print(i)
            l = l + i[1]
        print('GST (tax):', (28 * l) / 100)
        print('Total Cost:', l + ((28 * l) / 100))
        print('\n\n')

class admin():
    def cost(self):
        for i in r.values():
            for j in i:
                print(j)
    def profit(self):
        profit = l
        for (i,j,k) in zip(profit.values(),l.values(),r.values()):
            for (m,n,o) in zip(i,j,k):
                m[1]=n[1]-o[1]
        print('\n\nPROFIT PER PRODUCT\n')
        for (i, j) in zip(profit, profit.values()):
            print(i)
            for k in j:
                print(k)
            print('\n')


q=user()
p= admin()
a=input('Enter (Admin/User):\t\t')
if a.lower()=='user':
    print('WELCOME TO AKSHAY!!')
    q.display()
    q.search()
    q.final_cart()
    q.bill()
    print('Method of payment:\n1. swd\n2. UPI\n3. Cash')
    d=int(input("Enter your choice:"))
    if d==1:
        b = int(input('Enter your room no.:\t'))
        c = input('Enter your BITS-ID:\t\t')
        print('Money is deducted fom SWD!')
    if d==3:
        print('Thank you for shopping here! See you next time!')
    if d==2:
        print('Pay on the following id: akshay@gmail.com')

if a.lower()=='admin':
    print('1. Cost of the products\n2. Profit per product')
    d = int(input("Enter your choice:\t\t"))
    if d==1:
        p.cost()
    if d==2:
        p.profit()