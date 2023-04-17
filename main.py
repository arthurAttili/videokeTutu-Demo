from configs import *
from utils import *

from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['POST'])

def main():
    
    #Ações que devem ser realizadas pelos comandos
    #####################################################################

    #Videoke - Listas Prontas
    #############################
    def consultar_videoke(call,listaVideoke):
        bot.send_message(call.message.chat.id,'Você selecionou a opção Consultar Videokê Tutu! Baixando a lista do BQ...',parse_mode='html')
        bot.send_chat_action(call.message.chat.id,"typing")

        select = f"SELECT Interprete, Nome, Codigo FROM `videokebot.videoke.videoke` where {listaVideoke} = 'Sim' order by Interprete Asc, Nome Asc" 
        df_query = query_table(select)

        bot.send_chat_action(call.message.chat.id,"typing")

        listaFinalVideoke = df_query.values.tolist()
        lenListaFinalVideoke = len(str(listaFinalVideoke))

        enviador_lista_call(call,lenListaFinalVideoke,listaFinalVideoke)
    #############################


    #Videoke - Ferramenta de Busca
    #############################
    def buscador(call,tipoBusca):
        mensagemBot = bot.send_message(call.message.chat.id,'Você selecionou a opção por Busca! Por favor, digite o nome do Artista ou Canção',parse_mode='html')
        
        if tipoBusca == "Artista":
            bot.register_next_step_handler(mensagemBot, busca_handler_videoke_artista)
        else:
            bot.register_next_step_handler(mensagemBot, busca_handler_videoke_cancao)
    #############################



    #Handler para pegar o input do usuário - Artista
    #####################################################################
    def busca_handler_videoke_artista(message):
        busca = message.text.lower()

        bot.send_message(message.chat.id, f"Abrindo o livro do Videoke...")
        
        select = f"SELECT Interprete, Nome, Codigo FROM `videokebot.videoke.videoke` where REGEXP_CONTAINS(lower(Interprete),'{busca}') order by Interprete Asc, Nome Asc" 
        bot.send_chat_action(message.chat.id,"typing")
        df_query = query_table(select)
        listaFinalVideoke = df_query.values.tolist()
        lenListaFinalVideoke = len(str(listaFinalVideoke))
        enviador_lista_message(message,lenListaFinalVideoke,listaFinalVideoke)
    #####################################################################


    #Handler para pegar o input do usuário - Canção
    #####################################################################
    def busca_handler_videoke_cancao(message):
        busca = message.text.lower()

        bot.send_message(message.chat.id, f"Abrindo o livro do Videoke...")
        
        select = f"SELECT Interprete, Nome, Codigo FROM `videokebot.videoke.videoke` where REGEXP_CONTAINS(lower(Nome),'{busca}') order by Interprete Asc, Nome Asc" 
        bot.send_chat_action(message.chat.id,"typing")
        df_query = query_table(select)
        listaFinalVideoke = df_query.values.tolist()
        lenListaFinalVideoke = len(str(listaFinalVideoke))
        enviador_lista_message(message,lenListaFinalVideoke,listaFinalVideoke)
    #####################################################################


    #Acionador Inicial
    #####################################################################
    @bot.message_handler(content_types=["text"])
    def responder(message):
        print(message) #Útil para debugar
        if message.chat.id == USER_ID_1 or message.chat.id == USER_ID_2:
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            textoEntrada = f'Olá, <b>{first_name} {last_name}</b>! Bem vindo ao VideokêBot!'
            bot.reply_to(message,textoEntrada,parse_mode='html')
            
            envia_menu(message)
        else:
            texto = f"O seu id de usuário ({message.chat.id}) não é um id autorizado! Caso conheça o Tutu, mande este número para que ele te dê acesso."
            bot.reply_to(message,texto)
    #####################################################################


    #Acionador Funções
    #####################################################################
    @bot.callback_query_handler(func=lambda message: True)
    def callback_query(call):
        if call.data == "consultarVideokeTutuMpb":
            bot.answer_callback_query(call.id, "Consultar Videokê Tutu - MPB!")
            listaVideoke = "FavoritoTutuNacionalMPB"
            consultar_videoke(call,listaVideoke)

        if call.data == "consultarVideokeTutuNacionais":
            bot.answer_callback_query(call.id, "Consultar Videokê Tutu - Nacionais!")
            listaVideoke = "FavoritoTutuNacionalOutros"
            consultar_videoke(call,listaVideoke)

        if call.data == "consultarVideokeTutuInternacionais":
            bot.answer_callback_query(call.id, "Consultar Videokê Tutu - Internacionais!")
            listaVideoke = "FavoritoTutuInternacional"
            consultar_videoke(call,listaVideoke)

        if call.data == "consultarVideokeCarolNacionais":
            bot.answer_callback_query(call.id, "Consultar Videokê Carol - Nacionais!")
            listaVideoke = "FavoritoCarolNacional"
            consultar_videoke(call,listaVideoke)

        if call.data == "consultarVideokeCarolInternacionais":
            bot.answer_callback_query(call.id, "Consultar Videokê Carol - Internacionais!")
            listaVideoke = "FavoritoCarolInternacional"
            consultar_videoke(call,listaVideoke)

        if call.data == "buscarArtista":
            bot.answer_callback_query(call.id, "Você optou por Buscar Artista!")
            tipoBusca = "Artista"
            buscador(call,tipoBusca)

        if call.data == "buscarCancao":
            bot.answer_callback_query(call.id, "Você optou por Buscar Canção!")
            tipoBusca = "Cancao"
            buscador(call,tipoBusca)
    #####################################################################


    #Ativa o bot.
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)

    return "OK"

#Comente quando for subir pra núvem. Útil para testes locais.
print(main())