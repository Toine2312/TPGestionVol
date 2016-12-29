""" Tests unitaires pour roman.py """

import unittest
import roman


class KnownValues(unittest.TestCase):
	knownValues = ( (1, 'I'),
		(2, 'II'),
		(3, 'III'),
		(4, 'IV'),
		(5, 'V'),
		(6, 'VI'),
		(7, 'VII'),
		(8, 'VIII'),
		(9, 'IX'),
		(10, 'X'),
		(50, 'L'),
		(100, 'C'),
		(500, 'D'),
		(1000, 'M'),
		(31, 'XXXI'),
		(148, 'CXLVIII'),
		(294, 'CCXCIV'),
		(312, 'CCCXII'),
		(421, 'CDXXI'),
		(528, 'DXXVIII'),
		(621, 'DCXXI'),
		(782, 'DCCLXXXII'),
		(870, 'DCCCLXX'),
		(941, 'CMXLI'),
		(1043, 'MXLIII'),
		(1110, 'MCX'),
		(1226, 'MCCXXVI'),
		(1301, 'MCCCI'),
		(1485, 'MCDLXXXV'),
		(1509, 'MDIX'),
		(1607, 'MDCVII'),
		(1754, 'MDCCLIV'),
		(1832, 'MDCCCXXXII'),
		(1993, 'MCMXCIII'),
		(2074, 'MMLXXIV'),
		(2152, 'MMCLII'),
		(2212, 'MMCCXII'),
		(2343, 'MMCCCXLIII'),
		(2499, 'MMCDXCIX'),
		(2574, 'MMDLXXIV'),
		(2646, 'MMDCXLVI'),
		(2723, 'MMDCCXXIII'),
		(2892, 'MMDCCCXCII'),
		(2975, 'MMCMLXXV'),
		(3051, 'MMMLI'),
		(3185, 'MMMCLXXXV'),
		(3250, 'MMMCCL'),
		(3313, 'MMMCCCXIII'),
		(3408, 'MMMCDVIII'),
		(3501, 'MMMDI'),
		(3610, 'MMMDCX'),
		(3743, 'MMMDCCXLIII'),
		(3844, 'MMMDCCCXLIV'),
		(3888, 'MMMDCCCLXXXVIII'),
		(3940, 'MMMCMXL'),
		(3999, 'MMMCMXCIX'))
	
	def testToRomanKnownValues(self):
		"""toRoman doit donner les bons resultats aux valeurs connues"""
		for integer, numeral in self.knownValues:
		    result = roman.toRoman(integer)
		    self.assertEqual(numeral, result)

	def testFromRomanKnownValues(self):
		"""fromRoman doit donner les bons resultats aux valeurs connues"""
		for integer, numeral in self.knownValues:
		    result = roman.fromRoman(numeral)
		    self.assertEqual(integer, result)

class ToRomanBadInput(unittest.TestCase) :
	
	def testNegativeVal(self):
		"""toRoman doit echouer pour une valeur negative"""
		self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

	def testLongVal(self):
		"""toRoman doit echouer pour une valeur non entiere"""
		self.assertRaises(roman.NotIntegerError, roman.toRoman, 10.5)

	def testTooLarge(self):
	        """toRoman doit echouer pour un gros chiffre"""
	        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 4000)

	def testZero(self):
        	"""toRoman doit echouer pour 0"""
        	self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

class FromRomanBadInput(unittest.TestCase) :

	def testRepetSymbole(self):
		"""fromRoman doit echouer pour une valeur avec trop de repetitions de symboles """
		self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, 'XXXXVVVV')

	def testRepetPaire(self):
		"""fromRoman doit echouer pour une valeur avec des repetition de paires"""
		self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, 'XXXX')

	def testAntecedentIncorrect(self):
		"""fromRoman doit echouer pour une valeur avec des antecedents incorrects"""
		self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, 'VX')

class RomanValidation(unittest.TestCase) :
	
	def testMethodeCorrect(self):
		"""Pour tout entier n, converti en chiffre Romain puis reconverti en numerique doit etre egale a n"""	
		for n in [1,3999]:
			self.assertEqual(roman.fromRoman(roman.toRoman(n)), n)

	def testRomanCapitale_toRoman(self):
		"""Pour tout entier n, toRoman doit retourner une chaine en CAPITALE"""
		self.assertEqual(roman.toRoman(148), 'CXLVIII')

	def testRomanCapitale_fromRoman(self):
		"""fromRoman doit echouer si la chaine n'est pas toute en CAPITALE"""
		self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, 'CXLvIII')

if __name__ == "__main__" :
	unittest.main()
