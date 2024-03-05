class Carro:
    def __init__(self, marca, modelo,motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor


    def arrenque(self):
        print("El coche de marca: " + self.marca + " y el modelo: " + self.modelo+ "esta arrancando")