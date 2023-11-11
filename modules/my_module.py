import pandas
import numpy
import time
import datetime
import distfit

# Read data from csv file
data = pandas.read_excel('data/base.xlsx')

# change Mes to int where Enero = 1, ... , Diciembre = 12
data['numMes'] = data['Mes'].replace(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                                      'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Create a Column with the day of the week, that is the first word in 'Dia'
data['numDiaSemana'] = data['Dia'].str.split(' ').str[0]
# Change DiaSemana to int where Lunes = 1, ... , Domingo = 7
data['numDiaSemana'] = data['numDiaSemana'].replace(['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
                                              [1, 2, 3, 4, 5, 6, 7])

# Create a column with the day of the month, that is the second word in 'Dia'
data['numDiaMes'] = data['Dia'].str.split(' ').str[1].astype(int)

# Change Llegada, Inicio Serv. and Fin Serv. to time, show only hours, minutes and seconds
data['Llegada'] = pandas.to_datetime(data['Llegada'].astype(str)).dt.time
data['Inicio Serv.'] = pandas.to_datetime(data['Inicio Serv.'].astype(str).apply(str)).dt.time
data['Fin Serv.'] = pandas.to_datetime(data['Fin Serv.'].astype(str).apply(str)).dt.time

# Create a column with the duration of the service
data['Duracion'] = pandas.to_datetime(data['Fin Serv.'].astype(str).apply(str)) - pandas.to_datetime(data['Inicio Serv.'].astype(str).apply(str))
# show only hours, minutes and seconds in Duracion
data['Duracion'] = data['Duracion'].astype(str).str.split(' ').str[2]

# Create a Column with numbers for TipoServ.
data['numTipoServ'] = data['TipoServ.'].replace(
    pandas.unique(data['TipoServ.']), 
    numpy.arange(len(pandas.unique(data['TipoServ.']))))

# Create a Column with numbers for Servidor
data['numServidor'] = data['Servidor'].replace(
    pandas.unique(data['Servidor']), 
    numpy.arange(len(pandas.unique(data['Servidor']))))

# Create a Column with numbers for Estado, 'Atendido' = 1, 'Pendiente' = 0, 'Abandono' = -1
data['numEstado'] = data['Estado'].replace(['Atendido', 'Pendiente', 'Abandono'], [1, 0, -1])

# Create a copy and erase the columns that are not numeric
data_num = data.copy()
data_num = data_num.drop(['Mes', 'Dia', 'TipoServ.', 'Servidor', 'Estado'], axis=1)
