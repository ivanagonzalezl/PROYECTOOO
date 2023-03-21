from AppMA import AppMA


class App():

    def __init__(self):

        self.appa=AppMA()

    def start(self):
        self.appa.read_files()
        


        while True:

                option=input("""

BIENVENIDO F1 2023
1. Descargar información de las Api.
2. Gestión de Carreras y Equipos.
3. Gestion de Ventas de Entrada.
4. Gestion de Asistencia a las Carreras.
5. Gestion de Restaurantes.
6. Gestion de Venta de Restaurantes.
7. Indicadores de Gestión.
8. Salir\n>>> """) #FALTA TÍTULO
                
                print()
                if option=="1":
                    self.appa.from_api_to_txt()
                    self.appa.load_data()
                elif option=="2":
                    self.appa.race_team_management()
                elif option=="3":
                    self.appa.regisgter()
                elif option=="4":
                    pass
                elif option=="5":
                    self.appa.search_pro()
                elif option=="6":
                    pass
                elif option=="7":
                    pass
                elif option=="8":
                    print("Usted ha salido del programa.")
                    break
                else:
                    print("Ingreso inválido. Intente otra vez.")
                print()

