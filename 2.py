
import sys
import copy
import pdb

simbolo_branco = '!'
maquinas = []

class configuracao(object):
    def __init__(self,fita,pos,estado):
        self.fita = fita
        self.pos = pos
        self.estado = estado    

    def moveRight(self):
        self.pos+= 1
        if self.pos > len(self.fita) -1:
            self.fita.append(simbolo_branco)

    def moveLeft(self):
        self.pos-= 1
        if self.pos < 0:
            self.fita.insert(0,simbolo_branco)
            self.pos += 1

    def write(self,simbolo):
        self.fita[self.pos] = simbolo

    def read(self):
        return self.fita[self.pos]


class TM(object):
    def __init__(self,transicoes,aceitacao,alfabeto,a_fita):
        self.alfabeto = alfabeto
        self.a_fita = a_fita
        self.transicoes = transicoes
        self.aceitacao = aceitacao
        self.configuracoes = []

    def step(self):
        #para cada configuracao
        #encontra uma transicao com o simbolo
        #altera a configuracao
        #se encontrar mais transicoes
        #cria uma nova configuracao
        #altera a nova configuracao
        #adiciona a nova configuracao na lista

        for conf in self.configuracoes:
            print(conf.__dict__)

        buffer_conf = []
        for conf in self.configuracoes:
            #procura estados
            ocorrencias = 0
            for transicao in self.transicoes:
                if conf.estado == transicao[0] and conf.read() == transicao[1]:
                    print( transicao )
                    ocorrencias+= 1

                    conf2 = copy.deepcopy( conf )
                    #muda o estado da configuracao
                    conf2.estado = transicao[2]
                    #escreve na fita
                    conf2.write(transicao[3])
                    #move a cabeca
                    if transicao[4] == "R":
                        conf2.moveRight()
                    else:
                        conf2.moveLeft()
                    #adiciona na lista de config.
                    buffer_conf.append(conf2)

        #adiciona as novas configuracoes na lista
        self.configuracoes = buffer_conf

    def aceitou(self):
        if len(self.configuracoes) == 0:
            print("Palavra não aceita")
            sys.exit(0)
            #return False

        for conf in self.configuracoes:
            if conf.estado in self.aceitacao:
                return True
            else:
                return False

def leia_arquivo():

    if len(sys.argv) != 2:
        print("Falta arquivo de entrada")
        sys.exit(1)

    texto = []
    for linha in open(sys.argv[1]):
        texto.append(linha.replace("\n", ""))
    return texto

def prepara_tm(texto_cru):
    
    alfabeto = texto_cru[0].split(' ')
    print("#alfabeto " + str(texto_cru[0].split(' ')))
    
    alfabeto_fita = texto_cru[1].split(' ')
    print("#alfabeto_fita " + str(texto_cru[1].split(' ')))
    
    simbolo_branco = texto_cru[2].split(' ')[0]
    print("#simbolo_branco " + str(texto_cru[2].split(' ')))
    
    estado_inicial = texto_cru[3].split(' ')[0]
    print("#estados_incial " + str(texto_cru[3].split(' ')))
    
    estados_aceitacao = texto_cru[4].split(' ')
    print("#estados_aceitacao " + str(texto_cru[4].split(' ')))
    
    #Lê as transicoes
    transicoes =  []
    for t in texto_cru[5:]:
        transicoes.append(t.split(' '))
        print("#transicao " + str(t.split(' ')))    

    #Instancia uma maquina de turing
    tm = TM(transicoes, estados_aceitacao, alfabeto, alfabeto_fita )

    #pega o conteudo inicial da fita
    conteudo_fita = input("Digite os elementos da fita separados por espaço: ")
    fita = conteudo_fita.split(' ')
    fita.insert(0,simbolo_branco)
    fita.append(simbolo_branco)


    #inicia uma configuracao para o estado inicial
    c = configuracao(fita,1,estado_inicial)
    tm.configuracoes.append( c )
    
    return tm

if __name__ == "__main__":
    texto = leia_arquivo()
    turing_machines = prepara_tm(texto)
    step = 0
    while not turing_machines.aceitou():
        print( step )
        step += 1
        turing_machines.step() 

        #Se houver mais de 500 passos
        #Verifica se a execucao deve continuar
        if step % 500 == 0 :
            op = input("{0} configuracoes geradas. Continuar ? [s/n]".format(step))
            if op.count('n') > 0:
                print("Termino de Execucao")
                sys.exit(0)
    
    print("Palavra aceita")
