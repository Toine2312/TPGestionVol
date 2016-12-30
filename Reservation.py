import Passager
import time
class Reservation:


	def __init__(self,codeV,dR,codeP):
		self.codeVol=codeV
		self.codeRes=codeReservation()
		self.dateReservation=dR
		self.codePassager=codeP
	
	def validerResa():
		pass

	def annulerResa():
		pass

	def newResa():
		nomP=raw_input("Nom: ")
		prenomP=raw_input("Prénom: ")
		adrP=raw_input("Adresse: ")
		cpP=raw_input("Code postal: ")
		villeP=raw_input("Ville: ")
		passager=Passager.Passager(nomP,prenomP,adrP,cpP,villeP)
		Vol.addResa(time.localtime(),passager.codePassager)