import streamlit as st
import requests

def buscar_eliminar_impresoras():
    st.header("Buscar y Eliminar Impresoras")
    
    # Campos para ingresar el serial de la impresora o el UUID
    serial_impresora = st.text_input("Ingresa el serial de la impresora:")
    uuid_impresora = st.text_input("Ingresa el UUID de la impresora:")
    
    # Botón para buscar
    if st.button("Buscar"):
        try:
            # Construir la URL de búsqueda
            if uuid_impresora:
                response = requests.get(f"http://127.0.0.1:8000/impresoras/?uuid={uuid_impresora}")
            elif serial_impresora:
                response = requests.get(f"http://127.0.0.1:8000/impresoras/?serial={serial_impresora}")
            else:
                st.warning("Por favor, ingresa un serial de impresora o un UUID para buscar.")
                return
            
            if response.status_code == 200:
                impresoras = response.json()
                if impresoras:
                    # Mostrar solo el primer resultado encontrado
                    impresora_encontrada = impresoras[0]  # Obtener el primer resultado
                    st.json(impresora_encontrada)  # Mostrar el resultado en formato JSON
                else:
                    st.warning("No se encontraron impresoras con ese criterio de búsqueda.")
            else:
                st.error("Error al buscar la impresora. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar la impresora: {e}")
    
    # Botón para eliminar
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

# Llamar a la función principal
buscar_eliminar_impresoras()
