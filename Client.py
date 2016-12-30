import Reservation

class Client:
	codeClient
	carteBancaire
	cryptoVisuel
	dateExpiration
	userClient
	passwordClient
	client=[]

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
		boo=false
		reconnu=false
		while reconnu!=true:
			rep=int(raw_input("Nouveau client (oui:1 non:2) ? :"))
			if rep==1:
				nom=raw_input("Nom: ")
				prenom=raw_input("Prénom: ")
				adr=raw_input("Adresse: ")
				cp=raw_input("Code postal: ")
				ville=raw_input("Ville: "),
				numCB=raw_input("Numéro de carte bancaire: ")
				crypto=raw_input("Cryptogramme visuel: ")
				dateExpir=raw_input("Date d'expiration: ")
				user=raw_input("Utilisateur: ")
				pwd=raw_input("Mot de passe: ")
				client.append(Client(nom,prenom,adr,cp,ville,numCB,crypto,dateExpir,user,pwd))
				reconnu=true
			else
				user=raw_input("Utilisateur: ")
				for c in client:
					if user == c.userClient:
						pwd=raw_input("Mot de passe: ")
						while boo!=true :
							if pwd==c.passwordClient:
								print("Accés autorisé !")
								boo=true
							else
								print("Accés refusé !")
				print("utilisateur inconnu")


		nbClient=0
		nbClient=raw_input("Combien de passagers pour cette réservation?")
		for i in (1,nbClient):
			Reservation.newResa();