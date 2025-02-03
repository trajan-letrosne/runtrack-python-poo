class Personne :
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
pers1=Personne("Lebrun","jean")
pers2=Personne("Garcia","Leo")
pers3=Personne("Jeune","Robert")

print(pers3.SePresenter())
print(pers2.SePresenter())
print(pers1.SePresenter())

# je creer une class Personne avec pour attribut nom et prenom puis une methode SePresenter
#qui retourn le phrase "je suis prenom nom", je créé plusieur objet avec la class Personne
#puis je les imprime en utilisant objet.SePresenter
