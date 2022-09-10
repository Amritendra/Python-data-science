data="" #global variable
def data_appender(s): #s is parameter or argument
    global data #this line tell data_appender that we have a global var data
    if len(s)>0:
        data+=s
data_appender('hello')
data_appender(' world')
data_appender(' this is the simplest function')
data_appender(' pahle istemal kre phir viswas kre')

print(data)
