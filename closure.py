def gfg(raise_power_to):
    def power(number):
        return number ** raise_power_to
    return power


raise_power_to_3 = gfg(4)
print(raise_power_to_3(2))

print(type(raise_power_to_3.__closure__))
print(len(raise_power_to_3.__closure__))

print(type(raise_power_to_3.__closure__[0]))