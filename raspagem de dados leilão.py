from functools import partial

from requests import get
from bs4 import BeautifulSoup

import pandas as pd
import re
import matplotlib.pyplot as plt

### this is not complete code contact 7019832930
class Webscraper:
	def __init__(self, url):
		self.url = url
		self.tags_each_place = []
		#self.more_pages()

	def get_price(self):
		data = get(self.url)
		soup = BeautifulSoup(data.content, "html.parser")
		#print("Visiting URL:", self.url)

		for anuncio in soup.find_all(
			attrs={"class": "valor"}):
			print("Valor: "+ "   " + str(anuncio.get_text()))

	def more_pages(self):

		data = get(self.url)
		#f1 = open('all_things.txt', 'w')
		soup = BeautifulSoup(data.content, "html.parser")
		print("CURRENT PAGE URL IS:", self.url)

		#all_anuncios = soup.find_all("div", class_="visualizacaoDiv-titulo")
		resultado = []

		#for x in soup.find_all("li", class_="visualizacaoDiv-border act-ss-filtro-lista-img lt-jucicial-1 act-classe-lote0"):
		#i = 0
		#for anuncio in soup.find_all("div", attrs={"class": "visualizacaoDiv-titulo"}):

		dict_anuncios = {}
		url_base = "https://www.sodresantoro.com.br/"

		for i in range (15):

			for anuncio in soup.find_all(attrs={"class": "visualizacaoDiv-border act-ss-filtro-lista-img lt-jucicial-1 act-classe-lote"+str(i)}):

				print("-------------------------------------")
				#print(anuncio.div)
				link = anuncio.div

				#print(link)

				for x in link.find_all(attrs={"class": "visualizacaoDiv-titulo-lote"}):
						#print(x)
						#print(x.prettify())
						#print("---------")
						for zz in link.find_all(attrs={"class": "titulo_1"}):
							#print(zz)
							dict_anuncios[i] = {"anuncio":zz.get_text() , "url": url_base + x.get("href")}

						#print(x.find("titulo_1"))
						#print("-> "  + x.get("href"))
				#print(anuncio)
				#y = anuncio.div
				#x = y.find('a')


				#print(type(x))
				#print(anuncio.a)
				#z = x.find('class="visualizacaoDiv-titulo-lote"')
				#print("XXXXXXXXXXXXX: " + str(x))
				#i = i + 1
				print("-----------------" +str(i) + "--------------------\n\n")

		#print(">>>" + str(lista_anuncios))
		#print(dict_anuncios)
		for i in range (15):
			print("-------------------------------------------------")
			print(str(i)  +  " - " + str(dict_anuncios[i]))
			raspagem = Webscraper(dict_anuncios[i]['url'])
			raspagem.get_price()
			print("-------------------------------------------------")
		#print(soup.prettify())

raspagem  = Webscraper("https://www.sodresantoro.com.br/veiculos/v_categoria/motos/")
raspagem.more_pages()