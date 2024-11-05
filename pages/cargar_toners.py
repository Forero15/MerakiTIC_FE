import streamlit as st
import pandas as pd
import requests

def cargar_toners():
    st.header("Cargar Tóners en Bulk")
    
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Leer el archivo CSV
            df = pd.read_csv(uploaded_file)
            # Asegurarse de que el DataFrame tenga las columnas necesarias
            required_columns = ['referencia', 'estado', 'empresa_id', 'sede_id']
            if not all(col in df.columns for col in required_columns):
                st.error("El archivo CSV debe contener columnas llamadas 'referencia', 'estado', 'empresa_id' y 'sede_id'.")
                return
            
            # Cargar cada tóner
            for index, row in df.iterrows():
                data = {
                    "referencia": row['referencia'],
                    "estado": row['estado'],
                    "empresa_id": row['empresa_id'],
                    "sede_id": row['sede_id']
                }
                response = requests.post("http://127.0.0.1:8000/toners/", json=data)
                if response.status_code == 201:
                    st.success(f"Tóner '{row['referencia']}' cargado con éxito.")
                else:
                    st.error(f"Error al cargar el tóner '{row['referencia']}'. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los tóners: {e}")
