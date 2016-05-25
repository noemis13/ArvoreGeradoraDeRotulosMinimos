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
	numVertice = cabecalho[0]
	rotulo = cabecalho[1]
	
	vertice = []
	vertice = 1
	for i in conteudoDoArquivo:
		print vertice
			
		
ler_arquivo("HDGraph50_12.txt")

