#Armazena a mensagem em minusculo  
mensagem = str.lower(input("digite a mensagem a ser criptografada: "))

#Remove a pontuação
mensagem_Nopunctuation = ""
for character in mensagem:
    if character.isalnum():
        mensagem_Nopunctuation += character

#Remove caracteres especiais da mensagem
charEsp = "éãõâêôàçíúü"
charSemEsp = "eaoaeoaciuu"
for i in mensagem_Nopunctuation:
    if i in charEsp:
        mensagem_Nopunctuation = mensagem_Nopunctuation.replace(i, charSemEsp[charEsp.index(i)])

#Remove números
mensagem_final = ''.join(filter(lambda x: not x.isdigit(), mensagem_Nopunctuation))

#Armazena a variavel mensagem_final em msg.txt
arquivo = open("msg.txt", "w", encoding="utf-8")
arquivo.write(str(mensagem_final))
arquivo.close()

#Alfabetos e Rotores
AlfaL = "abcdefghijklmnopqrstuvwxyz"
R1 =    "zyxwvutsrqponmlkjihgfedcba"
R2 =    "mlkjihgfedcbazyxwvutsrqpon" 
R3 =    "nopqrstuvwxyzabcdefghijklm"
AlfaM = ["·-","-···","-·-·","-··","·","··-·","--·","····","··","·---","-·-","·-··","--","-·","---","·--·","--·-","·-·","···","-","··-","···-","·--","-··-","-·--","--··"]

#Maquina Enigma Remetente
criptR1 = []
for i in mensagem_final:
    criptR1.append(R1[AlfaL.index(i)])
print(criptR1)
criptR2 = []
for i in criptR1:
    criptR2.append(R2[R1.index(i)])
print(criptR2)
criptR3 = []
for i in criptR2:
    criptR3.append(R3[R2.index(i)])
print(criptR3)

#Transformação da lista criptografada para uma string
criptografia = "".join(map(str, criptR3))

#Criptografia para Morse 
Mcript = []
for i in criptografia:
    Mcript.append(AlfaM[AlfaL.index(i)])
print(Mcript)

#Armazena a variavel criptografia em cript.txt
arquivo = open("cript.txt", "w", encoding="utf-8")
arquivo.write(str(Mcript))
arquivo.close()

#Descriptografia do Morse 
DesMcript = []
for i in Mcript:
    DesMcript.append(AlfaL[AlfaM.index(i)])
print(DesMcript)
descriptografiaM = "".join(map(str, DesMcript))

#Maquina Enigma Destinatária 
descriptR1 = []
for i in descriptografiaM:
    descriptR1.append(R1[AlfaL.index(i)])
print(descriptR1)
descriptR2 = []
for i in descriptR1:
    descriptR2.append(R2[R1.index(i)])
print(descriptR2)
descriptR3 = []
for i in descriptR2:
    descriptR3.append(R3[R2.index(i)])
print(descriptR3)

#Transformação da lista descriptografada para uma string
descriptografia = "".join(map(str, descriptR3))

#Armazena a variavel descriptografia em descript.txt
arquivo = open("descript.txt", "w", encoding="utf-8")
arquivo.write(str(descriptografia))
arquivo.close()