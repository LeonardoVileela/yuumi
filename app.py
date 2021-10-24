# -*- coding: utf-8 -*-

import urllib.request
import re
from flask import Flask, request, jsonify, app
import nltk
import string
import spacy
from datetime import datetime
nltk.download('punkt')

spacy.cli.download("pt_core_news_sm")




# a base de dados se encontra online, aqui eu leio a base de dados de perguntas
perguntasWeb = ''
for line in urllib.request.urlopen("https://leonardovileela.github.io/perguntas.txt"):
    perguntasWeb = perguntasWeb + str(line.decode('utf-8'))

#conteudo textual fica na váriavel conteudo
conteudo = perguntasWeb

#coloco o conteudo em caixa baixa
conteudo = conteudo.lower()

#fatio o texto pelos pontos finais das frases
conteudo = conteudo.split('.')


# coloco o conteudo na minha lista de sentenças.
# e tiro a quebra de linha.
listaSentencas = list(map(lambda s: s.strip(), conteudo))

# agora vamos fazer uma lista com as intenções das sentenças.
# cada intenção terá um ID.
listaIntencoes= []

#range é -1
# intenção 1 Nome
for i in range(3): # 0 1 2
    listaIntencoes.append(1)

# intenção 2 idade
for i in range(4): # 3 4 5 6
    listaIntencoes.append(2)

# intenção 3 inglês
for i in range(8):
    listaIntencoes.append(3)

# intenção 4 se é humano
for i in range(4):
    listaIntencoes.append(4)

# intenção 5 proteção de dados
for i in range(4):
    listaIntencoes.append(5)

# intenção 6 perguntar quem é o criador
for i in range(5):
    listaIntencoes.append(6)

# intenção 7 perguntar idioma
for i in range(5):
    listaIntencoes.append(7)

# intenção 8 perguntar sobre mãe e pai
for i in range(4):
    listaIntencoes.append(8)

# intenção 9 perguntar onde mora
for i in range(4):
    listaIntencoes.append(9)

# intenção 10 perguntar quantas pessoas eu falo
for i in range(2):
    listaIntencoes.append(10)

# intenção 11 perguntar uma piada
for i in range(3):
    listaIntencoes.append(11)

# intenção 12 perguntar papai noel
for i in range(2):
    listaIntencoes.append(12)

# intenção 13 perguntar sobre filme
for i in range(6):
    listaIntencoes.append(13)

# intenção 14 perguntar sobre música
for i in range(9):
    listaIntencoes.append(14)

# intenção 15 deseja falar com um humano
for i in range(16):
    listaIntencoes.append(15)

# intenção 16 deseja saber o endereço
for i in range(19):
    listaIntencoes.append(16)

# intenção 17 deseja saber o site
for i in range(4):
    listaIntencoes.append(17)

# intenção 18 deseja saber o instagram
for i in range(8):
    listaIntencoes.append(18)

# intenção 19 deseja saber o telefone
for i in range(10):
    listaIntencoes.append(19)

# intenção 20 deseja saber o email
for i in range(12):
    listaIntencoes.append(20)

# intenção 21 deseja saber sobre emprego
for i in range(10):
    listaIntencoes.append(21)

# intenção 22 deseja saber sobre orçamento
for i in range(8):
    listaIntencoes.append(22)

# intenção 23 deseja saber de atendimento em outros estados
for i in range(45):
    listaIntencoes.append(23)

# intenção 24 deseja saber o hobby
for i in range(1):
    listaIntencoes.append(24)

# intenção 25 deseja saber o sexo
for i in range(2):
    listaIntencoes.append(25)

# intenção 26 deseja saber o portfolio
for i in range(8):
    listaIntencoes.append(26)

# intenção 27 deseja saber a cor favorita
for i in range(2):
    listaIntencoes.append(27)

# intenção 28 deseja saber a comida favorita
for i in range(3):
    listaIntencoes.append(28)

# intenção 29 deseja saber o esporte favorita
for i in range(4):
    listaIntencoes.append(29)

# intenção 30 deseja saber o tempo do projeto
for i in range(2):
    listaIntencoes.append(30)

# intenção 31 deseja saber os serviços
for i in range(2):
    listaIntencoes.append(31)

# intenção 32 deseja saber sobre a empresa
for i in range(4):
    listaIntencoes.append(32)

# intenção 33 deseja saber os valores Da empresa
for i in range(1):
    listaIntencoes.append(33)

# intenção 34 deseja saber a data
for i in range(3):
    listaIntencoes.append(34)

# intenção 35 deseja saber a hora
for i in range(4):
    listaIntencoes.append(35)

# intenção 36 deseja saber o dia da semana
for i in range(4):
    listaIntencoes.append(36)

# intenção 37 deseja saber o mês
for i in range(6):
    listaIntencoes.append(37)

# intenção 38 deseja saber o autocad
for i in range(4):
    listaIntencoes.append(38)

# intenção 39 saudação
for i in range(12):
    listaIntencoes.append(39)

# intenção 40 deseja saber base de silo
for i in range(6):
    listaIntencoes.append(40)

# intenção 41 deseja saber armazéns
for i in range(6):
    listaIntencoes.append(41)

# intenção 42 deseja saber moega
for i in range(4):
    listaIntencoes.append(42)

# intenção 43 deseja saber estruturas metálicas
for i in range(5):
    listaIntencoes.append(43)

# intenção 44 deseja saber instalações elétricas
for i in range(4):
    listaIntencoes.append(44)

# intenção 45 deseja saber bases de secadores
for i in range(4):
    listaIntencoes.append(45)

# intenção 46 deseja saber balança rodoviária
for i in range(4):
    listaIntencoes.append(46)

# intenção 47 deseja saber concreto armado
for i in range(2):
    listaIntencoes.append(47)

# intenção 48 deseja saber transporte de carga
for i in range(3):
    listaIntencoes.append(48)

# intenção 49 deseja saber prédios
for i in range(8):
    listaIntencoes.append(49)

# intenção 50 deseja saber apartamento
for i in range(4):
    listaIntencoes.append(50)

# intenção 51 deseja agendar reunião
for i in range(10):
    listaIntencoes.append(51)

# intenção 52 deseja analise do solo
for i in range(4):
    listaIntencoes.append(52)

# intenção 53 deseja terraplanagem
for i in range(4):
    listaIntencoes.append(53)

# intenção 54 deseja reforço solo
for i in range(8):
    listaIntencoes.append(54)

# intenção 55 deseja sabe sobre chuva
for i in range(9):
    listaIntencoes.append(55)

# intenção 56 deseja sabe financiamento
for i in range(13):
    listaIntencoes.append(56)


# agora vamos fazer um MAP, a key é a resposta, e o value é o ID da intenção
respostas = {}

# como estamos trabalhamos com dados em tempo real ,como data e hora
# temos a função adicionarRespostas para atualizar os dados
def adicionarRespostas():
    diaDaSemanaTest = datetime.today().weekday()

    diaDaSemana = ''
    if diaDaSemanaTest == 0:
        diaDaSemana = 'Segunda-Feira'
    elif diaDaSemanaTest == 1:
        diaDaSemana = 'Terça-feira'
    elif diaDaSemanaTest == 2:
        diaDaSemana = 'Quarta-feira'
    elif diaDaSemanaTest == 3:
        diaDaSemana = 'Quinta-Feira'
    elif diaDaSemanaTest == 4:
        diaDaSemana = 'Sexta-feira'
    elif diaDaSemanaTest == 5:
        diaDaSemana = 'Sábado'
    elif diaDaSemanaTest == 6:
        diaDaSemana = 'Domingo'

    mesTeste = datetime.today().date().month
    mesNumber = ''
    mes = ''
    if mesTeste == 1:
        mesNumber = '01'
        mes = 'Janeiro'
    elif mesTeste == 2:
        mesNumber = '02'
        mes = 'Fevereiro'
    elif mesTeste == 3:
        mesNumber = '03'
        mes = 'Março'
    elif mesTeste == 4:
        mesNumber = '04'
        mes = 'Abril'
    elif mesTeste == 5:
        mesNumber = '05'
        mes = 'Maio'
    elif mesTeste == 6:
        mesNumber = '06'
        mes = 'Junho'
    elif mesTeste == 7:
        mesNumber = '07'
        mes = 'Julho'
    elif mesTeste == 8:
        mesNumber = '08'
        mes = 'Agosto'
    elif mesTeste == 9:
        mesNumber = '09'
        mes = 'Setembro'
    elif mesTeste == 10:
        mesNumber = '10'
        mes = 'Outubro'
    elif mesTeste == 11:
        mesNumber = '11'
        mes = 'Novembro'
    elif mesTeste == 12:
        mesNumber = '12'
        mes = 'Dezembro'

    respostas["Meu nome é Yummi."] = 1
    respostas["Não tenho idade nem anos."] = 2
    respostas["Eu não falo inglês."] = 3
    respostas["Eu não sou um humano, sou um robô."] = 4
    respostas["Eu não armazeno nenhum dos seus dados."] = 5
    respostas["Quem me criou foi o Leonardo Vilela."] = 6
    respostas["Eu sei falar Português."] = 7
    respostas["Eu não tenho mãe nem pai, meu criador foi Leonardo Vilela."] = 8
    respostas["Eu moro no Brasil."] = 9
    respostas["Eu falo com várias pessoas ao mesmo tempo."] = 10
    respostas["Olhe essa piada, era uma vez um pintinho que se chama Relam, Toda vez que chovia, relam piava."] = 11
    respostas["Papai Noel existe sim."] = 12
    respostas["Meu filme favorito é Frozen. "] = 13
    respostas["Eu gosto de kpop."] = 14
    respostas["Se deseja atendimento humano, entre em contato pelo e-mail mvconstrucoesms@gmail.com ."] = 15
    respostas["Nosso endereço é Rua Leonel Velasco, 15 - Res. Oliveira. Campo Grande MS."] = 16
    respostas["Nosso site é o www.mvconstrucoesms.com.br ."] = 17
    respostas["Nosso instagram é o ."] = 18
    respostas["Nosso telefone de contato é o telefone: (67) 99960-2168."] = 19
    respostas["Nosso e-mail é o mvconstrucoesms@gmail.com ."] = 20
    respostas["Para se cadastrar a uma vaga de emprego, envie seu curriculum para o e-mail mvconstrucoesms@gmail.com ."] = 21
    respostas["Para fazer seu orçamento, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com ."] = 22
    respostas["Nós atendemos em todos os estados do país. Entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 23
    respostas["Meu hobby é ajudar as pessoas."] = 24
    respostas["Eu não sou homem nem mulher, sou um robô."] = 25
    respostas["Para ver nosso portfólio entre no site www.mvconstrucoesms.com.br ."] = 26
    respostas["Minha cor favorita é rosa."] = 27
    respostas["Gosto de chocolate."] = 28
    respostas["Meu esporte favorito é futebol."] = 29
    respostas["O tempo varia de construção para construção, pode entrar em contato pelo e-mail mvconstrucoesms@gmail.com e pedir seu orçamento."] = 30
    respostas["Executamos todos os tipos de bases de silos em concreto armado, fundo plano, elevados, totalmente perfurados, fundo cônico, moegas de grãos, armazéns e estruturas metálicas."] = 31
    respostas["A MV CONSTRUÇÕES oferece soluções diferenciadas no mercado da construção civil, buscando a satisfação de seus clientes e colaboradores fornecendo produtos e serviços de mão de obra com qualidade e segurança."] = 32
    respostas["Nossos maiores valores são: agilidade, comprometimento, credibilidade, flexibilidade, qualidade e preço justo."] = 33
    respostas["Data de hoje: " + ("0" + str(datetime.today().date().day), str(datetime.today().date().day))[datetime.today().date().day > 9] + "/" + str(mesNumber) + "/" + str(datetime.today().date().year)] = 34
    respostas["Agora são: " + str(datetime.today().time().hour) + ":" + str(datetime.today().time().minute)] = 35
    respostas[str(diaDaSemana)] = 36
    respostas[str(mes)] = 37
    respostas["Temos os melhores projetistas do país, para oferecer os melhores projetos CAD para você. Entre em contato pelo E-MAIL mvconstrucoesms@gmail.com com e receba seu orçamento."] = 38
    respostas["Olá, meu nome é Yuumi, estou aqui para te ajudar no que precisar."] = 39
    respostas["Nós construímos as melhores bases de silo do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 40
    respostas["Nós construímos os melhores armazéns do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 41
    respostas["Nós construímos as melhores moegas do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.come receba seu orçamento."] = 42
    respostas["Nós construímos as melhores estruturas metálicas do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.come receba seu orçamento."] = 43
    respostas["Nós temos as melhores instalações elétricas do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 44
    respostas["Nós construímos as melhores bases de secadores do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 45
    respostas["Nós construímos as melhores balanças rodoviárias do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com com e receba seu orçamento."] = 46
    respostas["Nós temos o melhor concreto armado do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 47
    respostas["Nós possuímos o melhor transporte de carga do país, entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 48
    respostas["Sinto muito, nós não construímos prédios, você pode ver mais informações sobre nosso trabalho em www.mvconstrucoesms.com.br."] = 49
    respostas["Sinto muito, nós não construímos apartamentos, você pode ver mais informações sobre nosso trabalho em www.mvconstrucoesms.com.br."] = 50
    respostas["Para agendar sua reunião, basta enviar um e-mail para mvconstrucoesms@gmail.com informando o melhor horário para você."] = 51
    respostas["Nossa empresa faz a melhor análise de solo do país, com entrega do laudo em até 7 dias úteis. Entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 52
    respostas["Temos o melhor serviço de terraplanagem, carga, descarga e compactação do material, incluídos no orçamento. O solo deve ser retirado do próprio local pertencente ao contratante em uma distância máxima de até 3 km. Entre em contato pelo E-MAIL mvconstrucoesms@gmail.com e receba seu orçamento."] = 53
    respostas["Nós trabalhamos com reforço de solo para faturamento o cliente conseguir aumentar a capacidade do silo, esse aumento depende do fabricante do equipamento. Para mais informações entre em contato pelo E-MAIL mvconstrucoesms@gmail.com."] = 54
    respostas["O período de chuva não atrapalha na entrega da unidade de armazenagem. Para mais informações entre em contato pelo E-MAIL mvconstrucoesms@gmail.com."] = 55
    respostas["Nós temos parceiros especialistas em financiamentos prontos para te ajudar. Para mais informações entre em contato pelo E-MAIL mvconstrucoesms@gmail.com ."] = 56


# carrega o space em português, o space mudou o pacote do português da versão 2 pra 3
# se estiver usando a versão 2 do spacy é spacy.load("pt")
# se não funcionar verificar sua versão na documentção oficial
naturalLanguageprocessing = spacy.load("pt_core_news_sm")

# remove as palavras que não dão sentido para frase
# stop word depende muito do contexto do chatbot
# pode fazer um 'set' manualmente com as palavras se fazer sentido pro contexto do chatbot
stopWord = spacy.lang.pt.stop_words.STOP_WORDS

# também é necessário remover pontuações do texto
# vamos utilizar string.punctuation para fazer isso
# string.punctuation

# nessa função vamos fazer um pré-processamento para remover coisas inúteis dos textos
# como Urls, espaços em brancos, stopwords e pontuação
def preprocessamento(texto):

    # remove qualquer tipo de URL dos textos
    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)

    # remove qualquer espaço em branco
    texto = re.sub(r" +", ' ', texto)

    # documento recebe o texto usando o spacy
    documento = naturalLanguageprocessing(texto)

    lista = []
    # esse for basicamente pega a raiz das palavras
    # como por exemplo transformar, navegando em navegar
    # faz esse processamento e joga na lista
    for token in documento:
        lista.append(token.lemma_)

    # agora é hora de tirar todas as stop words da lista
    # e tirar também todas as pontuações
    lista = [palavra for palavra in lista if palavra not in stopWord and palavra not in string.punctuation]

    # agora vamos juntar todos os elementos da lista e transformar em um texto de novo
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista


listaSentencasPreProcessadas = []

# Nesse FOR adicionamos todas as frases que estavam na listaSentencas
# em listaSentencasPreProcessadas só que com aquele processamento feito na função preprocessamento
for i in range(len(listaSentencas)):
    listaSentencasPreProcessadas.append((preprocessamento(listaSentencas[i])))


# para calcular o TF-IDF utilizaremos o TfidfVectorizer
# ele vai nos ajudar com os cálculos
from sklearn.feature_extraction.text import TfidfVectorizer


# para agilidade utilizaremos outro pacote do sklearn
from sklearn.metrics.pairwise import cosine_similarity


# nesse ChatBot utilizaremos uma estratégia diferente do Bag Of Words
# Utilizaremos TF-IDF (Term frequency - inverse document frequency)
# primeiro se calcula o Term frequency (TF): frequência da palavra no documento atual
# depois se calcula o Inverse document frequency (IDF): quão rara é a palavra nos documentos
# assim não temos só um calculo local como no bag of words, teremos também um calculo global.

def responder(respostaUsuario):
    respostaChatbot = ''
    # vamos adicionar a resposta do usuário no final
    # assim vamos poder fazer a comparação com todas as frases
    # depois retiramos essa frase da lista
    listaSentencasPreProcessadas.append(respostaUsuario)

    # inicializamos um objeto chamado tfidf do tipo TfidfVectorizer
    tfidf = TfidfVectorizer()

    # o fit_transform transforma todos os textos em uma matrix.
    # ele encontra todas as palavras únicas.
    # cada palavra recebe um ID, lembrando que aqui o algoritmo não entende as palavras
    # mas sim o número que está associado aquela palavra.
    palavrasMatrix = tfidf.fit_transform(listaSentencasPreProcessadas)

    # caso deseje ver o calculo do IDF utilize o código abaixo
    # print(vetorDePalavras.idf_)

    # caso deseje analisar os cálculos do TF-IDF.
    # vc pode analisar a matrix palavrasMatrix.
    # analise é feita utilizando o comando abaixo
    # print(palavrasMatrix.todense())

    # se deseja ver qual as medidas da matrix utilize o comando
    # print(palavrasMatrix.todense().shape)

    # agora vamos fazer o cálculo do Cosine similarity
    # para mais detalhes desse cálculo deixo um link abaixo
    # https://en.wikipedia.org/wiki/Cosine_similarity

    # aqui fazemos a comparação de uma frase dessa matrix com todas as frase
    # lembrando que quanto mais perto de 1 o valor, mais chance de ser a
    # frase que estamos buscando
    similaridade = cosine_similarity(palavrasMatrix[-1], palavrasMatrix)

    # ordena por tamanho do menor pro maior
    # e depois pega o maior valor
    indice = similaridade.argsort()[0][-2]

    # transforma de número simples para array
    vetorSimilar = similaridade.flatten()

    # ordena o vetor
    vetorSimilar.sort()

    # passa o indice da frase encontrada
    vetorEncontrado = vetorSimilar[-2]

    # agora temos que remover a frase do usuário da lista
    # para que seja possível fazer as próximas comparações
    del listaSentencasPreProcessadas[-1]

    # aqui verificamos se ele encontrou alguma coisa, se o valor será != de 0 ele encontrou
    # lembrando que a listaSentencas tem os índices iguais da listaSentencasPreProcessadas e listaIntencoes
    # assim que posso retornar a listaIntencoes key, já que é aonde se encontra as respostas
    if (vetorEncontrado == 0):
        respostaChatbot = respostaChatbot + 'Desculpe, mas não entendi!'
        return respostaChatbot
    else:
        # atualiza as respostas e limpando o map e adicionando de novo
        respostas.clear()
        adicionarRespostas()
        for key, value in respostas.items():
            if(value == listaIntencoes[indice]):
                respostaChatbot = key
        return respostaChatbot

    # como os cálculos foram feito pelo sklearn,
    # deixou um artigo abaixo com toda a explicação sobre TF - IDF
    # https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/


#continuar = True
#print('Olá, meu nome é Yuumi, sou sua assistente virtual, e estou aqui para te ajudar!')
#while (continuar == True):
    #  print('Usuário:')
  #texto_usuario = input()
  #texto_usuario = texto_usuario.lower()
  #if (texto_usuario != 'sair'):
    # print('Yuumi: ')
    #print(responder(preprocessamento(texto_usuario)))
    #else:
    #continuar = False
    #print('Yuumi: Até breve!')

app = Flask(__name__)

@app.route('/<string:txt>', methods = ['POST'])
def conversar(txt):
  texto_usuario = txt
  texto_usuario = texto_usuario.lower()
  if (texto_usuario != 'sair'):
    respostaAPI = responder(preprocessamento(texto_usuario))
  else:
    respostaAPI = 'Até breve!'

  response = jsonify({"resposta": respostaAPI})
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
