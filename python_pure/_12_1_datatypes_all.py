########################################################################
############ LIST ######################################################
# Type -> List --> Tekrarlı veya Tekrarsız Veriler
# List --> <class 'list'>
my_list1=[1,2,9,3,"Malatya",True,14.53,"Malatya"]

print(f"List --> {type(my_list1)}")
print(f"List --> {my_list1}")
print()


########################################################################
############ TUPPLE ####################################################
# Type -> Tupple -->  Tekrarlı veya Tekrarsız veri ancak immutable(Değişmez)
# Tupple --> <class 'tuple'>
my_tupple1= (1,2,9,3,"Malatya",True,14.53,"Malatya")
print(f"Tupple --> {type(my_tupple1)}")
print(f"Tupple --> {my_tupple1}")


########################################################################
############ SET #######################################################
# Type -> Set -->  Tekrarsız Veriler
# Set --> <class 'set'>
my_set1={1,2,9,3,"Malatya",True,14.53,"Malatya"}

print(f"Set --> {type(my_set1)}")
print(f"Set --> {my_set1}")
print()


########################################################################
############ DICTIONARY ################################################
# Type -> Dictionary --> Key,Value
# Dictionary <class 'dict'>
person ={
    "name":"Hamit",
    "surname":"Mızrak",
    "is_login":True,
    "number":4423
}
print(f"Dictionary {type(person)}")
print(f"Dictionary {person}")