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
	vertice = {} 
	valor = 1
	print tamLaco
		
	for i in conteudoDoArquivo:
		for j in i:
			if(j == rotulo):
				vertice = {'valorDoVertice': valor, 'rotulo': 0}
				valor = valor + 1
					
			else:
				vertice = {'valorDoVertice': valor, 'rotulo': j}
				valor = valor + 1
			
ler_arquivo("HDGraph50_12.txt")

