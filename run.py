import os #utilizado para limpiar pantalla
import re #utilizado para funciones regex
menu = 0
#lista = [1,2,3,4,5]
#print(lista)
#lista.append([1,2,3,4,5])
#print(lista)
#print(lista[5])
pacientes = []
paciente = []
registro = []
registros = []

consulta_paciente = []
consulta_registro = []

def registrar_paciente():
  os.system('cls')
  titulo = 'Registrar Paciente\n'
  print(titulo.center(50, " ") )
  rut = int(input('Ingrese su Rut: '))
  rut_validacion = 'false'
  while rut_validacion == 'false':
    if rut >= 5000000 and rut <= 99999999:
      rut_validacion = 'true'
    else:
      print('Error al ingresar rut. Rut debe ser un número entero que se encuentre dentro del rango de 5000000 y 99999999')
      rut = int(input('Ingrese su Rut: '))
  nombre = input('Ingrese su Nombre: ')
  direccion = input('Ingrese su Dirección: ')
  correo = input('Ingrese su correo: ')
  correo_validacion = 'false'
  while correo_validacion == 'false':
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	    correo_validacion = 'true'
    else:
      print('Error al ingresar Correo (revise su formato, debe contener almenos un @).')
      correo = input('Ingrese su correo: ')
  edad = int(input('Ingrese su edad: '))
  edad_validacion = 'false'
  while edad_validacion == 'false':
    if edad >= 0 and edad <= 110:
      edad_validacion = 'true'
    else:
      print('Error al ingresar edad. Edad debe ser un número entero que se encuentre en el rango 0 y 110')
      edad = int(input('Ingrese su edad: '))
  sexo = input('Ingrese su sexo (F o M): ')
  sexo_validacion = 'false'
  while sexo_validacion == 'false':
    if sexo.lower() == 'f' or  sexo.lower() == 'm':
      sexo_validacion = 'true'
    else:
      print('Error al ingresar Sexo. Debe Ingresar F o M según corresponda.')
      sexo = input('Ingrese su sexo (F o M): ')
  ps = input('Ingrese su PS (FONASA o ISAPRE): ')
  ps_validacion = 'false'
  while ps_validacion == 'false':
    if ps == 'FONASA' or  ps == 'ISAPRE':
      ps_validacion = 'true'
    else:
      print('Error al ingresar PS. PS debe ser una cadena de caracteres que sólo acepta los valores “ISAPRE” y “FONASA”')
      ps = input('Ingrese su PS (FONASA o ISAPRE): ')
  paciente = [rut, nombre, direccion, correo, edad, sexo, ps]
  #print(paciente)
  pacientes.append(paciente)
  #print(pacientes)

  input('\nPresione la tecla "Enter" para continuar...')
  return
def atencion_paciente():
  os.system('cls')
  titulo = 'Atención Paciente\n'
  print(titulo.center(50, " ") )
  encontro_usuario = 'false'
  rut = int(input('Ingrese su Rut del paciente a buscar: '))
  while encontro_usuario == 'false':
    # === Prueba con datos ===
    #paciente_test1 = []
    #paciente_test2 = []
    #pacientes_test = []
    #paciente_test1 = [1644565, 'Pedro', 'Calle1', 'test@test.cl', 20, 'm', 'fonasa']
    #paciente_test2 = [6554446, 'Juan', 'Calle2', 'test2@test.cl', 23, 'm', 'fonasa']
    #pacientes_test.append(paciente_test1)
    #pacientes_test.append(paciente_test2)
    for paciente in pacientes:
      if rut == paciente[0]:
        #print(paciente)
        encontro_usuario = 'true'
        fecha = input('Ingrese Fecha: ')
        obs = input('Ingrese Observaciones de la visita: ')
        registro = [paciente[0], fecha, obs]
        registros.append(registro)

        #print(registros)
        input('\nPresione la tecla "Enter" para continuar...')
        return

    print('\nNo se encontró al paciente...\n')
    rut = int(input('Ingrese su Rut del paciente a buscar: '))
  return
def consultar_datos_paciente():
  os.system('cls')
  titulo = 'Consultar datos paciente\n'
  print(titulo.center(50, " ") )
  rut = int(input('Ingrese su Rut del paciente a buscar: '))
  encontro_usuario = 'false'
  while encontro_usuario == 'false':
    # === Prueba con datos ===
    #paciente_test1 = []
    #paciente_test2 = []
    #pacientes_test = []
    #paciente_test1 = [1644565, 'Pedro', 'Calle1', 'test@test.cl', 20, 'm', 'fonasa']
    #paciente_test2 = [6554446, 'Juan', 'Calle2', 'test2@test.cl', 23, 'm', 'fonasa']
    #pacientes_test.append(paciente_test1)
    #pacientes_test.append(paciente_test2)

    #registro_test1 = []
    #registro_test2 = []
    #registro_test3 = []
    #registros_test = []
    #registro_test1 = [1644565, '16-01-12', 'test']
    #registro_test2 = [6554446, '17-01-12', 'test']
    #registro_test3 = [1644565, '18-01-12', 'test2']
    #registros_test.append(registro_test1)
    #registros_test.append(registro_test2)
    #registros_test.append(registro_test3)

    for paciente in pacientes:
      if rut == paciente[0]:
        encontro_usuario = 'true'
        consulta_paciente = paciente

        for registro in registros:
          if rut == registro[0]:
            consulta_registro.append(registro)

      #print(consulta_paciente)
      #print(consulta_registro)

      subtitulo = '\nDatos del paciente\n'
      print(subtitulo.center(50, " ") )

      print('Rut: ' + str(consulta_paciente[0]))
      print('Nombre: ' + consulta_paciente[1])
      print('Dirección: ' + consulta_paciente[2])
      print('Correo: ' + consulta_paciente[3])
      print('Edad: ' + str(consulta_paciente[4]))
      if consulta_paciente[5].lower() == 'f':
        sexo_salida = 'Femenino'
      else:
        sexo_salida = 'Masculino'
      print('Sexo: ' + sexo_salida)
      print('Registros: ')
      count = 0
      for registro_unico in consulta_registro:
        count +=1
        print('========================================================')
        texto1 = 'Registro Número ' + str(count) + ':'
        texto2 = 'Fecha: ' + registro_unico[1]
        texto3 = 'Observaciones de la visita: ' + registro_unico[2]
        print(texto1.center(50, " ") )
        print(texto2.center(25, " ") )
        print(texto3.center(25, " ") )
      if count == 0:
        print('========================================================')
        texto1 = 'Sin registros'
        print(texto1.center(25, " ") )

      print('========================================================')
      print("PS:" + consulta_paciente[6])
      input('Presione la tecla "Enter" para continuar...')
      return

    print('\nNo se encontró al paciente...\n')
    rut = int(input('Ingrese su Rut del paciente a buscar: '))
  return

while (menu >= 0) and (menu <= 3):
    os.system('cls')
    titulo = 'Centro Médico DUOC\n'
    print(titulo.center(50, " ") )
    print('1) Registrar Paciente')
    print('2) Atención Paciente')
    print('3) Consultar Datos Paciente')
    print('4) Salir\n')
    menu = int(input('Ingrese su Respuesta: '))
    if menu == 1:
      registrar_paciente()
    if menu == 2:
      atencion_paciente()
    if menu == 3:
      consultar_datos_paciente()
print("Ha Salido del Sistema ")

