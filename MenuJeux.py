from Menu import *
from MenuSnake import *

class MenuJeux(Menu):

	# ICI on ajoute les jeux et leurs menus
	def __init__(self):
		Menu.__init__(self)
		self.options = ["Snake","Quitter"]
		self.lanceurs = {"Snake":MenuSnake,"Quitter":None}
		self.titre = "Jeux"
		self.miseAjourParametres()

	def demarrer(self):
		continuer = True
		self.afficherMenu()
		self.afficheSelectMenu(pygame.mouse.get_pos())
		while continuer:

			ev = pygame.event.wait()

			if ev.type == pygame.QUIT:
				continuer = False

			elif ev.type == KEYDOWN:

				if ev.key == K_ESCAPE:
					continuer = False
				if ev.key == K_0 or ev.key == K_KP0:
					jeu = self.lanceurs[self.jeux[0]]()
					jeu.demarrer()

			elif ev.type==pygame.VIDEORESIZE:
				self.miseAjourParametres()
				self.surface.fill(self.couleurFond)
				self.afficherMenu()
				self.afficheSelectMenu(pygame.mouse.get_pos())

			elif ev.type == MOUSEMOTION:
				self.afficheSelectMenu(ev.pos)

			elif ev.type == MOUSEBUTTONDOWN:
				if self.menuSelected != None:
					if self.lanceurs[self.menuSelected] != None:
						jeu = self.lanceurs[self.menuSelected]()
						jeu.demarrer()
						self.miseAjourMenu()
						self.surface.fill(self.couleurFond)
						self.afficherMenu()
						self.afficheSelectMenu(pygame.mouse.get_pos())
					else:
						continuer = False

m = MenuJeux()
m.demarrer()