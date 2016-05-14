#coding:latin

import sys


def leia_arquivo(arquivo):
    """Lê o arquivo, retornando uma lista com as strings.
    """
    texto = []
    for linha in open(arquivo):
        texto.append(linha.replace("\n", ""))
    return texto

class AutomatoFinito(object):
    def __init__(self, alfabeto, estados, estados_iniciais, estados_aceitacao, transicoes):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estados_iniciais = estados_iniciais
        self.estados_aceitacao = estados_aceitacao
        self.transicoes = transicoes

    def __repr__(self):
        return "Alfabeto: " + str(self.alfabeto) + "\nestados: " + str(self.estados) + "\nestados_iniciais: " + str(self.estados_iniciais) + "\nEstados_aceitacao:" + str(self.estados_aceitacao) + "\ntransicoes: " + str(self.transicoes)

    def transicoes_com_epsilon( self, estado, cont = 0):
        if cont == len( self.estados ) + 1:
            return []

        estados = []
        estados.append( estado )
        for t in self.transicoes:
            if t[0] == estado and t[1] == "epsilon":
                print("transicao com epsilon de {} para {} ".format( estado, t[2] ))
                estados = list(set(estados + ( self.transicoes_com_epsilon( t[2], cont=cont+1))))
        return estados

    def transicoes_possiveis(self, estado_inicial, simbolo):
        proximos_estados = []
        for t in self.transicoes:
            if t[0] == estado_inicial and t[1] == simbolo:
                proximos_estados.append(t[2])
            #se houver transicoes em epsilon
            #if t[0] == estado_inicial and t[1] == "epsilon":
            #    transicoes_epsilon = self.transicoes_possiveis(t[2], simbolo)
            #    #Adiciona os estados de epsilon
            #    for tEpsilon in transicoes_epsilon:
            #        proximos_estados.append(tEpsilon)

        return proximos_estados

def prepara_automato(texto_cru):
    alfabeto = texto_cru[0].split(' ')
    #print("#alfabeto " + str(texto_cru[0].split(' ')))
    estados = texto_cru[1].split(' ')
    #print("#estados " + str(texto_cru[1].split(' ')))
    estados_iniciais = texto_cru[2].split(' ')
    #print("#estados_iniciais " + str(texto_cru[2].split(' ')))
    estados_aceitacao = texto_cru[3].split(' ')
    #print("#estados_aceitacao " + str(texto_cru[3].split(' ')))
    transicoes =  []

    for t in texto_cru[4:]:
        transicoes.append(t.split(' '))

    return AutomatoFinito(alfabeto, estados, estados_iniciais, estados_aceitacao, transicoes)

def executa(af, estados_atuais, simbolo):
    proximos_estados = []
    estados_epsilons = []
    estados_temporarios = []

    #Pega todas transicoes com epsilon
    for estado in estados_atuais:
        estados_epsilons = list(set(estados_epsilons + af.transicoes_com_epsilon( estado )))

    #Se estiver executando com um simbolo que não é o epsilon
    #e houver transicoes com epsilon
    #Processa somente o simbolo
    if simbolo != "epsilon" and len(estados_epsilons):
        for estado2 in estados_epsilons:
            proximos_estados = list(set(proximos_estados + af.transicoes_possiveis(estado2, simbolo)))

    #se o simbolo for epsilon e a lista for vazia
    elif simbolo == "epsilon":
        proximos_estados = list(set(proximos_estados + estados_epsilons))

    #finalmente, se o simbolo não for epsilon e a lista for vazia
    else:
        for e in estados_atuais:
            estados_temporarios = list(set(estados_temporarios + af.transicoes_possiveis( e, simbolo )))
            if not e in proximos_estados:
                proximos_estados.append(e)


    #print(proximos_estados)
    return proximos_estados



def main():
    if len(sys.argv) !=2:
        return

    texto_cru = leia_arquivo(sys.argv[1])
    af = prepara_automato(texto_cru)

    estados_atuais = af.estados_iniciais
    palavra =input("Digite a palavra a analisar, com os caracteres separados por espaços:").strip()

    if not len( palavra ):
        palavra = "epsilon"
    else:
        palavra = "epsilon " + palavra

    for simbolo in palavra.split(' '):
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
