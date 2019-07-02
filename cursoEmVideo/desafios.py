#! python3
# CURSO EM VÍDEO - PYTHON BÁSICO

import requests, math, random, time
from pygame import mixer


def desafio1(a=''):
	'''LER UM NOME E FAZER SAUDAÇÃO'''
	nome = str(input('Qual seu nome?'))
	return f'Olá {nome}! Seja bem vindo'


def desafio2(a=''):
	'''RECEBER DIA, MÊS E ANO E RETORNAR DATA FORMATADA'''
	dia = int(input('DIA = '))
	mes = int(input('MÊS = '))
	ano = int(input('ANO = '))

	return f'A data formatada é: {dia}/{mes}/{ano}'


def desafio3(a=''):
	'''RECEBER DOIS NÚMEROS E REALIZAR A SOMA'''
	numero1 = int(input('Primeiro número: '))
	numero2 = int(input('Segundo número: '))
	return f'A soma de {numero1} + {numero2} = {numero1 + numero2}'


def desafio4(a=''):
	'''VERIFICAÇÃO DE TIPOS'''
	arg = input('Digite o que quiser: ')

	if arg.isnumeric():
		return f'{arg} é um número.'
	elif arg.isalpha():
		return f'{arg} é um texto'
	elif arg.isalnum():
		return f'{arg} é alfanumérico'
	else:
		return 'sei não'


def desafio5(a=''):
	num = int(input('Entre com um número: '))

	return f'O antecessor é {num - 1} e o sucessor é {num + 1}'


def desafio6(a=''):
	'''OPERADORES ARITMÉTICOS'''
	num = int(input('Digite um número: '))
	print(f'O dobro de {num} é {num * 2}.')
	print(f'O triplo de {num} é {num * 3}.')
	print(f'A raiz quadrada de {85} é {num ** 0.5}.')

	pass


def desafio7(a=''):
	'''CALCULAR MÉDIA DE DOIS VALORES'''
	num1 = int(input('Entre com a primeira nota: '))
	num2 = int(input('Entre com a segunda nota: '))

	return f'A média do aluno é: {(num1 + num2)/2}'


def desafio8(a=''):
	'''CONVERTER METROS EM MILIMETROS E CENTIMETROS'''

	metros = float(input('Entre com o valor em métros: '))

	return f'Este valor em centímetros é {metros*100} e em milímetros é {metros*1000}'


def desafio9(a=''):
	'''TABUADA FORMATADA'''

	num = int(input('Qual a tabuada você quer ver? '))

	for i in range(1, 11):
		print(f'{num} * {i:2} = {num * i}')

	pass


def desafio10(a=''):
	'''CONVERTER REAL EM DOLAR'''

	r = requests.get('https://api.hgbrasil.com/finance/quotations?format=json&key=b533ca4d')

	dados = r.json()

	dolar = float(dados['results']['currencies']['USD']['buy'])

	real = float(input('Qual o valor você tem na carteira? '))

	return f'Você pode comprar US${real / dolar:.2f}'


def desafio11(a=''):
	'''CALCULAR QUANTIDADE DE TINTA'''

	largura = float(input('Qual a largura da parede?'))

	altura = float(input('qual a altura da parede?'))

	metro_quadrado = largura * altura

	print(f'Sua parede tem {metro_quadrado}m².')

	quantidade_de_tinta = metro_quadrado * 0.5

	return f'São necessários {quantidade_de_tinta:.3f}l de tinta para pinta-la'


def desafio12(a=''):
	'''CALCULAR DESCONTO DE 5%'''

	valor_do_produto = float(input('Qual o valor do produto?'))

	return f'O valor do produto com 5% de desconto é R${valor_do_produto * 0.95}'


def desafio13(a=''):
	'''CALCULAR AUMENTO SALÁRIO 15%'''

	valor_do_salario = float(input('Qual o valor do salário?'))

	return f'O valor do salário com 15% de aumento é R${valor_do_salario * 1.15}'


def desafio14(a=''):
	'''CONVERTER °C EM  °F'''

	temperatura = float(input('Qual a temperatura em °C? '))

	return f'{temperatura}°C é o mesmo que {temperatura * 1.8 + 32}°F'


def desafio15(a=''):
	'''CALCULAR PREÇO DE ALUGUEL POR DIAS E KM RODADOS'''

	km_rodados = float(input('Qual a quilometragem rodada? '))

	dias_aluguel = int(input('Quantos dias de aluguel? '))

	valor_total = (km_rodados * 0.15) + (dias_aluguel * 60)

	return f'Valor das diárias R${km_rodados * 0.15:.2f} + valor da kilometragem R${dias_aluguel * 60} = Total R${valor_total}'


def desafio16(a=''):
	'''PEGAR UM NÚMERO REAL E SÓ EXIBIR A PARTE INTEIRA COM A LIB MATH'''

	num = float(input('Digite o número: '))

	return f'A parte inteira de {num} é {math.trunc(num)}'


def desafio17(a=''):
	'''CALCULAR A HIPOTENUSA DOS CATETOS'''

	cateto1 = float(input('Cateto oposto: '))

	cateto2 = float(input('Cateto adjacente: '))

	return f'A hipotenusa dos catetos {cateto1} e {cateto2} = {math.hypot(cateto1, cateto2):.2f}'


def desafio18(a=''):
	'''RETORNAR O SENO, COSSENO, TANGENTE DE UM NÚMERO'''

	num = float(input('Entre com o número desejado: '))

	return f'Seno, cosseno e tangente de {num} é respectivamente: {math.sin(num)}, {math.cos(num)}, {math.tan(num)}.'


def desafio19(a=''):
	'''SORTEAR UM NOME ENTRE 4'''

	nomes = ['','','','']

	for item in range(0,4):
		nomes[item] = input(f'Entre com o {item + 1}º nome: ')

	return f'O sorteado foi {random.choice(nomes)}'


def desafio20(a=''):
	'''SORTEAR UMA ORDEM EM UMA LISTA'''

	nomes = ['','','','']

	for item in range(0,4):
		nomes[item] = input(f'Entre com o {item + 1}º nome: ')

	random.shuffle(nomes)

	return f'A ordem sorteada foi: {nomes}'

def desafio21(a=''):
	'''REPRODUZIR MP3 EM PYTHON'''

	mixer.init()

	mixer.music.load('desafio21.mp3')
	mixer.music.play()
	time.sleep(10)
	mixer.music.stop()

	return None


def desafio22(a=''):
	'''MANIPULAÇÃO DE STRINGS'''

	nome = str(input('Qual seu nome? '))

	primeiro_nome = nome.strip().split()

	print(f"""
	UPPER: {nome.strip().upper()}
	LOWER: {nome.strip().lower()}
	CARACTERES: {len(nome.strip()) - nome.strip().count(' ')}
	TAMANHO PRIMEIRO NOME: {len(primeiro_nome[0])}""")

	return None


def desafio23(a=''):
	'''RECEBER UM NÚMERO E FALAR UNIDADE, DEZENA, CENTENA E MILHAR'''
	numero = int(input('Entre com um número de 0 a 9999:'))

	unidade = numero // 1 % 10
	dezena = numero // 10 % 10
	centena = numero // 100 % 10
	milhar = numero // 1000 % 10

	print(f'\nunidade: {unidade}\ndezena: {dezena}\ncentena: {centena}\nmilhar: {milhar}')

	return None

''' #RESOLUÇÃO UTILIZANDO STRING
	numero = str(input('Entre com um número de 0 a 9999:'))

	if numero == 0:
		print('\nunidade: 0\ndezena: 0\ncentena: 0\nmilhar: 0')
	elif len(numero) == 1:
		print(f'\nunidade: {numero}\ndezena: 0\ncentena: 0\nmilhar: 0')
	elif len(numero) == 2:
		print(f'\nunidade: {numero[1]}\ndezena: {numero[0]}\ncentena: 0\nmilhar: 0')
	elif len(numero) == 3:
		print(f'\nunidade: {numero[2]}\ndezena: {numero[1]}\ncentena: {numero[0]}\nmilhar: 0')
	elif len(numero) == 4:
		print(f'\nunidade: {numero[3]}\ndezena: {numero[2]}\ncentena: {numero[1]}\nmilhar: {numero[0]}')
	else:
		print('São válidos somente números entre 0 e 9999!')'''


def desafio24(a=''):
	'''VERIFICAR SE O NOME DA CIDADE COMEÇA COM SANTO'''
	cidade = str(input('Qual o nome da cidade: '))

	if cidade[:5].strip().upper() == 'SANTO':
		print(f'A cidade {cidade} começa com Santo.')
	else:
		print(f'A cidade {cidade} não começa com Santo.')


def desafio25(a=''):
	'''VERIFICAR SE A PESSOA POSSUI SILVA NO NOME'''

	nome = str(input('Qual o seu nome completo: '))

	if nome.upper().find('SILVA') == -1:
		print('Seu nome não contém Silva.')
	else:
		print('Seu nome contém Silva.')


def desafio26(a=''):
	'''REPETIÇÕES E POSIÇÕES DA LETRA A NA FRASE'''

	frase = str(input('Digite uma frase: ')).strip()

	repeticoes_de_a = frase.lower().count('a')
	primeira_ocorrencia_a = frase.lower().find('a') + 1
	ultima_ocorrencia_a = frase.lower().rfind('a') + 1

	print(f'A letra A aparece {repeticoes_de_a} vezes na frase\nA primeira ocorrência foi na {primeira_ocorrencia_a}ª posição\nA ultima na {ultima_ocorrencia_a}ª posição')


def desafio27(a=''):
	'''IDENTIFICAR PRIMEIRO E ÚLTIMO NOME'''
	nome = str(input('Nome completo: '))

	nome = nome.split()

	print(f'Primeiro nome: {nome[0].strip()}')
	print(f'Ultimo nome: {nome[len(nome)-1].strip()}')

	return None


def desafio28(a=''):
	'''JOGO DE ADIVINHAR NÚMERO DE 0 - 5'''
	mensagem = f'''{'-=-' * 20}\nVOU PENSAR EM UM NÚMERO DE 0 - 5. TENTE ADIVINHAR...\n{'-=-' * 20}'''

	print(mensagem)
	aleatorio = random.randint(0,6)
	numero = int(input('Adivinhe o número de 0 - 5: '))
	print('PROCESSANDO...')
	time.sleep(1)
	print(f'Acertou mizeravi!' if numero == aleatorio else f'Errou mardito o número era {aleatorio}!')

	return None


def desafio29(a=''):
	'''MULTA POR VELOCIDADE'''
	velocidade = float(input('Qual a velocidade do veículo: '))

	if velocidade > 80:
		multa = (velocidade - 80) * 7
		print(f'Você foi multado em R${multa:.2f} por estar acima da velocidade')
	else:
		print('Dentro do limite de velocidade.')

	return None


def desafio30(a=''):
	'''É PAR OU ÍMPAR'''
	numero = int(input('Qual o número: '))

	print('É par.' if numero % 2 == 0 else 'É ímpar.')

	return None


def desafio31(a=''):
	'''PREÇO DA VIAGEM'''
	km_distancia = float(input('Distância da viagem: '))

	print(f'O valor é: R${km_distancia * 0.5}' if km_distancia <= 200 else f'O valor da viagem é: {km_distancia * 0.45}')

	return None


def desafio32(a=''):
	'''É BISEXTO OU NÃO É?!?!'''
	ano = int(input('Ano bisexto??? '))

	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
		print('Ano bisexto!')
	else:
		print('Não é bisexto!')

	return None


def desafio33(a=''):
	'''MAIOR E MENOR NÚMERO'''
	for i in range(0,3):
		numero = int(input(f'Qual o {i+1}º número : '))
		if i == 0:
			maior, menor = numero, numero
		else:
			if numero > maior:
				maior = numero
			elif numero < menor:
				menor = numero

	print(f'Menor: {menor}\nMaior: {maior}')

	return None


def desafio34(a=''):
	'''AUMENTO DE SALÁRIO'''
	salario = float(input('Qual o valor do salário: '))

	if salario > 1250.0:
		salario = salario * 1.10
	else:
		salario = salario * 1.15

	print(f'Novo salário: R${salario}')

	return None


def desafio35(a=''):
	'''É TRIÂNGULO OU NÃO É?!?!?!?!'''
	reta_a = float(input('Reta A: '))
	reta_b = float(input('Reta B: '))
	reta_c = float(input('Reta C: '))

	if (reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a):
		print('Pode formar um triângulo.')
	else:
		print('Não forma um triângulo.')

	return None


def cores_no_terminal(a=''):
	print('Para utilizar cores no terminal, basta utilizar código ANSI.\n\n \\033[<estilo>;<cor-da-letra>;<cor-de-fundo>m\n')
	print('\33[1;30;42mAbaixo temos as tabelas de cores:'+'\033[0m\n')

	print('ESTILO - COR LETRA - COR FUNDO')

	estilo, cor_letra, cor_fundo = 0, 30, 40

	padrao_estilo = f'\033[{estilo};0;0m'
	padrao_letra = f'\033[0;{cor_letra};0m'
	padrao_fundo = f'\033[5;0;{cor_fundo}m'
	preto = '\033[0;0;0m'

	for i in range(9):
		for j in range(3):
			if j == 0:
				if i == 0 and estilo < 8:
					print(padrao_estilo + f'{estilo:3}', end=" ")
					estilo += 1
					padrao_estilo = f'\033[{estilo};0;0m'
				elif i >= 1 and estilo < 8:
					print(padrao_estilo + f'{estilo:3}', end=" ")
					estilo += 3
					padrao_estilo = f'\033[{estilo};0;0m'
				else:
					print(preto + '    ', end="")
			elif j == 1:
				print(padrao_letra + f'{cor_letra:9}', end=" ")
				cor_letra += 1
				padrao_letra = f'\033[0;{cor_letra};0m'
			else:
				print(preto, end="          ")
				print(padrao_fundo + f'{cor_fundo}', end="")
				cor_fundo += 1
				padrao_fundo = f'\033[0;0;{cor_fundo}m'
				print(preto, end="")
		print()

	return None