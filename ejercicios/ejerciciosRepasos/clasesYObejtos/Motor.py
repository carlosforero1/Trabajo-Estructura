class motor:
    contador = 0
    def __init__(self):
        motor.contador += 1

    def tieneMotor(self):
        print("Este carro tiene motor")