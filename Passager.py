class Passager:
	codePassager
	def __init__(self,nom,prenom,adr,cp,ville):
		codePassager=CodePassager()
		Individu.__init__(self,nom,prenom,adr,cp,ville)