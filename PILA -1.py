class Pila:
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)
        print(f'El elemento {dato} ha sido apilado')

    def pop(self):
        if not self.vacia():
            self.datos.pop()
            print('El elemento ha sido desapilado')
        else:
            print('La pila se encuentra vacía')

    def vacia(self):
        return len(self.datos) == 0

# Instanciar un objeto de la clase Pila
pila1 = Pila()
pila1.push('HELMER')
