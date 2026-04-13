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


    # SETTER AND GETTER
    def set_marka(self,marka):
        self.marka=marka

    def get_marka(self):
        return self.marka


    def set_model(self,model):
        self.model=model

    def get_model(self):
        return self.model


    def set_yil(self,yil):
        self.yil=yil

    def get_yil(self):
        return self.yil


    def set_renk(self,renk):
        self.renk=renk

    def get_renk(self):
        return self.renk
