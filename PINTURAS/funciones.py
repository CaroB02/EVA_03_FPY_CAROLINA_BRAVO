pinturas_creadas=[]
codigoo=380560


def Ver_pinturas():
    if not Ver_pinturas:
        print('No hay pinturas que mostrar\n')
    else:
        print('Estas son las pinturas',pinturas_creadas)


def Buscar_pintura():
    if not pinturas_creadas:
        print('NO AHI PINTURAS PARA BUSCAR\n')
    else:
        with open(pinturas_creadas, mode='r')as archivo:
             input('Escriba el nombre de la pintura',pinturas_creadas,archivo)
       


def Agregar_pinturas():
    codigo=('Ingresa el codigo')
    nombree=input('Ingresa el color de la pintura:\n')
    tipo=input('Ingresa el tipo de pintura (1.Acrilico\t 2.Látex)')
    pinturas_creada={'nombre' : nombree, 'tipo' : tipo, 'codigo':codigo+1}
    pinturas_creada.append(pinturas_creadas)
    return


def Eliminar_pintura():
    if not pinturas_creadas:
        print('NO HAY PINTURAS CREADAS!!!\n')
        return
    else:
        print('Que pinturas deseas eliminar',pinturas_creadas)
        pass
        print('PINTURA EIMINADA EXITOSAMENTE!\n')
        return


def Exportar_pintura_json():
    if not Exportar_pintura_json:
        print('NO HAY ARCHIVOS EXPORTADOS!!')
    else:
        nombre=input('Escribe el nombre de el archivo:\n'),nombre,'.+json'
        import json
        with open(pinturas_creadas,'x'):
            json.dump(pinturas_creadas)
            print('ARCHICO CREADO!!\n')
            
    

def Salir():
    print('Bueno Adios')
    exit()