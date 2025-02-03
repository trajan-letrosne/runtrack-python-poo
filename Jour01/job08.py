from math import *
#besoin du module math pour utiliser le nombre pi
class Cercle:
    def __init__(self,rayon):
        self.rayon=rayon
        self.dia= self.diametre()
        self.circo= self.circonférence()
        self.air= self.aire()
    #j'initialise avec plusieur attributs dont certain sont déterminé par les
    #méthodes ci dessous

    def changerRayon(self):
        self.rayon=int(input("entrer votre nouveau rayon"))
    #methode pour changer de rayon

    def afficherInfos(self):
        print(f"""
            r = {self.rayon}
            diametre = {self.dia}
            circonférence = {self.circo}
            aire = {self.air}
        """)
    #affiche tout les attribut de l'objet depuis le constructeur
       
    def circonférence(self):
        circo=2* pi * self.rayon
        return circo

    def aire(self):
        air= pi * self.rayon * self.rayon
        return air
   
    def diametre(self):
        dia =self.rayon*2
        return dia
    # methodes qui calcules l' aire, la circonference et le diametre
    #les résultat sont renvoyé vers le constructeur

cercle1=Cercle(4)
cercle2=Cercle(7)

print(cercle1.afficherInfos(),cercle2.afficherInfos())
# je créé les deux cercles en tant qu'objet puis j'appelle mes fonctions
