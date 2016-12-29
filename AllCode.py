# coding=utf-8

"""Classe des code de chaque entités"""

import re
	

class Code:
	def __init__(self,car,s1):
		s=string (s1)
		self.code=car + s 	

class CodeFranchise:
	n=1
	char="F"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1

class CodeReservation:
	n=1
	char="R"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1

class CodeVol:
	n=1
	char="V"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1
		
class CodePassager:
	n=1
	char="P"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1
		
class CodeClient:
	n=1
	char="C"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1
		
class CodeAeroport:
	n=1
	char="A"
	def __init__(self):
		Code.__init__(self,char,n)
		n=n+1
