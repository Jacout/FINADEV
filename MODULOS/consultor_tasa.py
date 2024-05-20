import requests, json


url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF282/datos"
headers = {
    "Accept": "application/json",
    "Bmx-Token": "373edee917f4b5809fe997eeb4053b0e37ac53a194dcae884f692904adfea507",
}
archivo = open("token.txt","r")
token = archivo.read()

archivo.close()

r = requests.get(url,headers=headers)

# Verificar que la solicitud fue exitosa
if r.status_code == 200:
    data = r.json()
    # Save data to a file named `data.json`
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
    # Hacer algo con los datos
    print(data)
    
    for x,y in data.items():
        print(x,"-",y)
else:
    print(f"Error {r.status_code}: {r.reason}")


