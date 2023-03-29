#!/usr/bin/env python

*** Comments ***
    @objective = O bot tem por objetivo acessar o site da TOTVS Carol e emitir o relatório de funcionários. Além disso também fica responsável por
    tratar os dados e enviar para o DB, afim de emitir uma mensagem de alerta.
    ...
    @author = Mateus Santos de Jesus
    @regional = RBS
    @copyright = Copyright 2023
    @version = 1.0
    @email = mateussj305@gmail.com
    @status = Bot automatizado


*** Settings ***
Library    SeleniumLibrary
Library    Process
Resource   credential_carol.robot

*** Variables ***
${input_email}        //*[@id="email"]
${input_password}     //*[@id="password"]
${button_submit}      //button[@class="gate-btn cw-btn-primary"]
${a_button}           //a[@aria-label="Explore (18)"]
${tbody_campo}        //tbody[@data-row-id="clockinrecords"] 
${button_subtle}      //button[@cwbtnicon="ellipsis"]
${button_option}      //button[@class="cw-list-option cw-list-option--position cw-list-option--p-right"]
${button_download}    //button[contains(text(),"CSV")]
${button_indicator}   //button[@class="icon-button ng-star-inserted cw-indicator"]
${a_view_all}         //a[@class="cw-btn-regular cw-btn--small"] 

*** Keywords ***
Abrir navegador e acessar o site:
    Open Browser    https://telemont.carol.ai/auth/login?logout=true&env=telemont    chrome

Preencher Campos:
    Sleep    2s
    Input Text    ${input_email}    ${email}       
    
    Sleep    2s
    
    Input Text    ${input_password}    ${password}    
    Sleep    2s

Clicar em submit:
    Click Element    ${button_submit}
    Sleep    20s

Clicar em elemento ancora:
    Click Element    ${a_button}
    Sleep    15s

Clicar em Clock In Records:
    Click element    ${tbody_campo}
    Sleep    5s

Clicar em button subtle:
    Click Element    ${button_subtle}
    sleep    2s             

Clicar em button option:
    Click Element    ${button_option}
    sleep    2s

Exportar arquivo:
    Click Element    ${button_download}
    sleep    2s

Abrir Notificacao:
    Click Element    ${button_indicator}
    sleep    1s

Clicar em visualizar tudo:
    Click Element    ${a_view_all}
    sleep    10s 

Executar arquivo de tratamento de dados:
    ${RESULT} =    Run Process    python    #dados.py
    Log    all output: ${RESULT.stdout}
    Should Not Contain    ${RESULT.stdout}    FAIL  

*** Test Cases ***
Cenário 1: Acessar TOTVS Carol e exportar a planilha
    #Abrir navegador e acessar o site:
    #Preencher Campos:
    #Clicar em submit:
    #Clicar em elemento ancora:
    #Clicar em Clock In Records:
    #Clicar em button subtle:
    #Clicar em button option:
    #Exportar arquivo:
    #Abrir Notificacao:
    #Clicar em visualizar tudo:
#Cenário 2: Baixar zip da planilha mais recente:
    
Cenário 3: Trata os dados e gera um xlsx
    Executar arquivo de tratamento de dados: 
