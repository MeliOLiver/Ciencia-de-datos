import streamlit as st

def main():
    st.title("Bienvenidos")
    st.write("Esta es la página de inicio.")
    
    # Solo hay un botón para ir a la siguiente página
    if st.button("Ir a la siguiente página"):
        st.page_link("/page1")

if __name__ == "__main__":
    main()

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
import streamlit as st

def page3():
    st.title("Última Página")
    st.write("Aquí acaban las páginas.")
    
    # Botón para regresar a la página anterior
    if st.button("Ir a la página anterior"):
        st.page_link("/page2")

if __name__ == "__main__":
    page3()
