
from enum import Enum

class Country(Enum):
	Afg = 93
	Alb = 255
	Alg = 213
	
print("mumber name: {}, member value:{}".format(Country.Afg.name, Country.Afg.value))

 
