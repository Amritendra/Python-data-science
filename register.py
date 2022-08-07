from grpc import GenericRpcHandler


name=("enter name")
email=("enter email")
password=("enter password")
cpassword=("cnfirm password")
Gender=("enter ur gender(M/F/T)")

if len(name)>4 and len(name)<25:
    if "@" in email:
        if 