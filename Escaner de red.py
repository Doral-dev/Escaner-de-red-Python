

# Imprimo el titulo en pantalla

print(r"""

  _____                                     _                     _ 
 | ____|___  ___ __ _ _ __   ___ _ __    __| | ___   _ __ ___  __| |
 |  _| / __|/ __/ _` | '_ \ / _ \ '__|  / _` |/ _ \ | '__/ _ \/ _` |
 | |___\__ \ (_| (_| | | | |  __/ |    | (_| |  __/ | | |  __/ (_| |
 |_____|___/\___\__,_|_| |_|\___|_|     \__,_|\___| |_|  \___|\__,_|
                                                                    
""")



# Importo las librerias de python necesarias

import socket
import subprocess
import nmap
import time
import socket




# Defino esta variable global. Obtiene el nombre del host.
global nombre_host
nombre_host = socket.gethostname()



# Creo una funcion para automatizar la pregunta al usuario sobre si quiere detener el programa. Esto lo usare más adelante varias veces. Tenerlo en una funcion me simplifica su uso.
def quieres_parar():
    print("")
    quieres_parar = str(input("Quieres detener este programa? (s/n) -->"))
    print("")
    if quieres_parar == "s":
        quieres_parar = True
        exit()
    elif quieres_parar == "n":
        quieres_parar = False
        print("")
    else:
        print("")
        print("Opcion no valida. Tienes que escribir s o n.")




parar = False

# Mientras parar == False el programa ejecutará el bucle while infinitamente hasta que parar == True.
while parar == False:
  # Muestro las opciones al usuario
    print("")
    print("Esta herramienta cuenta con las siguientes opciones:")
    opciones = [
        "1.Obtener información de red del host",
        "2.Escanear puertos y servicios con nmap",
        "3.Mapeo de rutas con traceroute",
        "4.Descubrimiento de hosts en la red (ping sweeps)",
        "5.Detección de sistemas operativos en red",
        "6.Banner grabbing Services",
    ]

   # Para cada una de las opciones
    for opcion in opciones:
        print(opcion)

    # Le pido al usuario que elija una de ellas
    elegir_opcion = int(input("Elige una (1,2,3,4,5,6) --> "))
    print("")
  
   # Uso la funcionalidad match para ejecutar un bloque de código según la opcion que elija el usuario
    match elegir_opcion:

        # 1.Obtener informacion de red del host
        case 1:
            print("Recopilando información de red del host...")
            time.sleep(3)
            print(f"Nombre del host: {nombre_host}")
            print("")
            print("Ipconfig:")
            # Ejecuto un ipconfig con powershell
            ipconfig_resultado = subprocess.run(["powershell.exe", "ipconfig"])


            # Defino una lista de puertos
            puertos = [21, 22, 80, 443, 3306, 8080]
            print("")
            print("")
            print("Consultar la información de direcciones, familias de red e IPs asociadas a ese host a nivel de sistema/DNS: ")
            # Para cada uno de los puertos obtengo informacion
            for puerto in puertos:
                print("")
                print(f"Puerto {puerto} :")
                addr_info = socket.getaddrinfo(nombre_host, puerto)
                print(addr_info)
            quieres_parar()
            

        # 2.Escanear puertos y servicios con nmap
        case 2:
            print("Comenzando el escaneo de puertos de nmap...")
            time.sleep(3)
            try:
                nm = nmap.PortScanner()
                escaneo_puertos_nmap = nm.scan('127.0.0.1', '1-40043', timeout=50)
                print("")
                print(escaneo_puertos_nmap)
            except nmap.nmap.PortScannerTimeout:
                print("")
                print("Error: Se ha agotado el timeout de espera de Nmap. Vuelve a intentarlo o modifica su valor.")
            quieres_parar()


        # 3.Mapeo de rutas con traceroute
        case 3:
            print("Testeando las distintas rutas de red con traceroute...")
            time.sleep(3)
            test_traceroute = subprocess.run(["powershell.exe", "Test-NetConnection -TraceRoute"])
            print(test_traceroute)
            quieres_parar()


        # 4.Descubrimiento de hosts en la red (ping sweeps)
        case 4:
            print("4.Descubriendo hosts en la red...")
            time.sleep(3)
            descubrir_ips = subprocess.run(["powershell.exe", "Get-NetIPAddress -AddressFamily IPv4"])
            print(descubrir_ips)
            quieres_parar()

  
        # 5.Detección de sistemas operativos en red
        case 5:
            print("Detectando sistemas operativos en red con nmap...")
            time.sleep(3)
            try:
                nm = nmap.PortScanner()
                escaneo_os = nm.scan('127.0.0.1', arguments='-O')
                print("")
                print(escaneo_os)
            except Exception as e:
                print("")
                print(f"Error al detectar el sistema operativo: {e}")
            quieres_parar()


        # 6.Banner grabbing Services
        case 6:
            print("Iniciando Banner Grabbing...")
            time.sleep(3)
            ip_objetivo = input("Introduce la IP objetivo para el Banner Grabbing --> ")
            puerto_objetivo = int(input("Introduce el puerto (ej. 21, 80, 22) --> "))
            print("")
            
            try:
                s = socket.socket()
                s.settimeout(5)
                s.connect((ip_objetivo, puerto_objetivo))
                
                s.send(b'HEAD / HTTP/1.1\r\nHost: ' + ip_objetivo.encode() + b'\r\n\r\n')
                
                banner = s.recv(1024).decode(errors='ignore').strip()
                if banner:
                    print(f"Banner para {ip_objetivo}:{puerto_objetivo} -> \n{banner}")
                else:
                    print(f"El puerto {puerto_objetivo} no devolvió ningún banner.")
            except socket.error as e:
                print(f"Error de conexión con {ip_objetivo}:{puerto_objetivo} -> {e}")
            finally:
                s.close()
                
            quieres_parar()
                
                
        case _:
            print("Opción no válida. Vuelve a intentarlo.")

