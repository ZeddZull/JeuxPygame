import pygame
from pygame.locals import *

class Menu(object):
	def __init__(self):
		self.hauteur = 800
		self.largeur = 800
		self.styleFont = "texgyrechorus"
		self.couleur = (0,255,0)
		self.couleurSelection = (0,0,255)
		self.couleurFond = (0,0,0)
		self.menuSelected = None
		self.options = []
		self.titre = ""
		pygame.init()
		self.fenetre = pygame.display.set_mode((self.largeur,self.hauteur),pygame.RESIZABLE)

	def miseAjourParametres(self):
		self.surface = pygame.display.get_surface()
		self.hauteur = self.surface.get_height()
		self.largeur = self.surface.get_width()
		self.tailleFont = self.hauteur//20
		self.font = pygame.font.SysFont(self.styleFont, self.tailleFont)
		self.fontG = pygame.font.SysFont(self.styleFont, self.tailleFont*2)
		self.miseAjourMenu()

	def miseAjourMenu(self,espace = 40):
		menu = {}
		hauteur = 0
		for option in self.options:
			texte = self.font.render(option,1,self.couleur)
			textepos = texte.get_rect()
			textepos.x = (self.largeur - textepos.width)//2
			hauteur += textepos.height + espace
			menu[option]=(texte,textepos)
		if self.titre == "":
			y = 0
		else:
			titre = self.fontG.render(self.titre,1,self.couleur)
			titrepos = titre.get_rect()
			titrepos.x = (self.largeur - titrepos.width)//2
			titrepos.y = (self.hauteur//8 - titrepos.height)//2
			self.titreS = (titre,titrepos)
			y = self.hauteur//8
		y += (self.hauteur - hauteur - espace)//2
		for option in self.options:
			menu[option][1].y = y
			y += textepos.height + espace
		self.menu = menu
		self.espace = espace
		self.menuSelected = None

	def afficherMenu(self):
		if self.titre != "":
			self.surface.blit(self.titreS[0],self.titreS[1])
		for option in self.options:
			self.surface.blit(self.menu[option][0],self.menu[option][1])
		pygame.display.flip()

	def afficheSelectMenu(self,pos):
		i = 0
		cherche = True
		while i < len(self.options) and cherche:
			option = self.options[i]
			optionS = self.menu[option][1]
			if optionS.collidepoint(pos):
				pygame.draw.rect(self.surface,self.couleurFond,optionS)
				texte = self.fontG.render(option,1,self.couleurSelection)
				textepos = texte.get_rect()
				textepos.x = optionS.x - (textepos.width - optionS.width)//2
				textepos.y = optionS.y - (textepos.height - optionS.height)//2
				self.menu[option]=(texte,textepos)
				self.surface.blit(texte,textepos)
				pygame.display.update(textepos)
				cherche = False
				self.menuSelected = option
			else:
				i+=1
		if cherche and self.menuSelected != None:
			option = self.menuSelected
			optionS = self.menu[option][1]
			pygame.draw.rect(self.surface,self.couleurFond,optionS)
			texte = self.font.render(option,1,self.couleur)
			textepos = texte.get_rect()
			textepos.x = optionS.x-(textepos.width - optionS.width)//2
			textepos.y = optionS.y - (textepos.height - optionS.height)//2
			self.menu[option]=(texte,textepos)
			self.surface.blit(texte,textepos)
			pygame.display.update(optionS)
			self.menuSelected = None