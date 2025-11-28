import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):

    return kelvin -273.15



df_celsius = df.copy()

df_celsius['San diego']= df_celsius['San diego'].apply(kelvin_to_celsius)
df_celsius['Phoenix']= df_celsius['Phoenix'].apply(kelvin_to_celsius)
df_celsius['Toronto']= df_celsius['Toronto'].apply(kelvin_to_celsius)


df_celsius = df_celsius.round(2)

# Análisis para Phoenix

# 1. Día y hora de temperatura mínima en Phoenix
fecha_min = df_celsius['Phoenix'].idxmin()
print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min}")

# 2. Temperatura mínima en Phoenix
temp_min = df_celsius['Phoenix'].min()
print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min} °C")

# 3. Día y hora de temperatura máxima en Phoenix
fecha_max = df_celsius['Phoenix'].idxmax()
print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max}")

# 4. Temperatura máxima en Phoenix
temp_max = df_celsius['Phoenix'].max()
print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max} °C")

# 5. Temperatura promedio en Phoenix durante 2016
temp_promedio = df_celsius['Phoenix'].mean().round(2)
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_promedio} °C")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix', alpha=0.6)
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("data_celsius.csv")
