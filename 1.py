#coding:latin
"""Autômatos finitos.
Desenvolvido para a disciplina de Linguagens Formais, Autômatos e Computabilidade.
UTFPR-CM (2015-2)
Professor: Marco Aurélio Graciotto Silva
Aluno:Felipe V. Ramos
RA:1061461
BCC-4
"""

import sys
import copy

simbolo_branco = "!"
maquinas = []

def leia_arquivo(arquivo):
    """Lê o arquivo, retornando uma lista com as strings.
    """
    texto = []
    for linha in open(arquivo):
        texto.append(linha.replace("\n", ""))
    return texto

class TuringMachine(object):
    def __init__(self, alfabeto, alfabeto_fita, simbolo_branco, estados, estado_inicial, estados_aceitacao, transicoes, fita="", pos=0):
        self.alfabeto = alfabeto
        self.alfabeto_fita = alfabeto_fita
        self.simbolo_branco = simbolo_branco
        self.estados = estados
        self.estado_inicial = estados_iniciais
        self.estados_aceitacao = estados_aceitacao
        self.transicoes = transicoes

		self.fita = fita
		self.pos = pos

    def __repr__(self):
        return "Alfabeto: " + str(self.alfabeto) + "\nestados: " + str(self.estados) + "\nestado_inicial: " + str(self.estados_iniciais) + "\nEstados_aceitacao:"+ str(self.estados_aceitacao) + "\ntransicoes: " + str(self.transicoes)

    def transicoes_possiveis(self, estado_inicial, simbolo):
        self.proximos_estados = []
		ocorrencias = 0

        for t in self.transicoes:
            if t[0] == estado_inicial and (t[1] == simbolo or t[1] == simbolo_branco ):

			if ocorrencias > 1 :
				#nao determinismo
				tm2 = copy.deepcopy(self)
				tm2.proximos_estados.append(t[2])
				maquinas.append(tm2)
			else:
				ocorrencias++
				self.proximos_estados.append(t[2])

			#TODO se o simbolo de transição (t[1]) for !, criar uma nova tm e adiciona-la na liosta de tm
        return proximos_estados


def executa(af):
	#estados_atuais é af.estado_inicial
	#simbolo é af.fita[af.pos]
    proximos_estados = []
    for estado in af.estado_inicial:
        estados_temporarios = af.transicoes_possiveis(estado, af.fita[af.pos])
        for e in estados_temporarios:
            if not e in proximos_estados:
                proximos_estados.append(e)
	
	aceito = False
	af.estado_inicial = proximos_estados

	for estado in af.estado_inicial:
		if estado in af.estados_aceitacao:
			aceito = True
			
    return aceito

def prepara_tms(texto_cru):
	
    alfabeto = texto_cru[0].split(' ')
    print("#alfabeto " + str(texto_cru[0].split(' ')))
    
    alfabeto_fita = texto_cru[1].split(' ')
    print("#alfabeto_fita " + str(texto_cru[1].split(' ')))
    
    simbolo_branco = texto_cru[2].split
    print("#simbolo_branco " + str(texto_cru[2].split(' ')))
    
    estados = texto_cru[3].split(' ')
    print("#estados " + str(texto_cru[3].split(' ')))
    
    estados_iniciais = texto_cru[4].split(' ')
    print("#estados_iniciais " + str(texto_cru[4].split(' ')))
    
    estados_aceitacao = texto_cru[5].split(' ')
    print("#estados_aceitacao " + str(texto_cru[5].split(' ')))    
    
    transicoes =  []

    for t in texto_cru[6:]:
        transicoes.append(t.split(' '))
        print("#transicao " + str(t.split(' ')))    

	for estado in estados_iniciais:
		maquinas.append( TuringMachine(alfabeto, alfabeto_fita, simbolo_branco ,estados, estado, estados_aceitacao, transicoes))
	
	return maquinas

def main():
    if len(sys.argv) !=2:
        return

    texto_cru = leia_arquivo(sys.argv[1])
	maquinas = prepara_tms(texto_cru)
    #af = prepara_automato(texto_cru)


    fita = input("Digite a palavra a analisar, com os caracteres separados por espaços:")
	for tm in maquinas:
		tm.fita = fita

	aceito = False	
		for tm in maquinas:
			aceito = exeuta(tm)

		if aceito == True:
			break

    if aceito:
        print("Palavra aceita.")
    else:
            print("Palavra recusada.")




main()
