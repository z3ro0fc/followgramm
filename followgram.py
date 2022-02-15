import string, random
from colorama import Fore, init
import sys
import signal
init()
#$$
rojo = Fore.RED
violeta = Fore.MAGENTA
azul = Fore.BLUE
cyan = Fore.CYAN
verde = Fore.GREEN
amarillo = Fore.YELLOW

#portada
print(f"""
{violeta} 
░██████╗░██████╗░░█████╗░███╗░░░███╗
██╔════╝░██╔══██╗██╔══██╗████╗░████║
██║░░██╗░██████╔╝███████║██╔████╔██║
██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝ {violeta} 

{cyan} Creado Por Z3RO {cyan}
{violeta} Version 2.0 {vioketa}
{verde} telegram : @z3roofc""")

def seguidores():
    follow = input("coloca el usuario // ")
if not True:
    print('usuario incorrecto')
else:
  for i in range(1000):
      print(f"""{cyan}[{cyan} {amarillo}+{amarillo}{cyan}]{cyan}{verde} El bot se esta programando tardara 20 dias{verde}""")
      
      
      #reporte
      
def reportes():
    reporte = input("Coloca el usuario = ")
    if not True:
        print('usuario incorrecto')
else:
  for i in range(1000):
      print(f"""{cyan}[{cyan}{amarillo}+{amarillo}{cyan}]{cyan}{verde} REPORTANDO CUENTA ...{verde}""")
      
     #fuerzabruta
     
def fuerzabruta():
      password = input("coloca el correo")
       if not True:
           print("La contraseña tuene mas de 10 caracteres")
else:
  if __name__ == '__main__':
 
    rstr = random.choice(string.ascii_letters)
    print(rstr)
    
    #menu
  
def menu():
      print(""" - follow : da seguidores
      - report : reporta una cuenta
      - fuerzagram : obtiene la cintraseña de la cuenta""")
      
     #eleccion
     
      
      def eleccion():
    print(f"{verde}")
    opc = input(f" OPCION :")
    if opc == "followi":
        seguidores()
        eleccion()
    elif opc == "help":
        menu();
        eleccion()
    elif opc == "report":
        reportes()
        eleccion()
    elif opc == "fuerzagram":
       fuerzabruta()
        eleccion()
    else:
        print(f"""{rojo}
    ERROR 404 OPCIÓN INCORRECTA x_x 
        {verde}""")
        eleccion()
    
# inicio de tool
if __name__ == "__main__":
    portada()
    eleccion()
      
      
      
      
    
