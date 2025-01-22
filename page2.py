import streamlit as st

def page2():
    st.title("Aquí acaban las páginas")
    st.write("Has llegado a la última página.")
    
    # Botón para ir a la siguiente página
    if st.button("Ir a la siguiente página"):
        st.page_link("/page3")
    
    # Botón para regresar a la página anterior
    if st.button("Ir a la página anterior"):
        st.page_link("/page1")

if __name__ == "__main__":
    page2()
