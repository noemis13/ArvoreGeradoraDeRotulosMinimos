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
	vertice = {} 
	valorVertice = 1
	
	for i in conteudoDoArquivo:
		for j in i:
			if(j == rotulo):
				vertice = {valorVertice: }
			else:
				valorLinha = 
				valorColuna =
				vertice = {valorVertice: }
		
		
		
ler_arquivo("HDGraph50_12.txt")

