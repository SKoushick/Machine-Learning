import streamlit as st
import time as t

st.image("C:/Users/Kousimon/OneDrive/Desktop/Data Scientist/modified_image.jpg")

#title 
st.title("Welcome to Streamlit")

#header
st.header("Machine Learning")

#subheader
st.subheader("Linear Regression")

#to give information
st.info("Information details of a user")

#warning message 
st.warning("Come on time or else you will be marked as late")

#Error message

st.error("Wrong password")

# Write fucntion
st.write("Employee Name")
st.write(range(50))

#Success message
st.success("You have successfully logged in")

#Markdown
st.markdown("# Kousimon")
st.markdown("## Kousimon")
st.markdown(":rocket:")

st.text("This is a Streamlit web development training")

#to write a caption
st.caption("This is a caption for the text above")

#Mathematical Equations to be displayed
st.latex(r'''a^2 + b^2 = c^2''')

#widget

#checkbox
st.checkbox("Check this box if you are a Data Scientist")


#Button
st.button("Click")

#
st.radio("Pick your age group", ["18-25", "26-35", "36-45", "46-60", "60+"])


#Selectbox
st.selectbox("Pick your course", ["Python", "R", "SQL", "Machine Learning", "Deep Learning"])

#Multiselect

st.multiselect("Pick your favorite languages", ["Python", "R", "SQL", "Java", "C++"])

#Select slider

st.select_slider("Rating ", options=[1, 2, 3, 4, 5])

#slider
st.slider("Enter number",0,100)

#number input
st.number_input("Enter your number",0,100)

#text input

st.text_input("Enter your name:") 

#date input
st.date_input("Opening ceremony")

#time input
st.time_input("what time is it?")

#text area
st.text_area("This is the place where to enter our text")

#file uploader

st.file_uploader("Upload your file", type=["jpg", "png", "jpeg"])

#choosing color
st.color_picker("Pick a color")


#progress bar
st.progress(90)

#spinner
with st.spinner("Loading..."):
    t.sleep(3)
    
#ballons
st.balloons()


#Sidebar
st.sidebar.title("Welcome to the sidebar")
st.sidebar.text_input("Enter your name")
st.sidebar.button("Submit")
st.sidebar.radio("Select an option", ["1", "2", "3"])


#data visualization
import pandas as pd
import numpy as np
st.title("Bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)