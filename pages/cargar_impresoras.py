import streamlit as st
import pandas as pd
import requests

def cargar_impresoras():
    st.header("Cargar Impresoras en Bulk")
    
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Leer el archivo CSV
            df = pd.read_csv(uploaded_file)
            # Asegurarse de que el DataFrame tenga las columnas necesarias
            required_columns = ['serial', 'modelo', 'marca', 'estado', 'empresa_id', 'sede_id']
            if not all(col in df.columns for col in required_columns):
                st.error("El archivo CSV debe contener columnas llamadas 'serial', 'modelo', 'marca', 'estado', 'empresa_id' y 'sede_id'.")
                return
            
            # Cargar cada impresora
            for index, row in df.iterrows():
                data = {
                    "serial": row['serial'],
                    "modelo": row['modelo'],
                    "marca": row['marca'],
                    "estado": row['estado'],
                    "empresa_id": row['empresa_id'],
                    "sede_id": row['sede_id']
                }
                response = requests.post("http://127.0.0.1:8000/impresoras/", json=data)
                if response.status_code == 201:
                    st.success(f"Impresora '{row['serial']}' cargada con éxito.")
                else:
                    st.error(f"Error al cargar la impresora '{row['serial']}'. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar las impresoras: {e}")
