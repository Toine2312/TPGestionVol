# coding=utf-8

#Classes de test permettant de tester toute les classes de notre modéles

import unittest
import Allcode
#import Client
#import Passager
#import Individu
#import Compagnie
#import Vol
#import Trajet
#import Saut
#import Etape
#import Aeroport
#import Ville

class CodeTest(unittest.TestCase):
	#Test des code de chaque entité
	
	def testCodeFranchise(self):
		#Le code franchise doit commencer par un F
		self.assertEqual(Allcode.CodeFranchise.char, 'F')

	def testCodeReservation(self):
		#Le code Reservation doit commencer par un R
		self.assertEqual(Allcode.CodeReservation.char, 'R')
	
	def testCodeVol(self):
		#Le code Vol doit commencer par un V
		self.assertEqual(Allcode.CodeVol.char, 'V')

	def testCodePassager(self):
		#Le code Passager doit commencer par un P
		self.assertEqual(Allcode.CodePassager.char, 'P')
		
	def testCodeClient(self):
		#Le code Client doit commencer par un C
		self.assertEqual(Allcode.CodeClient.char, 'C')

	def testCodeAeroport(self):
		#Le code Aeroport doit commencer par un C
		self.assertEqual(Allcode.CodeAeroport.char, 'A')

if __name__ == "__main__" :
	unittest.main()