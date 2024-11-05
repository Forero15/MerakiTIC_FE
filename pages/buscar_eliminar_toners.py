import streamlit as st
import requests

def buscar_eliminar_toners():
    st.header("Buscar y Eliminar Tóners")
    
    uuid_toner = st.text_input("Ingresa el UUID del tóner a buscar:")
    referencia_toner = st.text_input("Ingresa la referencia del tóner a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_toner:
                response = requests.get(f"http://127.0.0.1:8000/toners/{uuid_toner}/")
                if response.status_code == 200:
                    toner = response.json()
                    st.write(f"**ID**: {toner['id']}, **Referencia**: {toner['referencia']}, **Estado**: {toner['estado']}, **Empresa ID**: {toner['empresa_id']}, **Sede ID**: {toner['sede_id']}")
                else:
                    st.error("No se encontró el tóner con ese UUID.")
            elif referencia_toner:
                response = requests.get(f"http://127.0.0.1:8000/toners/?referencia={referencia_toner}")
                if response.status_code == 200:
                    toners = response.json()
                    for toner in toners:
                        st.write(f"**ID**: {toner['id']}, **Referencia**: {toner['referencia']}, **Estado**: {toner['estado']}, **Empresa ID**: {toner['empresa_id']}, **Sede ID**: {toner['sede_id']}")
                else:
                    st.error("No se encontraron tóners con esa referencia.")
            else:
                st.warning("Por favor, ingresa un UUID o una referencia para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar el tóner: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_toner:
                response = requests.delete(f"http://127.0.0.1:8000/toners/{uuid_toner}/")
                if response.status_code == 204:
                    st.success("Tóner eliminado con éxito.")
                else:
                    st.error("Error al eliminar el tóner. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar el tóner.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar el tóner: {e}")
