import streamlit as st
import pandas as pd
import requests

def listar_impresoras():
    # Título de la página
    st.header("Lista de Impresoras")

    # Estilo de la página
    st.markdown(""" 
    <style>
        .header {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            font-weight: bold;
        }
        .table {
            border-collapse: collapse;
            width: 100%;
        }
        .table th, .table td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .table th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # Sección para listar impresoras
    st.header("Impresoras Registradas")
    try:
        response = requests.get("http://127.0.0.1:8000/impresoras/")
        if response.status_code == 200:
            df_impresoras = pd.DataFrame(response.json())
            st.table(df_impresoras.style.set_table_attributes('class="table"'))
        else:
            st.error("Error al obtener la lista de impresoras. Código de estado: {}".format(response.status_code))
    except Exception as e:
        st.error(f"Ocurrió un error al intentar obtener las impresoras: {e}")
