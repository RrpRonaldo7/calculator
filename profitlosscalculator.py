 #introduction and service options
print("profit, loss, cp, sp,")

a= str(input("Kindly enter your service:"))
if a == "profit" or a == "loss":
    b = float(input("enter your cp:"))
    c = float(input("enter your sp:"))
    if b > c:
        print("loss of",(b-c), "loss", round((b-c)*100/c,1),"%")   #finding out loss/profit
    elif b < c:
        print("profit of", (c-b), "profit", round((c-b)*100/c,1),"%")
    else:
        print("error")

elif a == "cp":
    c=float(input("enter your sp:"))
    d=str(input("enter loss or profit:"))
    if d == "loss":
        e=float(input("enter your loss% :"))
        f=(c/(1-e/100))                               #finding out cp with loss and profit % cases
        print("your cp is",round(f,  1))
    elif d == "profit":
        e=float(input("enter your profit% :"))
        g=(c/(1 + e/100))
        print("your cp is",round(g, 1))
    else:
        print("enter valid option")
elif a == "sp":
    c=float(input("enter your cp:"))
    d=str(input("enter loss or profit:"))
    if d == "loss":
        e=float(input("enter your loss% :"))
        h=(c/(1-e/100))                              #finding out sp with loss and profit % cases
        print("your sp is",round(h, 1))
    elif d == "profit":
        e=float(input("enter your profit% :"))
        i=(c/(1 + e/100))
        print("your sp is",round(i, 1))
else:
    print("invalid input")



























