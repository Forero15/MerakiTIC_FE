import streamlit as st
import pandas as pd
import requests

def cargar_sedes():
    st.header("Cargar Sedes en Bulk")
    
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Leer el archivo CSV
            df = pd.read_csv(uploaded_file)
            # Asegurarse de que el DataFrame tenga las columnas necesarias
            required_columns = ['nombre_sede', 'email', 'numero_contacto', 'departamento_id', 'ciudad_id']
            if not all(col in df.columns for col in required_columns):
                st.error("El archivo CSV debe contener columnas llamadas 'nombre_sede', 'email', 'numero_contacto', 'departamento_id' y 'ciudad_id'.")
                return
            
            # Cargar cada sede
            for index, row in df.iterrows():
                data = {
                    "nombre_sede": row['nombre_sede'],
                    "email": row['email'],
                    "numero_contacto": row['numero_contacto'],
                    "departamento_id": row['departamento_id'],
                    "ciudad_id": row['ciudad_id']
                }
                response = requests.post("http://127.0.0.1:8000/sedes/", json=data)
                if response.status_code == 201:
                    st.success(f"Sede '{row['nombre_sede']}' cargada con éxito.")
                else:
                    st.error(f"Error al cargar la sede '{row['nombre_sede']}'. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar las sedes: {e}")
