
from enum import Enum

class Country(Enum):
	Afg=93
	Alb =94


for data in Country:
	print("Country is {}, value is {}".format(data.name,data.value))
	print(f"country is {data.name}, value is {data.value}")
	print("Country is %s, value is 0X%x " % (data.name, data.value))
	print("Country is %(name)s, value is 0X%(value)x" % { "name" : data.name, "value":data.value})

