#string validation
file=input("enter file name:")

if file.endswith('.png'):
   print('its apng file')
elif file.endswith('.jpg'):
    print("itd a png file")
elif file.endswith(".docx"):
    print('its a word file')
elif file.endswith('.py'):
    print("its s python file")

else:
   print('unidentified file')