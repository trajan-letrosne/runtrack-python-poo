class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = float(prixHT)
        self.TVA = float(TVA)
        self.prix=self.CalculerPrixTTC()
    #initialisation du produit avec trois attribut nom,prixHT et TVA


    def CalculerPrixTTC(self):
        self.prix = self.prixHT + self.prixHT*self.TVA /100
        return self.prix
    #calcul du prix finale en ajoutant la TVA en tant que pourcentage du prixHT


    def afficherProduit(self):
        return f"{self.nom} {self.prixHT} {self.TVA} {self.prix}"
    #une méthodepour afficher tout les attributs en même temps

    
    def ChangerNom(self):
        self.nom = input("Entrez le nouveau nom :")
        return self.nom
        
    def ChangerPrix(self):
        self.prixHT=float(input("Entrez un nouveau prix :"))
        return self.prixHT

    def ChangerTVA(self):
        self.TVA = float(input("Entrez la nouvelle TVA :"))
        return self.TVA
    #Trois méthodes pour changer directement un des attribut de l'objet
    

    def afficherNom(self):
        return f'{self.nom}'
    
    def afficherPrixHT(self):
        return f'{self.prixHT}'
    
    def afficherTVA(self):
        return f'{self.TVA}'
    
    def afficherPrix(self):
        return f'{self.prix}'
    #trois méthodes pour afficher chaqu'un des attribut
    
    
choco=Produit("Chocolat",12,20)
print(choco.CalculerPrixTTC())
lait=Produit("Lait",3,15)
print(lait.CalculerPrixTTC())

choco.ChangerNom()
choco.ChangerPrix()
choco.CalculerPrixTTC()
print(choco.afficherNom(),choco.afficherPrix())
lait.ChangerNom()
lait.ChangerPrix()
lait.CalculerPrixTTC()
print(lait.afficherNom(),lait.afficherPrix())

