from google.oauth2 import service_account
from google.cloud import bigquery
import os
import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import pandas as pd
import pandas_gbq
from logging.handlers import DEFAULT_SOAP_LOGGING_PORT
import requests
import prettytable as pt


#Autenticação ao Telegram
#####################################################################
CHAVE_API = "CHAVE_API_TELEGRAM"
bot = telebot.TeleBot(CHAVE_API)
USER_ID_1 = 123456789
USER_ID_2 = 123456789
#####################################################################


#Códigos de autenticação ao GCP
#####################################################################
#Útil para testes locais! Comente quando for upar na núvem!
caminho_arquivo_json = os.environ['GCP_SERVICE_ACCOUNT_VIDEOKEBOT'] 
with open(caminho_arquivo_json) as arquivo:
    private_key_json = json.loads(arquivo.read())

#Quando estiver na núvem, descomentar este abaixo e comentar as 3 linhas acima!
#private_key_json = json.loads(os.environ['GCP_SERVICE_ACCOUNT_VIDEOKEBOT'], strict= False)

credentials = service_account.Credentials.from_service_account_info(private_key_json)

scoped_credentials = credentials.with_scopes(
    [
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery",
        "https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/photoslibrary",
        "https://www.googleapis.com/auth/photoslibrary.readonly",
        "https://www.googleapis.com/auth/photoslibrary.sharing",
        "https://www.googleapis.com/auth/devstorage.read_write",
    ]
)

project_id = private_key_json['project_id']
#client = gspread.authorize(scoped_credentials)
#####################################################################