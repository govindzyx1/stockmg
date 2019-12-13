def showOption():
    print("1 Show Record:")
    print("2 Add Qty:")
    print("3 Dispatch Qty:")
    print("4 Price:")
    print("5 Total Billing Amt:")
    x = int(input("your option:"))
    return x

def insertItem(stock):
    pname = input("product name:")
    pqty = int(input("product qty:"))
    
    if pname in stock:
        q=stock[pname]+pqty
        stock[pname] = q
    else:
        stock[pname]=pqty
        

def dispatchItem(stock):
    pname=input("product name:")
    pqty = int(input("product qty:"))
    pprice = input("product price:")
    if pname in stock:
        q = stock[pname]
        if q>=pqty:
            stock[pname] = q-pqty
        else:
            print("Not sufficient qty")
    else:
            print("Product not avilable")

def priceOfTotal(stock):
    pprice = int
    q = stock[pprice]
    for n in range(pprice):
        stock[pprice] = q+pprice
        print(n)
        return n


def billing(stock):
    pname=input("product name:")
    pqty = int(input("product qty:"))
    pprice = int(input("product price:"))
    if pname in stock:
        q = stock[pname]
        if q>=pprice:
            stock[pname] = q+pprice
        else:
            print("Pls enter amount")
    else:
        print("Product not found")
    

    
