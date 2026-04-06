# Function

##################################################
# 1- parametresiz returnsuz
def hesap_topla1():
    """
    parametresiz returnsuz toplam
    """
    sayi1=20
    sayi2=30
    sayi3=sayi1+sayi2
    print(f"Toplam: {sayi3}")

# Functional calling
hesap_topla1()

##################################################
# 2- parametreli returnsuz
def hesap_topla2(sayi1,sayi2):
    """
    parametreli returnsuz toplam
    """
    sayi3=sayi1+sayi2
    print(f"Toplam: {sayi3}")

# Functional calling
hesap_topla2(10,20)
print()


##################################################
# Default
def default_toplam(sayi1,sayi2=90):
    """
    parametreli returnsuz toplam
    """
    sayi3=sayi1+sayi2
    print(f"Toplam: {sayi3}")

# Functional calling
default_toplam(10)
default_toplam(10,20)
print()

##################################################
# 3- parametresiz returnlu
def hesap_topla3():
    """
    parametresiz returnlu toplam
    """
    sayi1=100
    sayi2=30
    sayi3=sayi1+sayi2
    return sayi3

# Functional calling
result=hesap_topla3()
print(f"Toplam: {result}")
print()



##################################################
# 4- parametreli,default returnlu
def hesap_topla4(sayi1=20,sayi2=90):
    """
    parametresiz returnlu toplam
    """
    sayi3=sayi1+sayi2
    return sayi3

# Functional calling
result2=hesap_topla4()
print(f"Toplam: {result2}")

result2=hesap_topla4(40,15)
print(f"Toplam: {result2}")

print()
