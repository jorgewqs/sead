from django.shortcuts import render
from django.http import HttpResponse

import subprocess as sp

def home(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')

def teste(request, ipdvr):

    qton = 0
    qtof = 0

    # Descomentar a linha a baixo para usar o script no Linux
    #status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))

    status,result = sp.getstatusoutput("ping " + str(ipdvr) + " -n 1")

    if status == 0:
        msg = "[ ON-LINE ]"
        qton += 1
    else:
        msg = "[ OFF-LINE ]"
        qtof += 1

    return render(request, 'teste.html', {'msg': msg})

# TODO: Campus Farolândia
campus_forolandia = {'10.72.0.115':'Almoxarifado','10.80.0.75':'Biblioteca',}
'''teste("10.72.0.115","Almoxarifado     ")
teste("10.80.0.75 ","Biblioteca       ")
teste("10.70.0.88 ","Bloco A          ")
teste("10.71.0.22 ","Bloco B          ")
teste("10.72.0.140","Bloco C          ")
teste("10.73.0.51 ","Bloco D          ")
teste("10.73.0.73 ","Bloco D 02       ")
teste("10.74.0.25 ","Bloco E          ")
teste("10.75.0.24 ","Bloco F          ")
teste("10.76.0.57 ","Bloco G          ")
teste("10.76.0.55 ","Bloco G Salas    ")
teste("10.77.0.41 ","CCS              ")
teste("10.82.1.103","DAA              ")
teste("10.83.0.27 ","Estacio. Externo ")
teste("10.83.0.23 ","G3 Cont de Acesso")
teste("10.73.0.47 ","Gastronomia      ")
teste("10.85.0.25 ","Gráfica          ")
teste("10.78.0.21 ","ITP              ")
teste("10.79.0.42 ","Mini-Shopping    ")
teste("10.74.0.65 ","NUESC            ")
teste("10.72.0.141","Patrimonio       ")
teste("10.82.2.190","Portaria Norte   ")
teste("10.83.0.57 ","Port. Principal  ")
teste("10.82.3.13 ","Reitoria         ")'''
