import streamlit as st

def page1():
    st.title("Esta es la información")
    st.write("Bienvenido a la segunda página con más detalles.")
    
    # Botón para ir a la siguiente página
    if st.button("Ir a la siguiente página"):
        st.page_link("/page2")
    
    # Botón para regresar a la página anterior
    if st.button("Ir a la página anterior"):
        st.page_link("/")

if __name__ == "__main__":
    page1()
