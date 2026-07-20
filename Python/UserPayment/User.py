class User:

    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.limite_credito = 30000

        self.saldo_pagar = 0

    def hacer_compra(self, monto):

        self.saldo_pagar += monto
        return self

    def pagar_tarjeta(self, monto):

        self.saldo_pagar -= monto
        return self

    def mostrar_saldo_usuario(self):

        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar: ${self.saldo_pagar}")
        return self

    def transferir_deuda(self, otro_usuario, monto):

        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
        else:
            print("No hay suficiente deuda para transferir.")
        return self
    
usuario1 = User("A", "AA", "A@email.com")
usuario2 = User("B", "BB", "B@email.com")
usuario3 = User("C", "CC", "C@email.com")


usuario1.hacer_compra(5000).hacer_compra(7000).pagar_tarjeta(12000).mostrar_saldo_usuario()
usuario2.hacer_compra(10000).pagar_tarjeta(3000).pagar_tarjeta(2000).mostrar_saldo_usuario()
usuario3.hacer_compra(4000).hacer_compra(3000).hacer_compra(2000).pagar_tarjeta(1000).pagar_tarjeta(1000).pagar_tarjeta(1000).pagar_tarjeta(1000).mostrar_saldo_usuario()