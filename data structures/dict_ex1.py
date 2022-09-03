info=['mistborn','the final empire','brandon sanderson','tor.com',2099,2002]
info_dict={'series':'mistborn','title':'the final empire','author':'brandon sanderson','publisher':'tor.com','price':2099,'year':2009}
print(info_dict)
print(info_dict.keys())
print(info_dict.values())
print(info_dict.items())

print(info_dict['author'])
print(info_dict.get('year'))
print(info_dict.get('address'))
#print(info_dict['address'])  #gives error if key doesn't exists
#print(info_dict['2002'])

#update
info_dict['price']=599
print(info_dict)
#adding a new value pair
info_dict['rating']=10
print(info_dict)