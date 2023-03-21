# map= {"general": [1, 6],
#       "vip": [5, 4]}

# matrizGeneral= []
# matrizVIP= []
# for tipo, entradas in map.items():
#     if tipo=="general":
#         filas=entradas[0]
#         columnas=entradas[1]
#         for f in range(filas):
#             matrizGeneral.append([])
#             for c in range(columnas):
#                 matrizGeneral[f].append(c+1)

#     elif tipo=="vip":
#         filas=entradas[0]
#         columnas=entradas[1]
#         for f in range(filas):
#             matrizVIP.append([])
#             for c in range(columnas):
#                 matrizVIP[f].append(c+1)

# # print(matrizGeneral)
# # print(matrizVIP)

# for fila in matrizVIP:
#     print (fila)

# # for i in range(filas):


# # for i in range(filas):
# #     matrizGeneral.append([])
# #     for j in range(columnas):
# #         puesto=x+1
# #         matrizGeneral[i].append(puesto)

# # print(matrizGeneral)

# import requests

# url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
# response=requests.request("GET", url_races)
        
# matriz_g=[]
# matriz_v=[]
# for carreras in response:
#     for key, value in carreras.items():
#         if key=="map":
#             for tipo, entradas in key.items():
#                 if tipo=="general":
#                     filas=entradas[0]
#                     columnas=entradas[1]
#                     for f in range(filas):
#                         matriz_g.append([])
#                         for c in range(columnas):
#                             matriz_g[f].append(c+1)
#                 elif tipo=="vip":
#                     filas=entradas[0]
#                     columnas=entradas[1]
#                     for f in range(filas):
#                         matriz_v.append([])
#                         for c in range(columnas):
#                             matriz_v[f].append(c+1)

# print(matriz_g)
# print(matriz_v)



x=int(input("Ingrese un númeoro: "))

