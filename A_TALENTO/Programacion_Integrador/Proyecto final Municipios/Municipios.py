def ingresar_datos():
    municipios = []
    while True:
        codigo = int(input("Ingrese el código del municipio (0 para terminar): "))
        if codigo == 0:
            break
        nombre = input("Ingrese el nombre del municipio: ")
        hombres = int(input("Ingrese el número de habitantes hombres: "))
        mujeres = int(input("Ingrese el número de habitantes mujeres: "))
        clima = int(input("Ingrese el clima del municipio (1-cálido, 2-frío, 3-templado): "))
        
        municipio = {
            "codigo": codigo,
            "nombre": nombre,
            "hombres": hombres,
            "mujeres": mujeres,
            "clima": clima
        }
        municipios.append(municipio)
    return municipios

def municipio_mayor_mujeres(municipios):
    mayor_mujeres = max(municipios, key=lambda x: x["mujeres"])
    return mayor_mujeres["codigo"], mayor_mujeres["nombre"], mayor_mujeres["mujeres"]

def clima_mayor_hombres(municipios):
    climas = {1: 0, 2: 0, 3: 0}
    for municipio in municipios:
        climas[municipio["clima"]] += municipio["hombres"]
    mayor_clima = max(climas, key=climas.get)
    return mayor_clima

def total_habitantes(municipios):
    total = sum(municipio["hombres"] + municipio["mujeres"] for municipio in municipios)
    return total

def porcentaje_mujeres(municipios, total_habitantes):
    total_mujeres = sum(municipio["mujeres"] for municipio in municipios)
    porcentaje = (total_mujeres / total_habitantes) * 100
    return porcentaje

def main():
    municipios = ingresar_datos()
    if municipios:
        codigo, nombre, mujeres = municipio_mayor_mujeres(municipios)
        clima = clima_mayor_hombres(municipios)
        total_habs = total_habitantes(municipios)
        porcentaje_muj = porcentaje_mujeres(municipios, total_habs)

        print(f"1. Municipio con mayor número de mujeres: Código={codigo}, Nombre={nombre}, Cantidad={mujeres}")
        print(f"2. Clima en el que habita la mayor cantidad de hombres: {clima}")
        print(f"3. Total de habitantes del país: {total_habs}")
        print(f"4. Porcentaje total de mujeres en el país: {porcentaje_muj:.2f}%")
    else:
        print("No se ingresaron datos de municipios.")

if __name__ == "__main__":
    main()
