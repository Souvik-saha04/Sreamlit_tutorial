import streamlit as st

st.write("choose the text ")
chai=st.selectbox("your fav chai ", 
                  ["","lemon chai","masala chai","ghurni chai"])

if(chai==""):
    st.write(f"not chose anythong")
else:
    st.write(f"your choice {chai}")

status=st.selectbox("select the status of the chai",["select status","delivered","preparing","destroyed","cancelled"])
if(status=="delivered"):
    st.success("you chai has been delivered")
elif (status=="destroyed" or status=="cancelled"):
    st.error(f"your chai has been {status}")
elif(status=="preparing"):
    st.write("you chai is being prepared")
else:
    st.write("Enter your choice")