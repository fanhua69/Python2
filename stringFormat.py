point={"x":4,"y":-5}
print('The x is {x}, the y is : {y}'.format(**point))

#s="Hello{}, your balance is {1:9.3f}".format("Adam",230.123)
#print(s)

# default arguments
#s="Hello {}, your balance is {:2d}.".format("Adam", 230.2346)


# positional arguments
print("Hello {1}, your balance is {0}.".format(123.44, 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

print("{:5.3f} {:1.2f}".format(12,34))
s="Hello {:012.3f}, {:5d}".format(324.43,4);
print(s)