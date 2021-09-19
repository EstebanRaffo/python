# Convertir diccionario a json
producto1 = {"nombre": "silla", "color": "blanco", "precio": 80}

import json

estructura_json = json.dumps(producto1)
print(estructura_json)

# Convertir json a diccionario

producto2 = json.loads(estructura_json)
print(producto2)