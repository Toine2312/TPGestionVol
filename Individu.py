import re

#Exceptions
class CodepostalError(Exception): 
	print ("Le code postale n'est pas valide")	

class Individu:
	def __init__(self,nom,prenom,adr,cp,ville):
		expression = r"^[0-9]{5}$"
		self.nomInd=nom
		self.prenomInd=prenom
		self.adresseInd=adr
		if not re.match(expression,cp):
			raise CodepostalError()
		else
			self.codePostalInd=cp
		self.villeInd=ville