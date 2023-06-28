import os
os.system("cls")

listaPrecio = []
listaNombre = []
listaCategoria = []
listaCodigo = []
listaStock = []

menu = """
------menu------
1. Registrar productos
2. Buscar productos
3. Listar Productos
4. salir

"""

def RegistraProducto ():
        
            while True:
                try:
                    cod = (int(input("ingrese codigo: ")))
                    if len(str(cod)) < 6 or len(str(cod)) > 6:
                        print("ocurrio una excepcion, ingrese denuevo el codigo ")
                    else:
                        listaCodigo.append(cod)
                        break
                except:
                    break
            while True:
                try:
                    nom = (int(input("ingrese nombre: ")))
                    if len(str(nom)) < 2 or len(str(nom)) > 50:
                            print("ocurrio una excepcion, ingrese denuevo el nombre ")
                    else:
                        listaNombre.append(nom)
                        break
                except:
                        break
                    
            while True:
                try:
                    cate = (int(input("ingrese categoria: ")))
                    if cate == "Paquete" or cate == "sobre":
                        listaCategoria.append(cate)
                        break
                except:
                    ("ocurrio una excepcion")
                    break
            while True:
                try:
                    pre = (int(input("ingrese valor: ")))
                    if len(str(pre)) < 0: 
                        print("ocurrio una excepcion, ingrese denuevo el valor")
                    else:
                        listaPrecio.append(pre)
                        break
                except:
                        print("ocurrio una excepcion")
                        break
            while True:
                try:
                    stock = (int(input("ingrese stock de producto: ")))
                    if len(str(stock)) < 0:
                        print("ocurrio una excepcion, stock debe ser positivo")
                    else:
                        listaStock.append(stock)
                        break
                except:
                    print("ocurrio una excepcion")
                    break
        
def BuscarProducto ():
     print("opcion 2")
     stock = input("ingrese codigo para buscar producto: ")
     print("listado segundo codigo: ")
     print("COD| NOMBRE| CATEGORIA|PRECIO|STOCK")

def ListarProducto():
        print("Listado")
        print("COD| NOMBRE| CATEGORIA|PRECIO|STOCK")
        for i in range (len(listaCodigo)):
            if listaStock[i] < 5 :
                stock = "SI"
            else:
                stock = "NO"
        print("---------------------------")
        print(f"{listaCodigo[i]:6d}|{listaNombre[i]:50s}{listaCategoria[i]:40s}{listaPrecio[i]:10d}{listaStock[i]:6d}")
        print("---------------------------")

while True :
        try:
            print(menu)
            opc = (int(input("digite una opcion: ")))
            if opc == 4:
                break
            elif opc == 1:
                RegistraProducto()
                
            elif opc == 3:
                ListarProducto()
                
        except:
            break

