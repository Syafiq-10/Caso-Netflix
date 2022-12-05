import pandas as pd
import streamlit as st


st.title("Netflix Peliculas")

@st.cache
def load_data(nrows):
    data = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/Netflix/movies.csv', nrows=nrows)
    return data


data = load_data(500)

sidebar = st.sidebar
sidebar.title("Sofía Almeraya")
sidebar.subheader('A01283713')



if sidebar.checkbox("Mostrar todas las Peliculas",value=True):
    st.dataframe(data)


title=st.sidebar.text_input('Titulo de la Pelicula')
submit_boton=st.sidebar.button(label='Buscar')

if (submit_boton):
    titulo=data.copy()
    titulo['name']=titulo['name'].str.lower()
    filtrar=titulo[titulo['name'].str.contains(title.lower())]
    st.dataframe(filtrar)


director=st.sidebar.selectbox('Director',data['director'])
search_button=st.sidebar.button(label='Filtrar')

if (search_button):
    filtrard=data[data['director']==director]
    st.dataframe(filtrard)
    
