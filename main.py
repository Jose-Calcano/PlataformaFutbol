import requests
import json
from partidos import *
from torneos import * 
import time
import os


url = "https://free-football-soccer-videos.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "14690e3474msh496212a9e1016cep1d0debjsn4bcb5c70b2b9",
    'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)


data = response.text
parsed = json.loads(data)
json.dumps(parsed, indent=4)


os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()


#Funcion para limpiar el archivo 'api.json' con el fin que la info de los partidos se actualice automaticamente y este al dia con la api
def limpieza_partidos():
  f = open('api.json', 'w')
  f.truncate(0)
  f.write('[]')
  f.close()


#Funcion que descarga la info de la API y la pone en api.json ordenada
def carga_partidos():

  with open("api.json", "r") as f:
    datas = json.loads(f.read())



  keys_bancos = parsed[0].keys()
  for keys_bancos in parsed[0].keys():
    print("\n")
    


  for i in range(len(parsed)):
    nombre_partido = parsed[i]['title']
    fecha_hora = parsed[i]['date']
    hora = fecha_hora[10:24]
    fecha = fecha_hora[0:10]
    url_thumbnail = parsed[i]['thumbnail']
    url = parsed[i]['url']
    competencia =  parsed[i]['competition']

    partidoRegistro = Partidos(nombre_partido, fecha_hora,fecha,hora, url_thumbnail,url,competencia)
    

    with open("api.json", "w", encoding='utf-8') as json_file:
     datas.append(partidoRegistro.asdict())
     json.dump(datas,json_file, indent = 8)
  
#Funcion que imprime los partidos del dia, filtrandolos usando la fecha de la computadora
def partidos_de_hoy():
  #Esto limpia la terminal
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  with open("api.json", "r") as f:
    datas = json.loads(f.read())
  fecha_hoy = time.strftime("%Y-%m-%d")
  time_hoy = time.strftime('T %H:%M:%S')
  print("\n")
  print("\n")
  print('Hoy es ' + fecha_hoy)
  print("\n")
  print("\n")
  print('Son las ' + time_hoy)
  for i in range(len(datas)):
    if datas[i]['fecha'] == fecha_hoy:
      nombre_partido = datas[i]['partido']
      hora = datas[i]['hora']
      fecha = datas[i]['fecha']
      url_thumbnail = datas[i]['url thumbnail']
      url = parsed[i]['url']
      print("\n")
      print(barras)
      print('Partido:  ' + nombre_partido)
      print('Fecha: ' + fecha)
      print('Hora: ' + hora)
      print('Url del thumbnail: ' + url_thumbnail)
      print('Url del partido: ' + url)
      print(barras)
  booleano = input('Desea volver al menu ? (Si o No):  ').capitalize()
  if booleano == 'Si':
    menu()
  elif booleano == 'No':
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    print(gracias_por)
    print(titulo)
    exit()

#Menu de inicio del programa
def menu():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print(titulo)
  print("\n")
  menu_inicio = """
  1.- Para ver los partidos del dia de hoy
  2.- Para ver los Torneos listados en la plataforma
  3.- Cerrar Programa
 """
  po = True;
  while po == True:
    print('Bienvenido a Saman Sport TV')
    print(menu_inicio)
    po = int(input("Por favor seleccione una entrada valida: "))
    if po == 1:
      partidos_de_hoy()
    elif po == 2:
      torneos()
    elif po == 3:
      exit()
    else:
      print(input("\n Por favor ingrese una entrada valida: "))
      menu()

#Filtro para colocar en torneos.json los torneos existentes en la API con su respectiva ID
def filtro_id_competencia():    
  with open("api.json", "r") as f:
    datas = json.loads(f.read())

  lista_id = []  
  for i in range(len(datas)):
    ids_competencias = datas[i]['competencia']['id']
    lista_id.append(ids_competencias)

  filtro = []
  for item in lista_id:
    if item not in filtro:
      filtro.append(item)
  filtro.sort()
  filtro_generador_de_torneos(filtro)

#Funcion que coloca todos los torneos en el archivo torneos.json 
def filtro_generador_de_torneos(filtro):
  d = open('torneos.json', 'w')
  d.truncate(0)
  d.write('[]')
  d.close()

  lista_id_torneos_2 = []
  filtro_2 = []

  with open("api.json", "r") as f:
    datas = json.loads(f.read())
  for i in range(len(filtro)):
    buscar_api = filtro[i]
    for b in range(len(datas)):
      if datas[b]['competencia']['id'] == buscar_api:
        nombre_torneo = datas[b]['competencia']['name']
        id_torneo_filtro = datas[b]['competencia']['id']


        lista_id_torneos_2.append(id_torneo_filtro)

        for item in lista_id_torneos_2:
         if item not in filtro_2:
          filtro_2.append(item)


          with open("torneos.json", "r") as h:
            file = json.loads(h.read())
            torneosRegistro = Torneos(id_torneo_filtro, nombre_torneo)
            with open("torneos.json", "w", encoding='utf-8') as json_file:
              file.append(torneosRegistro.asdicts())
              json.dump(file,json_file, indent = 8)
              
#Funcion que printea los torneos listados en la API y permite el input con el fin de poder imprimir los partidos de dicho torneo seleccionado
def torneos():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print('Estos son nuestros torneos disponibles actualmente: ')
  print("\n")
  with open("torneos.json", "r") as h:
    file = json.loads(h.read())
  with open("api.json", "r") as f:
    datas = json.loads(f.read())  
  for i in range(len(file)):
    print( 'Canal: ' + '(' + str(file[i]['id_torneo']) + ') ' +  file[i]['nombre_torneo'])
  print("\n")
  canal = input('Por favor escriba el numero del canal que desea ver, para ver los partidos de dicho torneo: ')
  for i in range(len(file)):
    if canal == str(file[i]['id_torneo']):
      for d in range(len(datas)):
        if canal == str(datas[d]['competencia']['id']):
          nombre_partido = datas[d]['partido']
          hora = datas[d]['hora']
          fecha = datas[d]['fecha']
          url_thumbnail = datas[d]['url thumbnail']
          url = parsed[d]['url']
          print("\n")
          print(barras)
          print('Partido:  ' + nombre_partido)
          print('Fecha: ' + fecha)
          print('Hora: ' + hora)
          print('Url del thumbnail: ' + url_thumbnail)
          print('Url del partido: ' + url)
          print(barras)
      break
  else:
      print('Por favor coloque una entrada valida')
      torneos()
  booleano = input('Desea volver al menu ? (Si o No):  ').capitalize()
  if booleano == 'Si':
    menu()
  elif booleano == 'No':
    booleano = input('Desea ver los partidos de otro torneo ? (Si o No):  ').capitalize()
    if booleano == 'Si':
      torneos()
    elif booleano == 'No':
      print(chr(27)+'[2j')
      print('\033c')
      print('\x1bc')
      print(gracias_por)
      print(titulo)
      exit()
  




def main():
  limpieza_partidos()
  carga_partidos()
  filtro_id_competencia()
  menu()



  
barras = '''
_____________________________________________________________________________________
'''

titulo = '''

   _____                                _____                  _     _________      __
  / ____|                              / ____|                | |   |__   __\ \    / /
 | (___   __ _ _ __ ___   __ _ _ __   | (___  _ __   ___  _ __| |_     | |   \ \  / / 
  \___ \ / _` | '_ ` _ \ / _` | '_ \   \___ \| '_ \ / _ \| '__| __|    | |    \ \/ /  
  ____) | (_| | | | | | | (_| | | | |  ____) | |_) | (_) | |  | |_     | |     \  /   
 |_____/ \__,_|_| |_| |_|\__,_|_| |_| |_____/| .__/ \___/|_|   \__|    |_|      \/    
                                             | |                                      
                                             |_|                                      
'''
gracias_por = '''

   _____                _                                                     
  / ____|              (_)                                                    
 | |  __ _ __ __ _  ___ _  __ _ ___   _ __   ___  _ __   _   _ ___  __ _ _ __ 
 | | |_ | '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__| | | | / __|/ _` | '__|
 | |__| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |    | |_| \__ \ (_| | |   
  \_____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|     \__,_|___/\__,_|_|   
                                     | |                                      
                                     |_|                                      
     
'''

main()