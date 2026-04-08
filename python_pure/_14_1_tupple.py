

# Boş bir tupple
empty_tupple = ()

# Önemli NOT: İlk eleman sonrasında mutlaka  virgül eklenmelidir.
empty_tupple=(11,)

#
empty_tupple=(11,22,33,55,44,44,66)
print(f"tupple -> {empty_tupple[0]}")
print(f"tupple -> {empty_tupple[-1]}")  # En son eleman
print()


print(f"tupple -> {empty_tupple[0:2]}")  #0<=DATA<=2-1
print(f"tupple -> {empty_tupple[3:]}")
print(f"tupple -> {empty_tupple[:3]}")
print(f"tupple -> {empty_tupple[::2]}")

# Sayma
# print(empty_tupple.index(2))
# print(empty_tupple.count(2))