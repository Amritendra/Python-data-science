#wap to create a list from user of m elements .if the user enters a duplicate value
#dont add it to list and warn the user about their mistake 
#wap to create a list and then replace all value greater then 5,by 0
#wap to create a list that contains 5 small sublists of 3 items each(nested list)
#take the input from user to create this nested list.

#ques1

x=[]
for i in range(10):
    val=input(f"enter the value{i+1}:")
    if val in x:
        print("u entered duplicate values")
    else:
        x.append(val)
print("the list x")
print(x)


#ques2

a=[2,6,4,23,56,76,3,5,8,9,54,12,2,1,3,4,]
for i in range(len(a)):
    if a[i]>5:
       a[i]=0
print(a) 


#ques3
l1=[]
l2=[]
l3=[]
l3=[]
l4=[]
l5=[]
nested_list=[l1,l2,l3,l4,l5]
for i in range(3):
    val1=input('enter the values of list1:')
    l1.append(val1)
    val2=input('enter the values of list2:')
    l2.append(val2)
    val3=input('enter the values of list3:')
    l3.append(val3)
    val4=input('enter the values of list4:')
    l4.append(val4)
    val5=input('enter the values of list5:')
    l5.append(val5)
print(nested_list)

