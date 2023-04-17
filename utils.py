from configs import *


#Gera o menuzinho maroto
#####################################################################
def gerar_botoes(categoria_menu):

    if categoria_menu == "listas_prontas":
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(
            InlineKeyboardButton("Lista Tutu - MPB", callback_data="consultarVideokeTutuMpb"),
            InlineKeyboardButton("Lista Tutu - Nacionais", callback_data="consultarVideokeTutuNacionais"),
            InlineKeyboardButton("Lista Tutu - Internacionais", callback_data="consultarVideokeTutuInternacionais"),
            InlineKeyboardButton("Lista Carol - Nacionais", callback_data="consultarVideokeCarolNacionais"),
            InlineKeyboardButton("Lista Carol - Internacionais", callback_data="consultarVideokeCarolInternacionais"),
        )

    if categoria_menu == "search":
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(
            InlineKeyboardButton("Buscar por nome de Artista", callback_data="buscarArtista"),
            InlineKeyboardButton("Buscar por nome de Canção", callback_data="buscarCancao"),
        )

    return markup
#####################################################################


#Funcao para fazer query em tabelas do BQ
#####################################################################
def envia_menu(message):
    bot.send_message(message.chat.id,"🔎 Faça buscas por Artista/Cancao 🔍",reply_markup=gerar_botoes("search"))
    bot.send_message(message.chat.id,"ou")
    bot.send_message(message.chat.id,"🎵 Selecione uma lista abaixo para continuar! 🎵",reply_markup=gerar_botoes("listas_prontas"))
#####################################################################


#Funcao para fazer query em tabelas do BQ
#####################################################################
def query_table(query):
    #encoding: utf-8
    #project_id gcp_credentials -- Já configuradas em configs.py
    """
    Requisita uma tabela do BigQuery | Realiza uma consulta

    Args:
        query (string): Consulta que será realizada no BigQuery
        project_id (string): Id do projeto a qual a tabela pertence
        gcp_credentials (client credentials object): Credenciais autenticadas da conta de servico
    Returns:
        dataframe: pandas dataframe com o retorno da consulta
    """
    print("-------------------------------------------")
    print("A funcao query_table foi chamada!")
    print(query)
    print("-------------------------------------------")

    df = pandas_gbq.read_gbq(query, project_id=project_id,credentials=scoped_credentials)
    return (df)
#####################################################################


#Função criada para enviar lista - Call
#####################################################################
def enviador_lista_call(call,lenListaFinalVideoke,listaFinalVideoke):

    table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])

    if lenListaFinalVideoke >=4095:
        print(f"Lista muito longa! {lenListaFinalVideoke}")
        quartoLista = len(listaFinalVideoke)//4
        metadeLista = quartoLista*2
        tresQuartosLista = quartoLista*3
        listaFinalVideokeParteUm = listaFinalVideoke[:quartoLista]
        #print(f"Tamanho da lista 1! {len(str(listaFinalVideokeParteUm))}")
        listaFinalVideokeParteDois = listaFinalVideoke[quartoLista:metadeLista]
        #print(f"Tamanho da lista 2! {len(str(listaFinalVideokeParteDois))}")
        listaFinalVideokeParteTres = listaFinalVideoke[metadeLista:tresQuartosLista]
        #print(f"Tamanho da lista 3! {len(str(listaFinalVideokeParteTres))}")
        listaFinalVideokeParteQuatro = listaFinalVideoke[tresQuartosLista:]
        #print(f"Tamanho da lista 4! {len(str(listaFinalVideokeParteQuatro))}")
        
        #Gera e envia a lista 1
        for Interprete, Nome, Codigo in listaFinalVideokeParteUm:
            table.add_row([Interprete, Nome, Codigo])
        bot.send_message(call.message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
        #Gera e envia a lista 2
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteDois:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(call.message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
        #Gera e envia a lista 3
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteTres:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(call.message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
        #Gera e envia a lista 4
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteQuatro:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(call.message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
    else:
        for Interprete, Nome, Codigo in listaFinalVideoke:
            table.add_row([Interprete, Nome, Codigo])
        bot.send_message(call.message.chat.id,f'<pre>{table}</pre>',parse_mode='html')        
#####################################################################


#Função criada para enviar lista - message
#####################################################################
def enviador_lista_message(message,lenListaFinalVideoke,listaFinalVideoke):

    table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])

    if lenListaFinalVideoke >=4095:
        print(f"Lista muito longa! {lenListaFinalVideoke}")
        quartoLista = len(listaFinalVideoke)//4
        metadeLista = quartoLista*2
        tresQuartosLista = quartoLista*3
        listaFinalVideokeParteUm = listaFinalVideoke[:quartoLista]
        #print(f"Tamanho da lista 1! {len(str(listaFinalVideokeParteUm))}")
        listaFinalVideokeParteDois = listaFinalVideoke[quartoLista:metadeLista]
        #print(f"Tamanho da lista 2! {len(str(listaFinalVideokeParteDois))}")
        listaFinalVideokeParteTres = listaFinalVideoke[metadeLista:tresQuartosLista]
        #print(f"Tamanho da lista 3! {len(str(listaFinalVideokeParteTres))}")
        listaFinalVideokeParteQuatro = listaFinalVideoke[tresQuartosLista:]
        #print(f"Tamanho da lista 4! {len(str(listaFinalVideokeParteQuatro))}")
        
        #Gera e envia a lista 1
        for Interprete, Nome, Codigo in listaFinalVideokeParteUm:
            table.add_row([Interprete, Nome, Codigo])
        bot.send_message(message.chat.id,f'<pre>{table}</pre>',parse_mode='html')

        #Gera e envia a lista 2
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteDois:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
        #Gera e envia a lista 3
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteTres:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
        #Gera e envia a lista 4
        table = pt.PrettyTable(['Interprete', 'Nome', 'Codigo'])
        for Interprete, Nome, Codigo in listaFinalVideokeParteQuatro:
            table.add_row([Interprete, Nome, Codigo])
        
        bot.send_message(message.chat.id,f'<pre>{table}</pre>',parse_mode='html')
    else:
        for Interprete, Nome, Codigo in listaFinalVideoke:
            table.add_row([Interprete, Nome, Codigo])
        bot.send_message(message.chat.id,f'<pre>{table}</pre>',parse_mode='html')        
#####################################################################