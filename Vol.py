class Vol:
	def __init__(self,dd,da):
		self.codeVol=codeVol()
		self.dateAVol=da
		self.dateDVol=dd
		self.listeRes=[]
		self.listePass=[]
		
	def addResa(self,time,codeP):
		resa=Reservation(self.codeVol,time,codeP)
		#Je vois pas à quoi serve les ligne en commentaire
		#res.creerRes(self.listeRes.len,self.listePass.len)
		self.listeRes.append(resa)
		#self.listePass.extend(resa.listePass)