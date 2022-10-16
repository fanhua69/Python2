quote = 'Let it be, let it be, let it be'
result = quote.rfind('let it')
print("Substring 'let it' : ", result)

result = quote.rfind('small')
print("Substring 'small':", result)

result = quote.rfind('be,')
if (result != -1):
    print("Highest index where 'be,' occurs:", result)
    print(quote[result:])
    print(quote[:result])
else:
    print("Doesn't contain substring")
    
quote="123456"
result = quote.index("5")
print("not found:",quote[result:])


quote="123,567,890"
result = quote.partition("==")
print(type(result))
print(result)

r=quote.split("=")
print(r)

quote="123\n456\n789\n"
r=quote.splitlines()
print(r)

if(quote.startswith("123")):
    print("startbwith 123")
else:
    print("not start")



