class operation :
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
        
    def addition(self,number1,number2):
        result=number1+number2
        return result

object=operation(1,2)
print(object.addition(1,2))

#on me demande de crer une methode addition et d'afficher le resultat de 
#l'addition donc je creer une variable methode addition qui retourne une 
#variable result que j'appelle avec object.addition