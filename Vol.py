class Ville:
	def __init__(self,n):
		self.nameVille=n
		
class Aeroport:
	def __init__(self,c,n,v):
		self.codeAero=c
		self.nameAero=n
		self.villeAero=v
		
class Etape:
	def __init(self,d,a):
		self.dateEtape=d
		self.etapeAeroport=a
		
class Saut:
	def __init__(self,e1,e2):
		self.etapeDepart=e1
		self.etapeArrivee=e2
	
class Trajet:
	def __init__(self):
		self.listeSauts=[]
		
	def ajouterSaut(ca1,ca2,na1,na2,va1,va2,d1,d2):
		listeSauts.append(Saut(Etape(d1,Aeroport(ca1,na1,va1)),Etape(d2,Aeroport(ca2,na2,va2)))
	
class Individu:
	def __init__(self,c)
	

class Code:
	def __init__(self,car):
		self.code=0
		s=string (code)
		self.code=car + s
		
	def increment 	

class CodePassager:
	def __init__(self,n):
		Code.__init__(self,"P",n)
		
class CodeClient:
	def __init__(self,n):
		Code.__init__(self,"C",n)
		
class CodeAeroport:
	def __init__(self,n):
		Code.__init__(self,"A",n)