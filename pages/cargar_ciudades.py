import streamlit as st
import pandas as pd
import requests

def cargar_ciudades():
    st.header("Cargar Ciudades en Bulk")
    
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Leer el archivo CSV
            df = pd.read_csv(uploaded_file)
            # Asegurarse de que el DataFrame tenga las columnas necesarias
            if 'nombre_ciudad' not in df.columns or 'departamento_id' not in df.columns:
                st.error("El archivo CSV debe contener columnas llamadas 'nombre_ciudad' y 'departamento_id'.")
                return
            
            # Cargar cada ciudad
            for index, row in df.iterrows():
                data = {
                    "nombre_ciudad": row['nombre_ciudad'],
                    "departamento_id": row['departamento_id']
                }
                response = requests.post("http://127.0.0.1:8000/ciudades/", json=data)
                if response.status_code == 201:
                    st.success(f"Ciudad '{row['nombre_ciudad']}' cargada con éxito.")
                else:
                    st.error(f"Error al cargar la ciudad '{row['nombre_ciudad']}'. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar las ciudades: {e}")
