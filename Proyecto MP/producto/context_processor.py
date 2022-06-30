import requests

def total_carrito(request):
    total=0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            acumulado = int(value["acumulado"])
            total += acumulado
    return {"total_carrito": str(total)}

def cantidad_carrito(request):
    total=0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            cantidad = int(value["cantidad"])
            total += cantidad
    return {"cantidad_carrito": str(total)}

def total_dolar(request):
    total = 0
    url = 'https://mindicador.cl/api/dolar/'
    response = requests.get(url)
    print(' status :' + str(response.status_code))
    datos = response.json()
    dolar_valor = datos['serie'][0]['valor']
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += round(int(value["acumulado"])/ int(dolar_valor),2)
    return {"total_carrito_dolar": total}