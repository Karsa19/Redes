from get_snmp import Snmp
from agent import Agent
import plot_rrd

agente = Agent()
s = Snmp()
r=0
while r!=5:
    print("<-------MONITOREO SNMP------> \n MENU \n1.Inicio \n2.Agregar dispositivo \n3.Eliminar dispositivo \n4.Reporte \n5.Salir")
    print("Ingrese el nuemero de opcion: ")
    res= input()
    r= int(res)

    if(res=='1'):
        pass

    elif(res=='2'):
        agente.add_Agent()

    elif(res=='3'):
        agente.delete_Agent()

    elif(res=='4'):
        pass
    elif(res=='5'):
        r=5

    else:
        print("Opcion no valida")
