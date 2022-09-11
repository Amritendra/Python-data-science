#keywords arguments - kwargs

def saveInfo(file='info.txt',**kwargs):
    with open(file,'r') as f:
        for k,v in kwargs.items():
            f.write(f'{k}->{v}\n')

saveInfo(mobile='motorola',price=20000,expiry='2024',
features='khus khas nahi')