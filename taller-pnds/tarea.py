from statistics import mean
import pandas as pd

#Cargar data frame tal como viene
df_temp=pd.read_csv("weather2012_d.csv",
                sep=',', 
                encoding='latin1',  #Lenguaje latin
                infer_datetime_format=True,
                dayfirst=True,
                parse_dates=['Fecha']) #Cambia a formato de fecha

#Ver informacion del dataframe
print(df_temp.info())

#Eliminar columna con datos nulos en el mismo dataset
df_temp.dropna(inplace=True,
)

#Eliminar datos duplicados
df_temp.drop_duplicates(inplace=True)


#Remover datos erroneos
df_temp['Fecha']=pd.to_datetime(df_temp['Fecha'])


df_temp.dropna(subset=['Fecha'],inplace=True)

#Copia del dataframe de las columnas 0 - 1 - 3 - 7
df_columns=df_temp.iloc[:,[0,1,3,7]]


#Promedio de la temperatura y promedio de la humedad relativa
df_copied_1= df_temp[['Pronostico', 'Temp (C)']].copy()     
df_pron_prom_temp = df_copied_1.groupby(['Pronostico']).aggregate(mean)


df_copied_2 = df_temp[['Pronostico', 'Hum Rel (%)']].copy()     
df_pron_prom_hum = df_copied_2.groupby(['Pronostico']).aggregate(mean)

print(df_pron_prom_temp)
print(df_pron_prom_hum)