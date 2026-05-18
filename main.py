##

##   ==============================
##    SUPERMERCADO PYTHON MARKET
##   ==============================
##   1. Cargar producto
##   2. Mostrar productos
##   3. Buscar producto por código
##   4. Ordenar productos por precio
##   5. Mostrar producto con menor stock
##   6. Calcular valor total del inventario
##   7. Salir


def verificarExistencia(codigo):
    prodExiste = False
    for posicion in range(len(productosNombres)):
        if productosCodigo[posicion].lower() == codigo.lower():
            prodExiste = True 
            break
    return prodExiste


productosCodigo = [
    'TLV',
    'LMP',
    'MIC',
    'MSE'
]
productosNombres = [
    'Televisor',
    'Lampara',
    'Microfono',
    'Mouse'
]
productosPrecios = [
    5500,
    7500,
    3500,
    4500
]
productosStock = [
    5,
    3,
    3,
    1
]


# 2026-Q1-P1-315-P1-PerezTomas

opcion = -1

while opcion != 7:

    print("==============================\n")
    print("SUPERMERCADO PYTHON MARKET\n")
    print("==============================\n")

    print("1. Cargar producto\n")
    print("2. Mostrar productos\n")
    print("3. Buscar producto por código\n")
    print("4. Ordenar productos por precio\n")
    print("5. Mostrar producto con menor stock\n")
    print("6. Calcular valor total del inventario\n")
    print("7. Salir\n")

    opcion= int(input("Ingrese la opción: "))


    match opcion:
        case 1:
            #Solicitar código, nombre, precio y stock. Validar código no repetido, precio mayor a cero y stock no negativo
            print("==============================\n")
            print("Agregar producto\n")
            print("==============================\n")

            codigoExiste = True
            while codigoExiste:
                codigoProd=input("Ingrese el Código del producto: ")

                codigoExiste = verificarExistencia(codigoProd)
                if codigoExiste:
                    print("Ese codigo de producto ya existe, cambialo.")

            nombreProd=input("Ingrese el Nombre del producto: ")
            precioProd = 0

            while precioProd <= 0:
                precioProd = float(input("Ingrese el Precio del producto: "))
                if precioProd <= 0:
                    print("El precio no puede ser 0 o menos, corregilo.")

            stockProd = -1
            while stockProd < 0:
                stockProd = int(input("Ingrese el Stock del producto: "))
                if stockProd <= 0:
                    print("El Stock no puede ser negativo, corregilo.")

            productosCodigo.append(codigoProd)
            productosNombres.append(nombreProd)
            productosPrecios.append(precioProd)
            productosStock.append(stockProd)

        case 2:
            # Mostrar todos los productos cargados de forma clara y ordenada

            print("==============================\n")
            print("Mostrar productos\n")
            print("==============================\n")

            for producto in range(len(productosCodigo)):
                print(f"Codigo del Producto: {productosCodigo[producto]}")
                print(f"Producto: {productosNombres[producto]}")
                print(f"Precio: {productosPrecios[producto]}")
                print(f"Stock: {productosStock[producto]}")
                print("==============================\n")
        
        case 3:
            print("==============================\n")
            print("Buscar producto\n")
            print("==============================\n")

            busquedaProd = input("Ingrese el código del producto a buscar: ")

            for producto in range(len(productosCodigo)):
                if busquedaProd.lower() == productosCodigo[producto].lower():
                    print(f"El producto que buscabas era: {productosNombres[producto]}")
                    founded= 1
            if founded != 1:
                print("No encontramos el Producto.")

        case 4:
            print("==============================\n")
            print("Productos ordenados correctamente\n")
            print("==============================\n")
            for posicion in range(1, len(productosPrecios)):
                for posicionSecundaria in range(0, len(productosPrecios) - 1):
                    if productosPrecios[posicionSecundaria] > productosPrecios[posicionSecundaria+1]:

                        auxCodigo = productosCodigo[posicionSecundaria]
                        productosCodigo[posicionSecundaria] = productosCodigo[posicionSecundaria+1]
                        productosCodigo[posicionSecundaria+1] = auxCodigo

                        auxPrecio = productosPrecios[posicionSecundaria]
                        productosPrecios[posicionSecundaria] = productosPrecios[posicionSecundaria+1]
                        productosPrecios[posicionSecundaria+1] = auxPrecio

                        auxStock = productosStock[posicionSecundaria]
                        productosStock[posicionSecundaria] = productosStock[posicionSecundaria+1]
                        productosStock[posicionSecundaria+1] = auxStock

                        auxNombre = productosNombres[posicionSecundaria]
                        productosNombres[posicionSecundaria] = productosNombres[posicionSecundaria+1]
                        productosNombres[posicionSecundaria+1] = auxNombre

            for producto in range(len(productosCodigo)):
                print(f"Codigo del Producto: {productosCodigo[producto]}")
                print(f"Producto: {productosNombres[producto]}")
                print(f"Precio: {productosPrecios[producto]}")
                print(f"Stock: {productosStock[producto]}")
                print("==============================\n")

        case 5:
            print("==============================\n")
            print("Producto con Menor Stock\n")
            print("==============================\n")

            posicion = -1
            for producto in range(len(productosPrecios)):
                posicion += 1
                if producto == 0:
                    posicionMenorStock = posicion
                    menorStock = productosStock[posicion]
                
                if posicion > 0:
                    if productosStock[posicion] < menorStock:
                        menorStock = productosStock[posicion]
                        posicionMenorStock = posicion
            
            print(f"El producto con menor stock es: {productosNombres[posicionMenorStock]} - y su Stock es de: {menorStock}")

        case 6:
            ## Calcular valor total del inventario

            print("==============================\n")
            print("Valor total de nuestro inventario: \n")
            print("==============================\n")

            valorTotal = 0

            for posicion in range(len(productosPrecios)):
                valorTotal += int(productosPrecios[posicion])
            
            print(f"Valor total del inventario: {valorTotal}")

        case 7:

            print("==============================\n")
            print("¡Adios! \n")
            print("==============================\n")          

            opcion = 7

