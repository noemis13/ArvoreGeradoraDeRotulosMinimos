# coding: utf-8 
import string

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
	
	vetorVertices = []
	valorVertice = 1
	
	valor = 0
	contLinhas = 0
	
	for i in conteudoDoArquivo:
		contColunas = 0
		for j in i:
			contColunas = contColunas + 1
			vertice = {'posLinha': contLinhas, 'posColuna': contColunas, 'valorDoVertice': valorVertice}
			
			if(j != rotulo):
				for i in vertice: 
					if(contLinhas == vertice.get('posLinha') and contColunas == vertice.get('posColuna')):
						valor = vertice.get('valorDoVertice')
					
				vetorVertice = contLinhas, contColunas
				grafo ={'vertice': valor, 'ligado': vetorVertice, 'rotulo': j}	
			print grafo
			valorVertice = valorVertice + 1
		contLinhas = contLinhas + 1
		
				

"""
def criaGrafo(cabecalho, conteudoDoArquivo):
	rotulo = cabecalho[1]
	tamLaco = int(cabecalho[0])
	vertice = {} 
	valor = 1
	
	for i in conteudoDoArquivo:
		for j in i:
			if(tamLaco == 0):
				vertice = {}
				valor = 1
													
			if(j == rotulo):
				vertice = {'valorDoVertice': valor, 'rotulo': 0}
				valor = valor + 1
					
			else:
				vertice = {'valorDoVertice': valor, 'rotulo': j}
				valor = valor + 1
			
			print vertice
			mvca(vertice)
			tamLaco = tamLaco - 1
"""		
"""
-------------PASSOS DO MVCA-----------
1) pegar label por label
2) gerar a arvore com esses labels
3) pegar o proximo label e verificar com todos, e ver qual é o menor

c = armazena os labels
h = gera um subgrafo com os labels
Comp(c) = numero de componentes conexas
"""
def mvca(vertice):
	c = []
	c = vertice.get('rotulo')
		
ler_arquivo("HDGraph50_12.txt")

