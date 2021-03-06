# coding: utf-8 
import string
import igraph
from igraph import *
 

def ler_arquivo (nomeArquivo):
	conteudoDoArquivo = []
	arquivo = open(nomeArquivo, 'r')
	with open(nomeArquivo) as cab:
		cebecalho = cab.readline().split()
		"""print cebecalho"""	
	for linha in arquivo.readlines():
		conteudoDoArquivo.append(linha.rstrip().split())
	"""print conteudoDoArquivo"""			
	
	criaGrafo(cebecalho, conteudoDoArquivo)
	arquivo.close()

def criaGrafo(cabecalho, conteudoDoArquivo):
	rotulo = cabecalho[1]
	tamLaco = int(cabecalho[0])
	
	g = igraph.Graph()
	
	vetorVertices = []
	valorVertice = 1
	
	valor = 0
	contLinhas = 0
	
	for i in conteudoDoArquivo:
		contColunas = 0
		for j in i:
			if(tamLaco == 0):
				grafo = {}
				vertice = {}
				valorVertice = 1
				
			contColunas = contColunas + 1
			vertice = {'posLinha': contLinhas, 'posColuna': contColunas, 'valorDoVertice': valorVertice}
			
			if(j != rotulo):
				valor = encontraVertice(vertice, contLinhas, contColunas)
				vetorVertice = contLinhas, contColunas
				
				g.add_vertices(valor)
				print g
				"""grafo ={'vertice': valor, 'ligado': vetorVertice, 'rotulo': j}"""	
			
			valorVertice = valorVertice + 1
			"""mvca(grafo)"""
		contLinhas = contLinhas + 1
		tamLaco = tamLaco - 1
		
		
def encontraVertice (vertice, contLinhas, contColunas):				
	for i in vertice: 
		if(contLinhas == vertice.get('posLinha') and contColunas == vertice.get('posColuna')):
			valor = vertice.get('valorDoVertice')
	return valor			
		
"""
-------------PASSOS DO MVCA-----------
1) pegar label por label
2) gerar a arvore com esses labels
3) pegar o proximo label e verificar com todos, e ver qual é o menor
4) retornar o menor numero de rotulos q liga todo mundo

c = armazena os labels
h = gera um subgrafo com os labels
Comp(c) = numero de componentes conexas
"""
def mvca(grafo):
	tamArestas = []
	for i in grafo:
		c = grafo.get('rotulo')
		tamArestas = grafo.get('ligado')
		minimo = 2
		if (len(tamArestas) <= minimo):
			grafoFinal = {'vertice': grafo.get('vertice'), 'ligado': tamArestas, 'rotulo': c}
			
	
		
ler_arquivo("HDGraph50_12.txt")

