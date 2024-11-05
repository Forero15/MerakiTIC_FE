import streamlit as st
import pandas as pd
import requests

def listar_departamentos():
    # Título de la página
    st.header("Lista de Departamentos")

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

    # Sección para listar departamentos
    st.header("Departamentos Registrados")
    try:
        response = requests.get("http://127.0.0.1:8000/departamentos/")
        if response.status_code == 200:
            df_departamentos = pd.DataFrame(response.json())
            st.table(df_departamentos.style.set_table_attributes('class="table"'))
        else:
            st.error("Error al obtener la lista de departamentos. Código de estado: {}".format(response.status_code))
    except Exception as e:
        st.error(f"Ocurrió un error al intentar obtener los departamentos: {e}")
