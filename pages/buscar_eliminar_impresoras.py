import streamlit as st
import requests

def buscar_eliminar_impresoras():
    st.header("Buscar y Eliminar Impresoras")
    
    uuid_impresora = st.text_input("Ingresa el UUID de la impresora a buscar:")
    serial_impresora = st.text_input("Ingresa el serial de la impresora a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_impresora:
                response = requests.get(f"http://127.0.0.1:8000/impresoras/{uuid_impresora}/")
                if response.status_code == 200:
                    impresora = response.json()
                    st.write(f"**ID**: {impresora['id']}, **Serial**: {impresora['serial']}, **Modelo**: {impresora['modelo']}, **Marca**: {impresora['marca']}, **Estado**: {impresora['estado']}, **Empresa ID**: {impresora['empresa_id']}, **Sede ID**: {impresora['sede_id']}")
                else:
                    st.error("No se encontró la impresora con ese UUID.")
            elif serial_impresora:
                response = requests.get(f"http://127.0.0.1:8000/impresoras/?serial={serial_impresora}")
                if response.status_code == 200:
                    impresoras = response.json()
                    for impresora in impresoras:
                        st.write(f"**ID**: {impresora['id']}, **Serial**: {impresora['serial']}, **Modelo**: {impresora['modelo']}, **Marca**: {impresora['marca']}, **Estado**: {impresora['estado']}, **Empresa ID**: {impresora['empresa_id']}, **Sede ID**: {impresora['sede_id']}")
                else:
                    st.error("No se encontraron impresoras con ese serial.")
            else:
                st.warning("Por favor, ingresa un UUID o un serial para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar la impresora: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_impresora:
                response = requests.delete(f"http://127.0.0.1:8000/impresoras/{uuid_impresora}/")
                if response.status_code == 204:
                    st.success("Impresora eliminada con éxito.")
                else:
                    st.error("Error al eliminar la impresora. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar la impresora.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar la impresora: {e}")
