class Client:
	codeClient
	carteBancaire
	cryptoVisuel
	dateExpiration
	userClient
	passwordClient

	def __init__(self,nom,prenom,adr,cp,ville,cb,de,cv,us,mdp):
		self.codeClient=CodeClient()
		Individu.__init__(self,nom,prenom,adr,cp,ville)
		self.carteBancaire=cb
		self.cryptoVisuel=cv
		self.dateExpiration=de
		self.userClient=us
		self.passwordClient=mdp

	def ReserverVol(n,nop):
		i=0
		client.append(Client(raw_input("Nom:"),
		raw_input("Prénom:"),raw_input("Adresse"),raw_input("Code postal"),raw_input("Ville"),
		raw_input("Numéro de carte bancaire:"),raw_input("Cryptogramme visuel:"),raw_input("Date d'expiration"),
		raw_input("Utilisateur:"),raw_input("Mot de passe:")))
		nbClient=0
		nbClient=raw_input("Combien de passagers pour cette réservation?")
		for i in (1,nbClient):
			client.append(Passager(raw_input("Nom:"),
			raw_input("Prénom:"),raw_input("Adresse"),raw_input("Code postal"),raw_input("Ville")))