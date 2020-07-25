# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.
name = "Cryptography is an interesting field"
#str.capitalize()
print(name.capitalize())

#str.casefold()
print(name.casefold())

#str.center
print(name.center(10, "Y"))

#str.count
print(name. count('p', 3, 10))



#str.encode
print('The string is:', name)

# ignore error
print('The encoded version (with ignore) is:', name.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', name.encode("ascii", "replace"))
print('This is:', name.encode("utf8", "strict"))

#str.endswith
print(name.endswith("is an"))

#str.expandtabs default tab space us 8
n_me = "I\tam\tgood"
print(n_me.expandtabs(4))

#str.find
print(name.find ('interesting', 6, 10))
print(name.find ('field', 17, 43))

#str.format
# it can be empty
print("It is true that {} and this is {}".
format("we have a purpose", "why we exist"))
#it can also be numbered
print("It is true that {0} and this is {1}".
format("we have a purpose", "why we exist"))
#or named
print("It is true that {yay} and this is {wow}".
format(yay ="we have a purpose", wow ="why we exist"))


#str.format_map
task = {"x":5, "y":7}
print('{x}, {y}'.format_map(task))


#str.index
print(name.index ('interesting', 6, 40))
print(name.index ('field', 17, 43))

#str.isalnum
great = "space1"
print(name.isalpha())
print(great.isalnum())

#str.ascii
mane = "This is life"
print(ascii(mane))

#str.isdecimal()
great = "It's 0.0002879"
print(great.isdecimal())

#str.isdigit
great = " 250000 is the price"
print(great.isdigit())

#str.isidentifier
print(name.isidentifier())

#str.islower
print(name.islower())

#str.isnumeric
great = '250000'
print(great.isnumeric())

#str.isprintable()
print(name.isprintable())

#str.isspace()
print(name.isspace())

#str.istitle
print(name.istitle())

#str.isupper
print(name.isupper())

#str.join

sup = "224"
min = "abc"
gain = "same"
print("sup.join(min):", sup.join(min))

#str.lower()
print(name.lower())

#str.upper()
print(name.upper())

#str.ljust()
print(name.ljust(100))


#str.rjust()
print(name.rjust(100))

sup = "224"
min = "abc"
gain = "same"
print("sup.join(min):", sup.join(min))

#str.maketrans
print(gain.maketrans(sup, min))

#str.partition
print(name.partition(" is "))

#str.replace
print(name.replace("is","it"))

#str.rfind()
result = name.rfind("late", 6, 15)
print(result)

#str.rindex()
result = name.rindex("is", 6, 15)
print(result)

#str.rsplit()
print(name.rsplit(' , ' , 2))

#str.rstrip()
print(name.rstrip('2'))

#str.split()
print(name.split(' , '))

#str.splitlines()

#str.startswith()
print(name.startswith('is an', 13, 28))

#str.strip()
print(name.strip(' '))

#str.swapcase()
print(name.swapcase())

#str.title()
print(name.title())

#str.translate
sup = "224"
min = "abc"
gain = "ab"

string = "abc224"
print("Original string", string)
translation = string.maketrans(sup, min,gain)
print("translated string", string.translate(translation))



#str.zfill
print(name.zfill(50))
