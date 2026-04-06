# Function

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


# 2- parametreli returnsuz
def hesap_topla2(sayi1,sayi2):
    """
    parametreli returnsuz toplam
    """
    sayi3=sayi1+sayi2
    print(f"Toplam: {sayi3}")

# Functional calling
hesap_topla2(10,20)