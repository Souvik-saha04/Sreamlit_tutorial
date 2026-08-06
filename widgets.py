import streamlit as st 

st.title("chai maker app")

tea_type=st.radio("pick your chai base : ",["milk","water","spray milk"])
masala=st.checkbox("add masala")
tea=st.checkbox("add tea")
chroma=st.checkbox("add chroma")
spice=st.checkbox("add spice")

sugar=st.slider("sugar level : ",0,10,2)
if(st.button("make chai")):
    st.write("making chai.....")
    st.success("your chai has been brewed")

name=st.text_input("ente your name : ")
dob =st.date_input("select youyr date of birth : ")
if(st.button("click to see INGREDIENTS ")):
    st.write(f"welcome ! {name}")
    st.write(f"Born on ! {dob}")
    st.write(f"base : {tea_type}")
    st.write(f"sugar level :{sugar}")
    if(masala):
        st.write("masala")
    if(tea):
        st.write("tea")
    if(chroma):
        st.write("chroma")
    if(spice):
        st.write("spice")
