'''
                                    ** Final Project **
Question:   Recipe Application
            Enter 3 recipes. Create a separate class for each recipe.
            Identify the products used in this recipe using the init() method.
            Write a function about how long these products should be used later.

            Do not forget to use inheritance here. Here to use inheritance;
            For example;
            Write a cooking function. Since this method will be common to all classes, you need to use inheritance here.
            
Coded By:   Yasin BİRCAN
Date:       21.02.2021
'''

class Yemekler():
    yemek1 = "- Menemen"
    yemek2 = "- Fasulye"
    yemek3 = "- Makarna"
    
    def tuzekle(self,yemektipi):
        self.yemektipi=yemektipi
        if(yemektipi == "Menemen"):
            print("25gr. tuz eklenir.")
        elif(yemektipi == "Fasulye"):
            print("50gr. tuz eklenir.")
        elif(yemektipi == "Makarna"):
            print("15gr. tuz eklenir.")

    def yagekle(self,yemektipi2):
        self.yemektipi2=yemektipi2
        if(yemektipi2 == "Menemen"):
            print("25gr. sıvı yağ eklenir.")
        elif(yemektipi2 == "Fasulye"):
            print("50gr. sıvı yağ eklenir.")
        elif(yemektipi2 == "Makarna"):
            print("15gr. sıvı yağ eklenir.")

    def pisir(self,yemektipi3):
        self.yemektipi3=yemektipi3
        if(yemektipi3 == "Menemen"):
            print("10 dk. pişirilir.")
        elif(yemektipi3 == "Fasulye"):
            print("20 dk. pişirilir.")
        elif(yemektipi3 == "Makarna"):
            print("30 dk. pişirilir.")
        
class Tarif1(): #Menemen Tarifi
    def __init__(self,malzeme1,malzeme2,malzeme3):
        self.malzeme1 = malzeme1 #domates
        self.malzeme2 = malzeme2 #soğan
        self.malzeme3 = malzeme3 #yumurta
        #super().__init__()
    def tarif1basla(self):
        print("MENEMEN TARİFİ:")
        print("3 adet " + self.malzeme1 + " ve 1 adet " + self.malzeme2 + " doğranır.")
        print(self.malzeme3 + " kırılır. Malzemeler tavaya eklenir.")
        Yemekler().tuzekle("Menemen")
        Yemekler().yagekle("Menemen")
        Yemekler().pisir("Menemen")
        print('\n')

class Tarif2(): #Fasulye Tarifi
    def __init__(self,malzeme4,malzeme5,malzeme6,malzeme7,malzeme8):
        self.malzeme4 = malzeme4 #fasulye
        self.malzeme5 = malzeme5 #soğan
        self.malzeme6 = malzeme6 #salça
        self.malzeme7 = malzeme7 #patates
        self.malzeme8 = malzeme8 #su
        #super().__init__()
    def tarif2basla(self):
        print("FASULYE TARİFİ:")
        print("1 kg. " + self.malzeme4 + " temizlenir")
        print("1 adet " + self.malzeme5 + " ve " + self.malzeme7 + " doğranır.")
        print("5gr. " + self.malzeme6 + " 5 bardak " + self.malzeme8 + " eklenir.")
        Yemekler().tuzekle("Fasulye")
        Yemekler().yagekle("Fasulye")
        Yemekler().pisir("Fasulye")
        print('\n')

class Tarif3(): #Makarna Tarifi
    def __init__(self,malzeme9,malzeme10):
        self.malzeme9 = malzeme9 #makarna
        self.malzeme10 = malzeme10 #su
        #super().__init__()
    def tarif3basla(self):
        print("MAKARNA TARİFİ:")
        print("10 bardak " + self.malzeme10 + " tavaya eklenir." )
        print("1 paket " + self.malzeme9 + " eklenir")
        Yemekler().tuzekle("Makarna")
        Yemekler().yagekle("Makarna")
        Yemekler().pisir("Makarna")

print("Tarif Edilecek Yemek Listesi:" + '\n' + Yemekler.yemek1 + '\n' + Yemekler.yemek2 + '\n' + Yemekler.yemek3 + '\n')

tarif1 = Tarif1("Domates", "Soğan" , "Yumurta")
tarif1.tarif1basla()

tarif2 = Tarif2("Fasulye", "Soğan" , "Salça", "Patates", "Su")
tarif2.tarif2basla()

tarif3 = Tarif3("Makarna", "Su")
tarif3.tarif3basla()



                
