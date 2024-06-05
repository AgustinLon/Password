password = input("Ingresa tu contraseña: ")

if len(password) < 8:
    print("La contraseña es muy corta.")
elif password == password.lower() or password == password.upper():
    print("La contraseña necesita al menos una letra mayúscula.")
elif not any(i.isdigit() for i in password):
    print("La contraseña necesita al menos un número.")
else:
    print("La contraseña es segura.")