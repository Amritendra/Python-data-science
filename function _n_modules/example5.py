from fileinput import filename

# def default_function(a=50,b=100):
#     return a+b

# print(default_function())
# print(default_function(a=99))
# print(default_function(b=255))



def triangle_area(b,h=1):
    return .5*b*h

print(triangle_area(8))
print(triangle_area(b=6,h=9))
print(triangle_area(b=5))
print(triangle_area(7,8))

def read(filepath=None):
    if filepath:
        with open(filepath) as f:
            return f.read()
    else:
        return 'please provide a filepath'
print(read('helper.py'))
print(read())
