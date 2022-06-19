import bdCantadas
from random import choice

while True:
  print('\033[31m=\033[m' * 50)
  print('\033[31m                 GURU DO AMOR\033[m')  # GURU RAUL
  print('\033[31m=\033[m' * 50)

  # ENTRADA PESSOA INTERESSADA
  nome = str(input('Digite o seu nome Guerreiro(a): ')).upper().strip()
  idadeEu = int(input('Sua idade:'))
  print('\033[34m=+\033[m' * 30)

  # ENTRADA ALVO
  alvo = str(input('Digite o nome do alvo: ')).upper().strip()
  idadeA = int(input('Digite a idade do alvo: '))
  print('\033[34m=+\033[m' * 30)

  # PROCESSAMENTO 1
  diferença = idadeEu - idadeA

  if idadeEu >= idadeA:
    diferença = idadeEu - idadeA
  
  elif idadeA >= idadeEu:
    diferença = idadeA - idadeEu
  print(f'Diferença em anos: {diferença}')

  if diferença > 4 and idadeA < 18 or diferença > 4 and idadeEu < 18:
    print("\033[31mOLHA A POLICÍAAAAAAAAA WIUWIUWIUWIUWIUWIUWIUWIUWIU\033[m")
    break

  print('''\033[31mCANTADAS SOBRE:
[ 1 ] SEM ÁREA ESPECÍFICA
[ 2 ] TECNOLOGIA
[ 3 ] QUÍMICA
[ 4 ] HISTÓRIA
[ 5 ] FILOSOFIA
[ 6 ] FÍSICA\033[m''')

  #LISTAS
  bdCantadas.lista_Sem_Área_Específica
  bdCantadas.lista_tecnologia
  bdCantadas.lista_Química
  bdCantadas.lista_História
  bdCantadas.lista_Filosofia
  bdCantadas.lista_Física

  escolhaU = int(input("Escolha: "))

  while True:
    
    if escolhaU == 1 or escolhaU == 2 or escolhaU == 3 or escolhaU == 4 or escolhaU == 5 or escolhaU == 6:
      break
    
    else:
      print('\033[31mESCOLHA UM NÚMERO ENTRE 1 E 6\033[m')
      escolhaU = int(input('Escolha:'))

  # PROCESSAMENTO 3
  if escolhaU == 1:  # SEM ÁREA ESPECÍFICA
    print(choice(bdCantadas.lista_Sem_Área_Específica))

  #  PROCESSAMENTO 4
  if escolhaU == 2:  # TECNOLOGIA
    print(choice(bdCantadas.lista_tecnologia))

  # PROCESSAMENTO 5
  if escolhaU == 3:  # QUÍMICA
    choice(bdCantadas.lista_Química)

  # PROCESSAMENTO 6
  if escolhaU == 4:  # HISTÓRIA
    print(choice(bdCantadas.lista_História))

  # PROCESSAMENTO 7
  if escolhaU == 5:  # FILOSOFIA
    print(choice(bdCantadas.lista_Filosofia))

  # PROCESSAMENTO 8
  if escolhaU == 6:  # FÍSICA
    print(choice(bdCantadas.lista_Física))

  while True:
    continuidade = ' '
    continuidade = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if continuidade in 'SN':
      break
    print('ERRO! Por Favor, digite apenas [S] ou [N].')
  
  if continuidade == 'N':
    print("FIM DO PROGRAMA")
    break