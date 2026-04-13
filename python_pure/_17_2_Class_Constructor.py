# Class
class ArabaConstructor:
    def __init__(self,marka="Bilinmiyor",model="bilinmiyor",yil=0,renk="bilinmiyor"):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        print("Araba için yeni bir sınıf oluşturdum")

    # Function name
    def bilgileri_goster(self):
        print(f"Marka: {self.marka}  model:{self.model} yıl:{self.yil} renk:{self.yil}")


    # SETTER AND SETTER



