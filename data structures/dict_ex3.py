
from pprint import pprint
movies={}
#adding a single value
movies['bhul bhulaiya']='horror and psychology'
movies['devdas']='love story'
movies['anabela']='scariest doll story'


#adding multipe values
movies.update(thor='god of thunder',
 omnamahshivay='mythological story',
 shaktiman='gangadhar')

#remove
movies.pop('anabela')

#update 
movies['shaktiman']='story of indian superhero'
#update 2
movies['shaktiman']+=' and saves the world from black and tamsic intention of tamjraj kilvis'
pprint(movies)
print(movies)