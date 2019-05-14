import time

#Busca o nome dado a uma variável
def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj and 'q' in name]

#Transforma a letra da entrada em um número para ser utilizado como index
def letraPraIndex(x):
    return {
        'a': 0,
        'b': 1,
    }[x]

#Busca dentro do vetor o que é imprimido e retorna o index
def indexDoPrint(Estados):
    if '0' in Estados:
        index = Estados.index('0')
    elif '1' in Estados:
        index = Estados.index('1')
    elif '2' in Estados:
        index = Estados.index('2')
    return index

#Checa se o estado é final, procurando por um elemento que diz se o estado é final
def checaFinal(Estados):
    indexFinal = 0
    if 'final' in Estados:
        indexFinal = Estados.index('final')

    return indexFinal


#Começo do código principal

#Informa o usuário para digitar uma entrada, essa entrada é salva na variável entrada
entrada = input(" Digite uma entrada: ")
print("")
saida = ""
FitaEntrada = [] * len(entrada)
i = 0


#Separa as letras da string salva na variável entrada para um vetor
for letras in entrada:
	FitaEntrada = list(entrada)

#Definicao dos elementos de cada estado
q0 = [1,3,'1']
q1 = [3,1,'0',"final"]
q2 = [0,3,'0']
q3 = [3,2,'2',"final"]

#Variável que salva o estado atual
estadoAtual = 0

#Vetor que possui todos os estados
arrEstados = [q0, q1, q2, q3]


#Loop de funcionamento da maquina de moore, le cada letra da FitaEntrada e executa de acordo com a entrada e o estado atual
for letra in FitaEntrada:
	arrEstadoAtual = arrEstados[estadoAtual]
	indexNovoEstado = arrEstadoAtual[letraPraIndex(letra)]
	print (" Estado Atual: " + str(namestr(arrEstados[estadoAtual], globals())) + " Entrada: " + letra)
	estadoAtual = indexNovoEstado
	arrNovoEstado = arrEstados[indexNovoEstado]
	indexPrint = indexDoPrint(arrNovoEstado)
	print (" Novo Estado: " + str(namestr(arrEstados[indexNovoEstado], globals())) + "\n")
	saida = saida + str(arrNovoEstado[indexPrint])
	print(" Saída: " + saida + "\n")

#Apresenta o estado final, a saida e se a mensagem foi aceita ou rejeitada
if (checaFinal(arrNovoEstado)):
	print(" Saída Final: " + saida)
	print(" Estado Final: " + str(namestr(arrEstados[estadoAtual], globals())))
	print(" Mensagem aceita\n")
else:
	print(" Saída Final: " + saida)
	print(" Estado Final: " + str(namestr(arrEstados[estadoAtual], globals())))
	print(" Mensagem Rejeitada\n")
