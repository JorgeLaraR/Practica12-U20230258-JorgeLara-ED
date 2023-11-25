class cadenaError(Exception):
    def _init_(self, mensaje="La cadena no debe estar vacia"):
        self.mensaje = mensaje
        super()._init_(self.mensaje)

def invertir_cadena(cadena):
    if not cadena:
        raise cadenaError()
    if len(cadena) == 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
try:
    cadena_original = "Hoy es un excelente dia"
    cadena_invertida = invertir_cadena(cadena_original)
    print("Cadena original:", cadena_original)
    print("Cadena invertida:", cadena_invertida)

except cadenaError as e:
    print("Error:", e)
except Exception as e:
    print("Error inesperado:", e)