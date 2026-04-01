### string (Dizgi)
vocabulary="Python öğreniyorum Python "
# vocabulary= vocabulary.encode("utf-8")
print(len(vocabulary))
print(len(vocabulary.strip()))
print(vocabulary.strip())
print(vocabulary.lower())
print(vocabulary.islower())
print(vocabulary.upper())
print(vocabulary.isupper())
print(vocabulary.find("öğreniyorum"))

print(vocabulary.capitalize())
print(vocabulary.title())

print(vocabulary.replace("Python","Java"))

print(vocabulary.index("Python"))
print(vocabulary.rindex("Python"))

print(vocabulary[1])
print(vocabulary[1:4])
print(vocabulary[:4])
print(vocabulary[4:])

# print(vocabulary*3,sep=" - ")
#
# vocabulary1="java"
# vocabulary2="python"
# print(vocabulary1+" "+vocabulary2)

# vocabulary="Python öğreniyorum Python"
# print(vocabulary.startswith("Python"))
# print(vocabulary.endswith("Python"))
