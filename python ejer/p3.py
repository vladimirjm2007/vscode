# Sistema de autenticación de empleados
def verificar_acceso(usuario, contrasena, es_admin):
    if usuario == "admin" and contrasena == "12345" or es_admin == True:
        return True
    else:
        return False

# Pruebas
usuarios = [
    {"usuario": "admin", "contrasena": "12345", "es_admin": True},
    {"usuario": "jefe", "contrasena": "pass", "es_admin": False},
    {"usuario": "invitado", "contrasena": "invitado", "es_admin": False}
]

for user in usuarios:
    acceso = verificar_acceso(user["usuario"], user["contrasena"], user["es_admin"])
    estado = "Acceso concedido" if acceso else "Acceso denegado"
    print(f"{user['usuario']}: {estado}")