#!/usr/bin/env python

"""
    @objective = O bot tem por objetivo acessar o site da TOTVS Carol e emitir o relatório de funcionários. Além disso também fica responsável por
    tratar os dados e enviar para o DB, afim de emitir uma mensagem de alerta.
    ...
    @author = Mateus Santos de Jesus
    @regional = RBS
    @copyright = Copyright 2023
    @version = 1.0
    @email = mateussj305@gmail.com
    @status = Bot automatizado
"""

#Importa as bibliotecas que serão utilizadas:
import pandas as pd
import numpy as np
import datetime as dt
from datetime import date

#Variáveis:
cont = 0

#Lê o arquivo CSV:
df_dados = pd.read_csv('./arquivo.csv', low_memory=False)

#Delimita o campo "eventdatestr" em duas colunas e em um data frame separado: 
df_dados_merge = df_dados['eventdatestr'].astype(str).str.split('[T\.|]', expand=True)
df_dados_merge = df_dados_merge.drop(columns=[2])

#Faz a ánalise dos elementos e exclui todas as colunas que não serão utilizadas:
df_dados = df_dados.drop(columns=["image","devicecode","imei","appname","piscode","devicedescription","datetimeprovider", "mdmeventdate", "coordinates","coordinatesaccuracy","isuserinsidegeofenceenum","supervisorcode","nsrcode","mdmphonenumber","clockinmode","selfclockin","locationcode","imagehash","locationdescription","smssent","receiptimage","supervisorname","eventdatestr","gmt","updatedatetimeautomatically","diffgpsdevicetime","lastmomentgpsdatetimeobtained","lastgpsdatetime","devicesynchistorycode","mdmemailaddress","receiptsentmode","readphonestateenabled","fakegpslocation","clockineventtypegroupname","clockineventtypename","clockineventtypelabel","mdmtaxid","score","datetimechanged","externalservicestatuscode","sectioncode","costcentercode","has_receiptimage","empty_mdmeventdate","has_image","offset_statusanalysisdate","offset_mdmeventdate","empty_smssent","offset_smssent","empty_statusanalysisdate","nsrprocesseddatetime","offset_nsrprocesseddatetime","empty_nsrprocesseddatetime","georeferencestate","employeegeofencecoordinatesoptional","clockinsessionstatus","fraudscore","statusanalysis","statusanalysisdate","collectiveagreement"])

#Faz a concatenção dos dataframes df_dados e df_dados_merge:
df_table = pd.concat([df_dados, df_dados_merge], axis=1, join='inner')

#Renomeia as colunas:
df_table = df_table.rename(columns={"mdmname": "NOME", "mdmpersonid": "CPF", 0: "DATA", 1: "HORA BATIDA"}) 

#Adiciona novas colunas que serão usadas:
df_table = df_table.reindex(columns = df_table.columns.tolist() + ["ENTRADA EXPEDIENTE", "ENTRADA ALMOÇO", "SAIDA ALMOÇO", "SAIDA EXPEDIENTE"])

#Exclui caracteres indesejados e coloca tudo minusculo:
for i in df_table.columns:
    df_table[i] = df_table[i].astype(str).str.replace('\"', '')
    df_table[i] = df_table[i].astype(str).str.lower()
  
print(df_table)

df_table.to_excel('./clockin.xlsx')






