#nested dict
from pprint import pprint
emps={'pratham':{'name':'pratham singh','salary':20000,'designation':'foreman'},
'amrit':{'name':'amrit maurya','salary':25000,'designtion':'asst 2','manager':'krish mehta'},
'ashmit':{'name':'ashmit pratap singh','salary':30000,'designation':'system officer'}
}

pprint(emps)
print("designation",emps['pratham']['designation'])

for key,data in emps.items():
    print(key,'~~')
    for k,v in data.items():
        print(k,v)
    print('*'*10)