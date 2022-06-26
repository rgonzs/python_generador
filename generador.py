import csv
from faker import Faker
import random
from datetime import datetime, timedelta

Faker.seed(0)
fake = Faker()

def generate_random_number(min, max):
    return random.randint(min, max)

def generate_nro_cheque(cantidad = 10):
    cheques = []
    for _ in range(1 , cantidad + 1):
        cheques.append(fake.swift11())
    return cheques

def generate_ammount():
    return round(random.random() * 1000, 2)
    
def generate_account_number():
    return fake.bban()

def generate_fecha_origen(days=60):
    antiguedad = timedelta(days=days)
    fecha = datetime.now() - antiguedad
    return fecha.timestamp()

def generate_fecha_pago(days=60):
    antiguedad = timedelta(days=days)
    fecha = datetime.now() + antiguedad
    return fecha.timestamp()

def generate_estado():
    estado = random.randint(0,2)
    if estado == 0:
        return 'rechazado'
    if estado == 1:
        return 'aceptado'
    if estado == 2:
        return 'pendiente'

if __name__ == '__main__':
    print('NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado')
    for _ in range(0, 100):
        dni = fake.ssn()
        cheques = generate_nro_cheque(20)
        bank = generate_random_number(1, 100)
        sucursal = generate_random_number(1, 300)
        numero_cuenta_origen = generate_account_number()
        numero_cuenta_destino = generate_account_number
        for cheque in cheques:
            fecha_origen = generate_fecha_origen(random.randint(30, 70))
            fecha_pago = generate_fecha_pago(random.randint(10, 30))
            valor = generate_ammount()
            estado = generate_estado()
            if random.randint(1, 20) == 10: 
                numero_cuenta_origen = generate_account_number()
            print(f'{cheque},{bank},{sucursal},{numero_cuenta_origen},{numero_cuenta_destino()},{valor},{fecha_origen},{fecha_pago},{dni},{estado}')
