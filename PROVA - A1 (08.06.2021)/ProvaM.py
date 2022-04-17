'''
Dadas as listas geradas no arquivo provaM.py, escolha 5 relatórios citados abaixo para enviar ao professor Douglas para ele conferir e assim atribuir a nota de sua avaliação!
Cada relatório vale 1,0 ponto 
1.	Relatório que mostre digitado uma UF mostre a quantidade que exista na lista 
2.	Relatório que ao digitar a UF mostre no nome antigo e o atual da cidade
3.	Relatório que ao digitar o código da Lei mostre a quantidade que exista na lista, caso o código digitado não exista mostrar a mensagem lei não encontrada.
4.	Relatório que exibam as cidades dada uma justificativa do evento ato.
5.	Relatório que exiba todas as informações de ao ser digitado a data da ocorrência.
6.	Relatório que ao digitar o ALT exiba a quantidade de ALT existentes bem como a sua lei, justificativa do evento e cidades correspondentes.
7.	Relatório que ao digitar um cod_uf mostre todos os dados correspondentes a este código.
Em seu programa deverá inserir os comentários onde você deverá citar quais foram os relatórios escolhidos.
Caso tenha mais de um relatório, será considerado somente os 5 primeiros relatórios inseridos no programa.
Lembretes:
len(rank) retorna o tamanho da lista
paises[0].upper() retorna o país em letra maiúscula
paises[0].lower() retorna o país em letra minúscula 
for i range(len(população)) efetua o loop pela quantidade de itens
Obs.: tome muito cuidado com a Endentação do seu código!!!!
Não altere qualquer dado dentro das listas
'''

UF=['SP','RJ','PE','BA','BA','BA','MG','RJ','SP','SP','SP','SC','SC','RS','RS','RS','GO','MT','PB','CE','SP','RN','PA','PE','PA','MG','PB','SP','PB','PB','PE','PE','TO','RJ','RJ','RS','MS','MT','RS','TO','PB','SC','SP','SP','PR','SC','BA','RN','MG','SP','BA','MG','SC','TO','PB','RJ','RO','PB','PI','PB','PB','BA','PE','RO','RO','AP','AP','PR','RS','AC','PR','PR','SC','SC','PB','PB','MG','MG','PE','SP','TO','MG','MG','PB','GO','SC','RJ','PE','MG','PR','RJ','MG','PR','RN','RJ','MG','SC','MG','MG','BA','PR','MT','PR','PR','MT','SP','SP','PE','PE','PE','PE','PE','PE','PE','PE']
COD_UF=[35,33,26,29,29,29,31,33,35,35,35,42,42,43,43,43,52,51,25,23,35,24,15,26,15,31,25,35,25,25,26,26,17,33,33,43,50,51,43,17,25,42,35,35,41,42,29,24,31,35,29,31,42,17,25,33,11,25,22,25,25,29,26,11,11,16,16,41,43,12,41,41,42,42,25,25,31,31,26,35,17,31,31,25,52,42,33,26,31,41,33,31,41,24,33,31,42,31,31,29,41,51,41,41,51,35,35,26,26,26,26,26,26,26,26]
COD_MUN=[50001,5901,13800,2054,17334,22250,47808,5901,6607,16101,22158,9607,16057,15503,22855,23770,20157,7008,12606,6306,30805,10306,6500,6903,2954,8909,15401,15004,13653,16409,1607,8503,20499,3807,5901,11718,609,5309,17103,6001,13968,12809,30607,30805,28625,13906,3300,12559,31802,39301,19504,51503,17204,13809,13927,233,1104,13158,7959,12754,16409,3300,2902,502,338,154,55,25555,2659,435,27882,28633,16255,2057,2607,5501,71501,53509,14303,20905,21000,2704,15201,700,8301,18756,3856,7901,53103,8601,1009,36603,22651,3251,1009,25507,5308,65206,53103,504,25456,7107,459,17255,7305,7803,43501,12604,13503,12604,13008,13503,13701,14006,13701]
ALT=[1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,1]
LEI=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,976,3170,73,15443,9691,2160,4954,0,18033,3516,14537,49,15,1,7,1865,1553,4088,0,0,0,3308,0,132,13068,117,117,14349,12852,22,7938,13823,2941,2325,12946,398,963,63,2825,747,17197,4912,14,28196,2449,1690,549,531,124,76,10272,9866,1063,10230,10164,8816,8593,5333,5529,10326,10504,85,55,1,9961,9960,0,10953,7649,16,4,388,8910,1371,9454,8542,5601,4559,9223,934,375,354,4483,8121,4637,7601,7580,4294,579,2334,1819,1770,952,952,952,952,952,235]
NOME_ANTERIOR=['São Luís do Paraitinga','Trajano de Morais','São Vicente Ferrer','Araças','Iuiú','Muquém de São Francisco','Passa-Vinte','Trajano de Moraes','Biritiba-Mirim','Florínia','Itaóca','Lauro Muller','São Cristovão do Sul','Restinga Seca','Vespasiano Correa','Westfalia','São Luíz do Norte','Poxoréo','Quixabá','Itapagé','Moji Mirim','Presidente Juscelino','Santa Isabel do Pará','Iguaraci','Eldorado dos Carajás','Brasópolis','Seridó','Embu','Santarém','Campo de Santana','Belém de São Francisco','Lagoa do Itaenga','São Valério da Natividade','Parati','Trajano de Morais','Maçambara','Amambaí','Luciára','Santana do Livramento','Couto de Magalhães','São Domingos de Pombal','Piçarras','Moji das Cruzes','Moji-Mirim','Vila Alta','Presidente Castelo Branco','Governador Lomanto Júnior','São Miguel de Touros','Itabirinha de Mantena','Piraçununga','Livramento do Brumado','Piuí','São Miguel D.Oeste','Mosquito','São Bento de Pombal','Armação de Búzios','Jamari','Santa Cecília do Umbuzeiro','Petrônio Portela','Assis Chateaubriand','Tacima','Barro Preto','Cabo','Cacaieiros','Vila Nova do Mamoré','Amapari','Água Branca do Amapari','São Manoel','Brochier do Maratá','Santa Rosa','Tunas','Vila Branca','São João','Barra do Sul','Boqueirão dos Cochos','Desterro de Malta','Vila Matias','Presidente Soares','Sítio dos Moreiras','Ipauçu','Taquarussu do Porto','André Fernandes','Cassiterita','Antenor Navarro','Galheiros','Tunas','Pati do Alferes','Jaboatão','Calambau','Goio-Erê','Campos dos Goitacazes','José de Melo','Rosário','Eduardo Gomes','Campos','Felisberto Caldeira','Fachinal dos Guedes','São Tomé das Letras','Presidente Bernardes','Água Quente','São José','Quatro Marcos','Altamira','Nova Prata','Rio Claro','Brodósqui','Ribeirão Vermelho do Sul','Caripós','Manissobal','Boa Vista','São Bento','Belmonte','São Lourenço','Serrinha','São Lourenço da Mata']
NOME_ATUAL=['São Luiz do Paraitinga','Trajano de Moraes','São Vicente Férrer','Araçás','Iuiu','Muquém do São Francisco','Passa Vinte','Trajano de Morais','Biritiba Mirim','Florínea','Itaoca','Lauro Müller','São Cristóvão do Sul','Restinga Sêca','Vespasiano Corrêa','Westfália','São Luiz do Norte','Poxoréu','Quixaba','Itapajé','Mogi Mirim','Serra Caiada','Santa Izabel do Pará','Iguaracy','Eldorado do Carajás','Brazópolis','São Vicente do Seridó','Embu das Artes','Joca Claudino','Tacima','Belém do São Francisco','Lagoa de Itaenga','São Valério','Paraty','Trajano de Moraes','Maçambará','Amambai','Luciara','Sant.Ana do Livramento','Couto Magalhães','São Domingos','Balneário Piçarras','Mogi das Cruzes','Moji Mirim','Alto Paraíso','Presidente Castello Branco','Barro Preto','São Miguel do Gostoso','Itabirinha','Pirassununga','Livramento de Nossa Senhora','Piumhi','São Miguel do Oeste','Palmeiras do Tocantins','São Bentinho','Armação dos Búzios','Itapuã do Oeste','Santa Cecília','Nova Santa Rita','Riachão do Bacamarte','Campo de Santana','Governador Lomanto Júnior','Cabo de Santo Agostinho','Novo Horizonte do Oeste','Nova Mamoré','Pedra Branca do Amapari','Serra do Navio','São Manoel do Paraná','Brochier','Santa Rosa do Purus','Tunas do Paraná','Doutor Ulysses','São João do Oeste','Balneário Barra do Sul','Igaracy','Vista Serrana','Mathias Lobato','Alto Jequitibá','Moreilândia','Ipaussu','Palmas','Cachoeira de Pajeú','Conceição da Barra de Minas','São João do Rio do Peixe','Divinópolis de Goiás','Tunápolis','Paty do Alferes','Jaboatão dos Guararapes','Presidente Bernardes','Goioerê','Campos dos Goytacazes','Nova União','Rosário do Ivaí','Parnamirim','Campos dos Goitacazes','São Gonçalo do Rio Preto','Faxinal dos Guedes','São Thomé das Letras','Calambau','Érico Cardoso','São José das Palmeiras','São José dos Quatro Marcos','Altamira do Paraná','Nova Prata do Iguaçu','São José do Rio Claro','Brodowski','Riversul','Santa Maria da Boa Vista','São José do Belmonte','Caripós','São Bento do Una','Manissobal','São Lourenço da Mata','Serrita','São Lourenço']
JUSTIFICATIVA_DO_EVENTO_ATO=['Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Ato Legal (mudança de grafia)','Correção Ortográfica (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)','Ato Legal (mudança de grafia)']
DATA_LEI=['05/06/2017','30/11/2016','','','01/07/1990','27/04/1990','','31/12/1990','17/08/1990','04/04/1990','28/01/1993','05/04/1990','21/06/1993','23/12/1989','27/12/1997','13/05/2016','13/05/2016','25/05/2005','05/05/1964','04/09/2015','09/06/2014','14/01/2013','10/01/1961','20/12/1963','17/10/2013','12/01/2009','09/01/1968','06/09/2011','09/11/2010','23/12/2009','04/04/2007','10/09/1968','14/12/2007','22/03/2007','25/03/2003','27/03/2007','27/03/2007','27/03/2007','13/12/1957','09/10/2006','17/03/2003','20/07/2004','09/09/2003','09/09/2003','18/02/2004','22/12/2003','21/05/2003','04/05/2001','11/01/2001','08/09/1999','14/05/1966','15/07/1998','22/05/1998','02/04/1998','10/12/1997','10/11/1997','24/10/1997','03/06/1997','21/05/1997','12/05/1997','01/10/1996','10/04/1967','19/05/1994','11/01/1994','17/12/1993','06/12/1993','22/06/1993','05/05/1993','22/04/1993','09/12/1992','07/12/1992','07/12/1992','06/10/1992','17/05/1992','07/01/1992','27/12/1991','21/12/1991','21/10/1991','03/06/1991','01/10/1990','01/01/1990','27/10/1989','27/10/1989','05/10/1989','14/07/1989','28/06/1989','02/06/1989','05/05/1989','07/01/1989','09/12/1988','24/10/1988','16/12/1987','06/08/1987','03/08/1987','16/10/1986','08/07/1986','24/03/1986','29/11/1985','01/10/1985','15/07/1985','04/07/1985','10/01/1984','15/06/1982','13/05/1982','19/05/1981','16/09/1980','16/04/1980','30/12/1953','07/12/1953','31/12/1943','31/12/1943','31/12/1943','31/12/1943','31/12/1943','09/12/1938']
DATA_OCORRENCIA=['05/06/2017','30/11/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','01/09/2016','13/05/2016','13/05/2016','13/05/2016','13/05/2016','29/10/2015','21/09/2015','08/09/2015','16/12/2014','25/02/2014','01/01/2014','31/12/2013','17/10/2013','14/08/2013','03/07/2013','12/09/2011','28/02/2011','14/04/2010','02/09/2009','16/06/2009','29/04/2009','04/04/2008','31/07/2007','27/03/2007','27/03/2007','27/03/2007','25/10/2006','09/10/2006','16/06/2006','04/04/2005','12/04/2004','17/03/2004','19/02/2004','22/12/2003','21/05/2003','04/05/2001','11/01/2001','08/09/1999','20/10/1998','15/07/1998','22/05/1998','02/04/1998','10/12/1997','10/11/1997','24/10/1997','03/06/1997','21/05/1997','12/05/1997','01/10/1996','02/08/1996','19/05/1994','11/01/1994','17/12/1993','06/12/1993','22/06/1993','05/05/1993','22/04/1993','09/12/1992','07/12/1992','07/12/1992','06/10/1992','17/05/1992','07/01/1992','27/12/1991','21/12/1991','21/10/1991','03/06/1991','01/10/1990','01/01/1990','27/10/1989','27/10/1989','06/10/1989','14/07/1989','28/06/1989','02/06/1989','05/05/1989','07/01/1989','09/12/1988','24/10/1988','16/12/1987','06/08/1987','03/08/1987','16/10/1986','08/07/1986','24/03/1986','29/11/1985','01/10/1985','15/07/1985','04/07/1985','10/01/1984','15/06/1982','13/05/1982','19/05/1981','16/09/1980','16/04/1980','30/12/1953','07/12/1953','31/12/1943','31/12/1943','31/12/1943','31/12/1943','31/12/1943','09/12/1938']

# Professor escolhi as questões 1,2,3,5 e 7

# Inicio da questão 1

# 1 - Relatório que mostre digitado uma UF mostre a quantidade que exista na lista

x = input('Digite uma UF de sua escolha: ')
qtd = 0

for i in range(len(UF)):
    if (UF[i]==x.upper()):
        qtd=qtd+1

print('A quantidade de',x,'que existe na lista UF é de: ',qtd)

# Fim da questão 1


# Inicio da questão 2

# 2 - Relatório que ao digitar a UF mostre no nome antigo e o atual da cidade

x = input('\n Digite uma UF: ')

for i in range(len(UF)):
    if (UF[i]==x.upper()):
        print('\n Nome atual da cidade: ',NOME_ATUAL[i],"\n" 'Nome anterior da cidade: ', NOME_ANTERIOR[i], '\n')

# Fim da questão 2


# Inicio da questão 3

# 3 - Relatório que ao digitar o código da Lei mostre a quantidade que exista na lista, caso o código digitado não exista mostrar a mensagem lei não encontrada.

cod=int(input('Digite um código da Lei: '))
qtd=0

for i in range(len(LEI)):
    if (LEI[i] == cod):
        qtd=qtd+1        
   
if qtd == 0:
    print("Lei não encontrada")
else:
    print(' A quantidade de vezes que o código da Lei ',cod,'Aparece na lista é: ',qtd,'vezes')

    
# Fim da questão 3


# Inicio da questão 5

# 5 - Relatório que exiba todas as informações de ao ser digitado a data da ocorrência.

x = input('\n Qual foi a data da ocorrência: ')

for i in range(len(DATA_OCORRENCIA)):
    if (DATA_OCORRENCIA[i] == x):
        print(UF[i], COD_UF[i], COD_MUN[i], ALT[i], LEI[i], NOME_ANTERIOR[i], NOME_ATUAL[i], JUSTIFICATIVA_DO_EVENTO_ATO[i], DATA_LEI[i], DATA_OCORRENCIA[i])

# Fim da questão 5


# Inicio da questão 7

# 7 - Relatório que ao digitar um cod_uf mostre todos os dados correspondentes a este código.

cod=int(input('\n Digite o código do UF desejado: '))

for i in range(len(COD_UF)):
        if (COD_UF[i]==cod):
            print(UF[i], COD_UF[i], COD_MUN[i], ALT[i], LEI[i], NOME_ANTERIOR[i], NOME_ATUAL[i], JUSTIFICATIVA_DO_EVENTO_ATO[i], DATA_LEI[i], DATA_OCORRENCIA[i])
        
# Fim da questão 7
