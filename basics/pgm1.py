#WAp to calculate total price based on tghe following rules
#order amount>1000,discount of 3%
#if payment from credit card then 100rs off


order_amt=int(input("enter the amount"))
pm=(input("payment method(credit,cash,upi):"))
if order_amt>1000:
    dis=order_amt*3/100
    print(f"got discount of 3% {dis}")
if  pm=='credit':
    dis=order_amt -100
    print(f"got 100rs off {dis}")
else:
    print(f'no discoumt pay by cash {order_amt}')