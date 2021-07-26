
# Importing Modules
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

print("Conecting to the DB")

#Change node and file with the correspondent ones
Node = "node_0"
File="covid_00.csv"

# Connect to Database
conn = psycopg2.connect(
host = "localhost",
port = 5432,
database = "covid_db",
user = "jason",
password = "jason")


# Cursor to use Database
cur = conn.cursor()


# ---
# ## Create Table and Copy CSV Partition


#conn.rollback()



# Create Table public.tbl_covid in covid_db 
ctbl_query = 'CREATE TABLE IF NOT EXISTS public.tbl_covid("FECHA_ACTUALIZACION" date,"ID_REGISTRO" character varying,"ORIGEN" integer,"SECTOR" integer,"ENTIDAD_UM" character varying,"SEXO" integer,"ENTIDAD_NAC" character varying,"ENTIDAD_RES" integer,"MUNICIPIO_RES" character varying,"TIPO_PACIENTE" integer,"FECHA_INGRESO" date,"FECHA_SINTOMAS" date,"FECHA_DEF" character varying,"INTUBADO" integer,"NEUMONIA" integer,"EDAD" integer,"NACIONALIDAD" integer,"EMBARAZO" integer,"HABLA_LENGUA_INDIG" integer,"INDIGENA" integer,"DIABETES" integer,"EPOC" integer,"ASMA" integer, "INMUSUPR" integer,"HIPERTENSION" integer,"OTRA_COM" integer,"CARDIOVASCULAR" integer,"OBESIDAD" integer,"RENAL_CRONICA" integer,"TABAQUISMO" integer,"OTRO_CASO" integer,"TOMA_MUESTRA_LAB" integer,"RESULTADO_LAB" integer,"TOMA_MUESTRA_ANTIGENO" integer,"RESULTADO_ANTIGENO" integer,"CLASIFICACION_FINAL" integer,"MIGRANTE" integer,"PAIS_NACIONALIDAD" character varying,"PAIS_ORIGEN" character varying,"UCI" integer );'
cur.execute(ctbl_query)
conn.commit()



print("Importing Data")

# Copy content of covid_01.csv into tbl_covid
cpy_query = "COPY public.tbl_covid FROM '/home/partition/" + File + "' " "WITH DELIMITER AS ',' CSV HEADER;"
cur.execute(cpy_query)
conn.commit()


# ---
# ## From Queries To Result DataFrame



#Useful Tools
Null_date = "'9999-99-99'"
list_s = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 
          'Chiapas', 'Chihuahua', 'Ciudad de México', 'Coahuila', 'Colima', 'Durango', 
          'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 
          'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 
          'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 
          'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']




# Query For Defunciones
def_query = 'SELECT "ENTIDAD_RES", COUNT("FECHA_DEF") AS "Defunciones_Totales" FROM public.tbl_covid WHERE "FECHA_DEF" != '+ Null_date +' GROUP BY "ENTIDAD_RES" ORDER BY "ENTIDAD_RES" LIMIT 40;'

# DataFrame for Defunciones
df_def = sqlio.read_sql_query(def_query, conn)



# Query For Casos Activos
ca_query = 'SELECT "ENTIDAD_RES", COUNT("CLASIFICACION_FINAL") AS "Casos_Activos" FROM public.tbl_covid WHERE "CLASIFICACION_FINAL" <= 3 AND "FECHA_DEF" = '+ Null_date + ' GROUP BY "ENTIDAD_RES" ORDER BY "ENTIDAD_RES" LIMIT 40;'

# DataFrame for Casos Activos
df_ca = sqlio.read_sql_query(ca_query, conn)




# Resulting DataFrame from Node 1
df_r = pd.DataFrame({"Estados":list_s, "Casos_activos_covid":df_ca["Casos_Activos"],
        "Defunciones":df_def["Defunciones_Totales"]})



print("Generating new file")

# Saving Result DataFrame into CSV File
df_r.to_csv('./processed/'+Node+'.csv')


# ---
# ## Drop Table and Close Connection




# Drop Table public.tbl_covid from covid_db 
cur.execute("DROP TABLE public.tbl_covid CASCADE;")
conn.commit()





# Closing Cursor to Database
cur.close()
conn.close()

print("Done")




