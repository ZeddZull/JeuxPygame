from Menu import *
from Snake import *

class MenuSnake(Menu):
	def __init__(self):
		Menu.__init__(self)
		self.options = ["Jouer","Score","Quitter"]
		self.titre = "Snake"
		self.miseAjourParametres()
		self.initScores()

	def initScores(self):
		c = Classement("scoreSnake")
		texte = self.font.render(str(c),1,self.couleur)
		

	def demarrer(self):
		continuer = True
		self.surface.fill(self.couleurFond)
		self.afficherMenu()
		self.afficheSelectMenu(pygame.mouse.get_pos())
		while continuer:

			ev = pygame.event.wait()

			if ev.type == pygame.QUIT:
				continuer = False

			elif ev.type == KEYDOWN:

				if ev.key == K_ESCAPE:
					continuer = False

			elif ev.type==pygame.VIDEORESIZE:
				self.miseAjourParametres()
				self.surface.fill(self.couleurFond)
				self.afficherMenu()
				self.afficheSelectMenu(pygame.mouse.get_pos())

			elif ev.type == MOUSEMOTION:
				self.afficheSelectMenu(ev.pos)

			elif ev.type == MOUSEBUTTONDOWN:
				if self.menuSelected == "Jouer":
					jeu = JeuSnake()
					jeu.demarrer()
					self.miseAjourMenu()
					self.surface.fill(self.couleurFond)
					self.afficherMenu()
					self.afficheSelectMenu(pygame.mouse.get_pos())
				elif self.menuSelected =="Quitter":
					continuer = False