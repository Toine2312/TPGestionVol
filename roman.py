"""Convertion de chiffres romains"""

import re

#Exceptions
class RomanError(Exception): 
	""" Exception generique """
	pass

class OutOfRangeError(RomanError): 
	""" Le nombre n'est pas dans l'intervalle de valeur """
	print "Le nombre n'est pas dans l'intervalle de valeur [1-3999]"


class NotIntegerError(RomanError): 
	""" Le nombre n'est pas un entier """
	print "Le nombre n'est pas un entier"


class InvalidRomanNumeralError(RomanError): 
	""" Le chiffre romain n'est pas valide """
	print "Le chiffre romain n'est pas valide"


# Table des symboles
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I', 1))

def toRoman(n):
	""" Converti un nombre vers en un chiffre romain"""
	if (n<1 or n>3999):
		raise OutOfRangeError()
	if not(isinstance(n,int)):
		raise NotIntegerError()
	resultat=""
	for symbole, nombre in romanNumeralMap:
		while (n>=nombre) :
			resultat=resultat+symbole
			n=n-nombre
	return resultat
	

# Expression reguliere de validation des chiffres romains
romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

def fromRoman(s):
	""" Converti un chiffre romain en nombre """
	if not(re.match(romanNumeralPattern,s)):
		raise InvalidRomanNumeralError()
	index=0
	resultat=0
	for symbole, nombre in romanNumeralMap:
		while (s[index:index+len(symbole)]==symbole):
			resultat=resultat+nombre
			index=index+len(symbole)
	return resultat


   	
