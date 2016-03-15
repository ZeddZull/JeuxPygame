import time
import os

class Score(object):
	def __init__(self,nom,score):
		self.nom = nom
		self.point = score
		self.date = time.localtime()

	def __lt__(self,autre):
		return self.point < autre.point

	def __eq__(self,autre):
		return self.point == autre.point and self.nom == autre.nom

	def __gt__(self,autre):
		return self.point > autre.point

	def __str__(self,espace = 10):
		return self.nom.center(espace) + str(self.point).center(espace)

class Classement(object):
	def __init__(self,nomFic):
		self.scores = []
		self.nomFic = nomFic
		self.charger()

	def ajout(self,score):
		if len(self.scores) == 0:
			self.scores.append(score)
		else:
			i = 0
			trouver = self.scores[0] < score
			while i < len(self.scores) and not trouver:
				if self.scores[i] < score:
					trouver = True
				else:
					i+=1
			if not trouver:
				if self.scores[i-1] == score:
					self.scores[i-1] = score
				else:
					self.scores.append(score)
			else:
				if self.scores[i-1] == score:
					self.scores[i-1] = score
				else:
					self.scores.insert(i,score)

	def charger(self):
		if os.path.exists(self.nomFic):
			f = open(self.nomFic,"r")
			for ligne in f:
				scoretxt = ligne.split(',')
				score = Score(scoretxt[0],int(scoretxt[1]))
				score.date = time.localtime(float(scoretxt[2]))
				self.scores.append(score)

	def sauver(self):
		f = open(self.nomFic,"w")
		for score in self.scores:
			f.write(score.nom+','+str(score.point)+','+str(time.mktime(score.date))+'\n')
		f.close()

	def __str__(self):
		res = "    "+"Nom".center(10)+"score".center(10)+'\n'
		for i in range(len(self.scores)):
			res += '\n'+str(i+1).center(4)+str(self.scores[i])+'\n'
		return res

