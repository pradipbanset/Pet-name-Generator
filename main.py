import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("dog", "cat", "bird", "fish", "rabbit"))

if animal_type == "Cat":
    pet_colour = st.sidebar.text_area(abel="What is the colour of your cat?", max_chars=15)

elif animal_type == "Dog":
    pet_colour = st.sidebar.text_area(label="What is the colour of your dog?", max_chars=15)

elif animal_type == "Bird":
    pet_colour = st.sidebar.text_area(label="What is the colour of your bird?", max_chars=15)

elif animal_type == "Fish":
    pet_colour = st.sidebar.text_area(label="What is the colour of your fish?", max_chars=15)

elif animal_type == "Rabbit":
    pet_colour = st.sidebar.text_area(label="What is the colour of your rabbit?", max_chars=15)

else:
    pet_colour = st.sidebar.text_area(label="What is the colour of your pet?", max_chars=15)

if pet_colour:
    response = lch.generate_pet_name(animal_type, pet_colour)
    st.text(response["pet_name"])

