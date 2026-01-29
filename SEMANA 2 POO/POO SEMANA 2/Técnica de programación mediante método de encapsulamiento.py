


class CuentaBancaria:
    def __init__(self, titular, saldo):
        # Atributos encapsulados
        self._titular = titular
        self._saldo = saldo

    # Getter para titular
    def get_titular(self):
        return self._titular

    # Setter para titular
    def set_titular(self, nuevo_titular):
        if len(nuevo_titular) > 1:
            self._titular = nuevo_titular

    # Getter para saldo
    def get_saldo(self):
        return self._saldo

    # Setter para saldo
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo


# Uso del encapsulamiento
cuenta = CuentaBancaria("Fabian", 500)

print("Titular:", cuenta.get_titular())
print("Saldo:", cuenta.get_saldo())

# Cambiando valores usando los setters
cuenta.set_titular("Fabian Guambuguete")
cuenta.set_saldo(750)

print("Nuevo titular:", cuenta.get_titular())
print("Nuevo saldo:", cuenta.get_saldo())