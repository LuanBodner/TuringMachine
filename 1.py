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

def leia_arquivo(arquivo):
    """Lê o arquivo, retornando uma lista com as strings.
    """
    texto = []
    for linha in open(arquivo):
        texto.append(linha.replace("\n", ""))
    return texto

class TuringMachine(object):
    def __init__(self, alfabeto, alfabeto_fita, simbolo_branco, estados, estados_iniciais, estados_aceitacao, transicoes):
        self.alfabeto = alfabeto
        self.alfabeto_fita = alfabeto_fita
        self.simbolo_branco = simbolo_branco
        self.estados = estados
        self.estados_iniciais = estados_iniciais
        self.estados_aceitacao = estados_aceitacao
        self.transicoes = transicoes

    def __repr__(self):
        return "Alfabeto: " + str(self.alfabeto) + "\nestados: " + str(self.estados) + "\nestados_iniciais: " + str(self.estados_iniciais) + "\nEstados_aceitacao:
"         + str(self.estados_aceitacao) + "\ntransicoes: " + str(self.transicoes)

    def transicoes_possiveis(self, estado_inicial, simbolo):
        proximos_estados = []
        for t in self.transicoes:
            if t[0] == estado_inicial and (t[1] == simbolo or t[1] == 'B'):
                proximos_estados.append(t[2])
        return proximos_estados

def prepara_automato(texto_cru):
	
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

    return TuringMachine(alfabeto, alfabeto_fita, simbolo_branco ,estados, estados_iniciais, estados_aceitacao, transicoes)

def executa(af, estados_atuais, simbolo):
    proximos_estados = []
    for estado in estados_atuais:
        estados_temporarios = af.transicoes_possiveis(estado, simbolo)
        for e in estados_temporarios:
            if not e in proximos_estados:
                proximos_estados.append(e)
    return proximos_estados



def main():
    if len(sys.argv) !=2:
        #
        return

    texto_cru = leia_arquivo(sys.argv[1])
    af = prepara_automato(texto_cru)

    print(af)

    estados_atuais = af.estados_iniciais
    palavras = input("Digite a palavra a analisar, com os caracteres separados por espaços:")
    for simbolo in palavras.split(' '):
        print("Estado(s) atual(is): " + str(estados_atuais ))
        print("Fazendo transição com o símbolo " + simbolo + ".")
        estados_atuais = executa(af, estados_atuais, simbolo)
        print("Estado(s) após a transição: " + str(estados_atuais ))

    aceito = False
    for x in estados_atuais:
        if x in af.estados_aceitacao:
            aceito = True
            break

    if aceito:
        print("Palavra aceita.")
    else:
            print("Palavra recusada.")




main()
