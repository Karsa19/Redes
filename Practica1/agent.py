
class Agent:

    global f
    f = open ('agentes.txt','w')

    def __init__(self, ip='', v_snmp='', comunidad='', interfaz=''):
        self.ip = ip
        self.v_snmp = v_snmp
        self.comunidad = comunidad
        self.interfaz = interfaz

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip

    def set_v_snmp(self, v_snmp):
        self.v_snmp = v_snmp

    def get_v_snmp(self):
        return self.v_snmp

    def set_comunidad(self, comunidad):
        self.comunidad = comunidad

    def get_comunidad(self):
        return self.comunidad

    def set_interfaz(self, interfaz):
        self.interfaz = interfaz

    def get_interfaz(self):
        return self.interfaz

    def str_agent(self, a):
        f.write("IP: " + str(a.get_ip())+"\n")
        f.write("Version SNMP: " + str(a.get_v_snmp())+"\n")
        f.write("Comunidad: " + str(a.get_comunidad())+"\n")
        f.write("Interfaz: " + str(a.get_interfaz())+"\n")
        f.close()



    def delete_Agent(self, ip):
        pass

    def add_Agent(self):
        print("----Datos del Agente----")
        print("Ingrese IP: ")
        ip= input()
        print("Ingrese version SNMP: ")
        snmp= input()
        print("Ingrese comunidad: ")
        comunidad= input()
        print("Ingrese interfaz: ")
        interfaz= input()

        agt= Agent(ip,snmp,comunidad,interfaz)
        agt.str_agent(agt)
        

    def read_file(self):
        ip = f.readline().split(' ')

        
        



    


