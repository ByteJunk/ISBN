import random
import time

def isbn10chksum(digits):
    sum_digits = 0
    for i in range (0, len(digits)):
        sum_digits += int(digits[i]) * (11-(i+1))
        mod1 = 11 - (sum_digits % 11)
    return mod1 % 11

def isbn13chksum(digits):
    sum_digits = 0
    for i in range (0, len(digits)):
        if i & 1:
            #print("Indice {}: digito {} vezes 3".format(i,digits[i]))
            sum_digits += int(digits[i]) * 3
        else:
            #print("Indice {}: digito {} vezes 1".format(i,digits[i]))
            sum_digits += int(digits[i])
    return (10 - (sum_digits % 10))

# Vamos gerar ambos para o mesmo "livro" 
isbn13 = ''
isbn10 = ''

# Inicializar coisas
gs1_prefix   = ["978", "979"]    #Aplicável ao ISBN13, é atualmente sempre um destes 2
lang_group   = [0,1,2,3,4,5,600,601,602,603,604,605,606,607,608,609,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,65,7,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,9915,9916,9917,9918,9919,9920,9921,9922,9923,9924,9925,9926,9927,9928,9929,9930,9931,9932,9933,9934,9935,9936,9937,9938,9939,9940,9941,9942,9943,9944,9945,9946,9947,9948,9949,9950,9951,9952,9953,9954,9955,9956,9957,9958,9959,9960,9961,9962,9963,9964,9965,9966,9967,9968,9970,9971,9972,9973,9974,9975,9976,9977,9978,9979,9980,9981,9982,9983,9984,9985,9986,9987,9988,9989,99901,99902,99903,99904,99905,99906,99908,99909,99910,99911,99912,99913,99914,99915,99916,99917,99918,99919,99920,99921,99922,99923,99924,99925,99926,99927,99928,99929,99930,99931,99932,99933,99934,99935,99936,99937,99938,99939,99940,99941,99942,99943,99944,99945,99946,99947,99948,99949,99950,99951,99952,99953,99954,99955,99956,99957,99958,99959,99960,99961,99962,99963,99964,99965,99966,99967,99968,99969,99970,99971,99972,99973,99974,99975,99976,99977,99978,99979,99980,99981,99982,99983] # lingua
lang_group   = [0, 1, 2, 3, 4, 5, 7, 65, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961]


# Escolher um prefixo ao acaso para o isbn13
grp_prefx = gs1_prefix[random.randint(0,1)]

# Escolher um "grupo de linguas" ao acaso da lista
grp_group = random.choice(lang_group)    

# Escolher um número aleatório para editora
maxlen_publi = 8 - len(str(grp_group))
len_publi = random.randint(1,maxlen_publi)
grp_publi = []
for x in range (0,len_publi):
    grp_publi.append(random.randint(0,9))
grp_publi = "".join(map(str, grp_publi))

# Escolher o título da obra conforme o que sobra
grp_title = []
for x in range (0, (maxlen_publi - len_publi + 1)):
    grp_title.append(random.randint(0,9))
grp_title = "".join(map(str, grp_title))


# Calcular controlo para ISBN10
grp_cntrl10 = isbn10chksum(str(grp_group) + str(grp_publi) + str(grp_title))
grp_cntrl13 = isbn13chksum(str(grp_prefx) + str(grp_group) + str(grp_publi) + str(grp_title))

# Mostrar os ISBNs
print("***** Novo livro inventado *****")
print("ISBN10: {}-{}-{}-{}".format(grp_group, grp_publi, grp_title, (grp_cntrl10 if grp_cntrl10 != 10 else "X")))
print("ISBN13: {}-{}-{}-{}-{}".format(grp_prefx, grp_group, grp_publi, grp_title, grp_cntrl13))