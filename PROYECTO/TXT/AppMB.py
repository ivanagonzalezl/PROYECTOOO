import requests
from ClientGeneral import ClientGeneral as general
from ClientVIP import ClientVIP as vip
from AppMA import AppMA
from Ticket import Ticket
from Race import Race

class AppMB:

    def __init__(self):
        self.entradas=[]
        self.aux_entradas=[]
        self.general=[]
        self.vip=[]
        self.races=[]
    
    def load_data(self):
    
        url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        response=requests.request("GET", url_races)
        
        for carrera in response.json():
            entrada= Ticket(carrera["name"],carrera["map"]["general"][0]*carrera["map"]["general"][1],carrera["map"]["vip"][0]*carrera["map"]["vip"][1])
            self.aux_entradas.append(entrada)
        
        print(self.aux_entradas)
    
    def from_api_to_txt(self):
        
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/"

        file_name="Ticket.txt"
        with open(directory+file_name, "w") as f:
            for entrada in self.aux_entradas:
                f.write(f"{entrada.race_name}, {entrada.general}, {entrada.vip}\n")
    

    def read_files(self):
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/"
        
        file_name="Ticket.txt"
        with open(directory+file_name) as f:
            for line in f:
                x=int(line.split(",")[1])
                y=int(line.split(",")[2])
                entrada= Ticket(line.split(",")[0],x,y)
                self.entradas.append(entrada)

    def ondulado(self):
        pass
    
    def regisgter(self):

        print("\nSelecciones la carrera a la que desea asistir: ")
        for i, race in enumerate(self.appa.races):
            print(f"{i+1}. {race.race_name}")

        option=input(">>> ")
        while not option.isnumeric() or int(option) not in range(len(self.appa.races)+1):
            option=("ERROR: Ingreso inválido, intente nuevamente: ")
        
        option=int(option)
        option-=1

        carrera=self.entradas[option].race_name

        for race in self.appa.races: #TODO AQUÍ ESTOY LLAMANDO A LA LISTA PERO CUANDO LA LLAMO ESTA VACÍA
            if race.race_name==carrera:
                if race.race_end==True:
                    print("Es carrera ya finalizó, no puede comprar más entradas.")
                elif race.race_end==False:
                    tipo=input("Ingrese el tipo de entradad que desea (G)eneral o (V)IP: ").capitalize()
                    while tipo!="G" and tipo!="V":
                        tipo=input("Ingreso inválido, escribe la letra G si desea una entrada general o la letra V si desea una entrada VIP: ")
                    if tipo=="G":
                        print(f"El número de entradas disponibles es de: {self.entradas[option].general}")
                        if self.entradas[option].general==0:
                            print("Lo sentimos, no hay entradas generales disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or int(num_entrada) not in range(self.entradas[option].general): #####
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            for i in range(num_entrada):
                                nombre=input("Ingrese su nombre: ")
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")
                                edad=input("Ingrese su edad: ")
                                while not edad.isnumeric() and int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")
                                cliente= general(nombre,cedula,edad,carrera,False,i)
                                self.general.append(cliente)
                    elif tipo=="V":
                        print(f"El número de entradas disponibles es de: {self.entradas[option].vip}")
                        if self.entradas[option].vip==0:
                            print("Lo sentimos, no hay entradas generales disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or int(num_entrada) not in range(self.entradas[option].general): #####
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            for i in range(num_entrada):
                                nombre=input("Ingrese su nombre: ")
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")
                                edad=input("Ingrese su edad: ")
                                while not edad.isnumeric() and int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")
                                cliente= vip(nombre,cedula,edad,carrera,False,i)
                                self.vip.append(cliente)


