#create a contacts dictionary,where the user can search for a person
#name and if the name exists ,it display the phone numbers
#else,the user should be provided a choice to add the phone number of that person
#also the user can also choose to list all person and numbers
cont={'amrit':965128765,'shiva':9876543456,'parth':9832674387,'ashmita':98437687236}
cont_info=input('enter the user name:')
if cont_info in cont:
    print(cont.get(cont_info))
else:
    print('contact not found ,u can add the number')
    add_cont=input('enter the contact name')
    add_num=input('enter the contact number:')
    cont[add_cont]=add_num
print(cont)
print(list(cont))
for key in cont:
    print(key,cont[key])

#using

