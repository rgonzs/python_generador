import argparse
import csv
from datetime import datetime


def save_to_file(dni, data):
    fecha = datetime.now().timestamp()
    fieldnames = data[0].keys()
    with open(f'{dni}_{fecha}.csv','w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames, delimiter=',', )
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        f.close()


def _filter_cheque_status(estado, row):
    if row['Estado'] == estado:
        print(row['Estado'] == estado)
        return row
    
    


def main(filename: str, dni: str, salida:str, estado_cheque:str ):
    datos = []
    datos_dni = []
    try:
        with open(filename, 'r') as f:
            csv_reader = csv.DictReader(f)

            # 1 era validacion
            for row in csv_reader:
                if f"{row['NroCheque']}-{row['NumeroCuentaOrigen']}-{row['DNI']}" not in datos:                    
                    datos.append(f"{row['NroCheque']}-{row['NumeroCuentaOrigen']}-{row['DNI']}")
                else:
                    print(f"ERROR: Cheque: {row['NroCheque']}, Nro Cuenta Origen: {row['NumeroCuentaOrigen']} DNI: {row['DNI']} se encuentra duplicado")
                    break
                if row['DNI'] == dni:
                    datos_dni.append(row)
                if estado_cheque:
                    datos_dni = list(filter(lambda row: _filter_cheque_status(estado_cheque, row), datos_dni))
            del datos
            if salida == 'PANTALLA':
                print(datos_dni)
            if salida == 'CSV':
                save_to_file(dni, datos_dni)

    except FileNotFoundError:
        print(f'El archivo con nombre no existe')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validador de cheques')
    parser.add_argument('-filename',
                        required=True,
                        help="Nombre del archivo a examinar")

    parser.add_argument('-dni',
                        required=True,
                        help='DNI del cliente que se busca')

    parser.add_argument('-salida',
                        required=True,
                        help='(Requerido) Tipo de salida: [ PANTALLA, CSV ]')

    parser.add_argument('-tipo_cheque',
                        required=True,
                        help='(Requerido) Tipo del cheque a listar: [ EMITIDO, DEPOSITADO ]')

    parser.add_argument('-estado_cheque', 
                        required=False,
                        help='(Opcional) Estado del cheque a buscar: [ PENDIENTE, APROBADO, RECHAZADO ]')

    parser.add_argument('-rango_fecha',
                        required=False,
                        help='(Opcional) Rango de fecha: xx-xx-xxxx:yy-yy-yyyy')

    args = parser.parse_args()
    main(args.filename, args.dni, args.salida, args.estado_cheque)
