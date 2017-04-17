import lib_FAM as lib
clientes = lib.load_xl("clientes2.xlsx", "Hoja1", "A1:C1001")

def febrero(cliente):
    mes = cliente['Fecha'].split('-')
    if int(mes[1]) == 2:
        return '%s,%d' % (mes[1], cliente['Consumo'])
def marzo(cliente):
    mes = cliente['Fecha'].split('-')
    if int(mes[1]) == 3:
        return '%s,%d' % (mes[1], cliente['Consumo'])

enero = lib.data_map(clientes, lib.filtro)

print 'enero: \n',enero

febrero = lib.data_map(clientes, febrero)
#print febrero

marzo = lib.data_map(clientes, marzo)
#print marzo