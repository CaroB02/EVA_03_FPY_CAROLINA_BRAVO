from funciones import *



print('Bienvenido a Pinturas acrilicas Mandarina')

menu=['Ver pinturas',
      'Buscar pinturas',
      'Agregar pintura',
      'Eliminar pintura',
      'Exportar pintura',
      'Salir']

while True:
    for ind,opt in enumerate(menu):
        print(f'{ind + 1},{opt}') 
    ans=input('Opcion')
    if ans == '1':
        Ver_pinturas()
    elif ans =='2':
        Buscar_pintura()
    elif ans =='3':
        Agregar_pinturas()
    elif ans =='4':
        Eliminar_pintura()
    elif ans =='5':
        Exportar_pintura_json()
    elif ans =='6':
        Salir()
    else:
        print('ERROR OPCION NO VALIDA!!\n')

