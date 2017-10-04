#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Nome: SCANPY v1.1
# Descrição: Script que verifica a conectividade com os DVR.
# Autor: Jorge Wendell Queiros Santos
# Email: jorgewqs@gmail.com
# Criação: 06/03/2017

# TODO: Informações
__autor__ = "Jorge Wendell <jorgewqs@gmail.com>"
__copyright__ = "Copyright (c) 2017, JWQS"
__license__ = "GPL"

import subprocess as sp
import sys, os
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

now = datetime.now()
init()

# lambda Retorna uma função ao invés de atribuí-la à um nome como acontece com def
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
limpar()

print('''

          _|_|_|    _|_|_|    _|_|    _|      _|    _|_|    _|     _|
        _|        _|        _|    _|  _|_|    _|  _|    _|    _| _|
          _|_|    _|        _|_|_|_|  _|  _|  _|  _|_|_|       _|
              _|  _|        _|    _|  _|    _|_|  _|           _|
        _|_|_|      _|_|_|  _|    _|  _|      _|  _|           _|



                   SCANPY - Scanner para DVR em Python

[*] Nome: SCANPY v1.19092017
[*] Descrição: Script que verifica a conectividade com os DVR.
[*] Autor: Jorge Wendell Queiros Santos
[*] Email: jorgewqs@gmail.com
[+] Update: Ultimo update em 19/09/2017
[+] Comente: Atualização de IPs e ajustes de espaçamentos

                         Verificando conexões...

''')

qton = 0
qtof = 0


def ipcheck(ipdvr,ndvr):

    global qton
    global qtof

    # Descomentar a linha a baixo para usar o script no Linux
    #status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))

    status,result = sp.getstatusoutput("ping " + str(ipdvr) + " -n 1")

    hoje = "%s" % (time.strftime("%Y_%m_%d"))
    arquivo = open("log_dvr_%s.txt" % (hoje), "a")
    hora = time.strftime("%H:%M:%S")

    if status == 0:
        arquivo.write(ndvr + " | IP: " + str(ipdvr) + " | [ ON-LINE ] " + hora + " \r\n")
        arquivo.close()
        print(ndvr + " | IP: " + str(ipdvr) + " | " + Fore.WHITE + Back.GREEN + "[ ON-LINE ]" + Fore.RESET + Back.RESET)
        qton += 1
    else:
        arquivo.write(ndvr + " | IP: " + str(ipdvr) + " | [ OFF-LINE ] " + hora + " \r\n")
        arquivo.close()
        print(ndvr + " | IP: " + str(ipdvr) + " | " + Fore.WHITE + Back.RED + "[ OFF-LINE ]" + Fore.RESET + Back.RESET)
        qtof += 1

# TODO: Campus Farolândia
print("--| Campus Farolândia |"+"-"*41)
ipcheck("10.72.0.115","Almoxarifado     ")
ipcheck("10.80.0.75 ","Biblioteca       ")
ipcheck("10.70.0.88 ","Bloco A          ")
ipcheck("10.71.0.22 ","Bloco B          ")
ipcheck("10.72.0.140","Bloco C          ")
ipcheck("10.73.0.51 ","Bloco D          ")
ipcheck("10.73.0.73 ","Bloco D 02       ")
ipcheck("10.74.0.25 ","Bloco E          ")
ipcheck("10.75.0.24 ","Bloco F          ")
ipcheck("10.76.0.57 ","Bloco G          ")
ipcheck("10.76.0.55 ","Bloco G Salas    ")
ipcheck("10.77.0.41 ","CCS              ")
ipcheck("10.82.1.103","DAA              ")
ipcheck("10.83.0.27 ","Estacio. Externo ")
ipcheck("10.83.0.23 ","G3 Cont de Acesso")
ipcheck("10.73.0.47 ","Gastronomia      ")
ipcheck("10.85.0.25 ","Gráfica          ")
ipcheck("10.78.0.21 ","ITP              ")
ipcheck("10.79.0.42 ","Mini-Shopping    ")
ipcheck("10.74.0.65 ","NUESC            ")
ipcheck("10.72.0.141","Patrimonio       ")
ipcheck("10.82.2.190","Portaria Norte   ")
ipcheck("10.83.0.57 ","Port. Principal  ")
ipcheck("10.82.3.13 ","Reitoria         ")
print("-"*64)

# TODO: Campus Centro
print("--| Campus Centro |"+"-"*45)
ipcheck("10.10.0.47 ","DVR 01 DAA       ")
ipcheck("10.46.0.24 ","DVR 02           ")
print("-"*64)

# TODO: Campus Estância
print("--| Campus Estância |"+"-"*43)
ipcheck("10.153.0.46","DVR 01           ")
ipcheck("10.154.6.20","DVR Laboratório  ")
print("-"*64)

# TODO: Campus Itabaiana
print("--| Campus Itabaiana |"+"-"*42)
ipcheck("10.162.0.20","DVR 01           ")
print("-"*64)

# TODO: Campus Propria
print("--| Campus Propria |"+"-"*44)
ipcheck("10.182.0.32","DVR 01           ")
print("-"*64)

# TODO: Clinica Odontológica
print("--| Clinica Odontológica |"+"-"*38)
ipcheck("10.17.0.37 ","DVR 01           ")
ipcheck("10.17.0.32 ","DVR 02           ")
ipcheck("10.17.0.30 ","DVR 03           ")
ipcheck("10.17.0.44 ","DVR 04           ")
print("-"*64)

# TODO: Laboratorio Central
print("--| Laboratorio Central |"+"-"*39)
ipcheck("10.4.15.1 ","DVR 01            ")
print("-"*64)

# TODO: Ninota Garcia
print("--| Ninota Garcia |"+"-"*45)
ipcheck("10.20.0.61 ","Ninota Garcia 01 ")
ipcheck("10.20.0.59 ","Ninota Garcia 02 ")
print("-"*64)

# TODO: DeCos
print("--| DeCos |"+"-"*53)
ipcheck("10.222.0.26","DeCos 01         ")
ipcheck("10.222.0.27","DeCos 02         ")
ipcheck("10.222.0.28","DeCos 03         ")
ipcheck("10.222.0.29","DeCos 05         ")
print("-"*64)

# TODO: Campus Maceio
print("--| Campus Maceio |"+"-"*45)
ipcheck("10.211.180.3","DVR Biblioteca  ")
ipcheck("10.211.180.5","DVR Blc A 01    ")
ipcheck("10.211.180.6","DVR Blc A 02    ")
ipcheck("10.211.180.1","DVR Blc C 02    ")
ipcheck("10.211.180.8","DVR Blc C Andar ")
ipcheck("10.212.0.37 ","DVR Blc C       ")
ipcheck("10.211.180.2","DVR Blc D 01    ")
ipcheck("10.212.6.27 ","DVR Blc D 02    ")
ipcheck("10.211.180.4","DVR Catracas    ")
ipcheck("10.211.180.9","DVR Clinica     ")
ipcheck("10.211.180.7","DVR Laboratório ")
ipcheck("10.226.6.33 ","DVR Sala Innyx  ")
print("-"*64)

# TODO: Geras os resultados se ON-LINE ou OFF-LINE
print("="*64)
print("|  Data: %s-%s-%s" %(now.day, now.month, now.year))
print("|  Hora: %s:%s:%s" %(now.hour, now.minute, now.second))
print("|  %s DVRs estão " %qton + Fore.WHITE + Back.GREEN + "[ ON-LINE ]" + Fore.RESET + Back.RESET)
print("|  %s DVRs estão " %qtof + Fore.WHITE + Back.RED + "[ OFF-LINE ]" + Fore.RESET + Back.RESET)
print("="*64)

print("\n                         Verificação concluida !")