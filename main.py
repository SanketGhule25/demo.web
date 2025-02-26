import streamlit as st

st.title("vaibhavi sanas")

st.header("ghule")
st.subheader("python")
st.markdown("vaibhi is a reda")
st.code(""" for i in range(1,5,1):
        print("")
        
        """)


name = st.text_input("enter your name: ")
fname = st.text_input("enter your father name: ")
adr = st.text_area("enter your text: ")
classdata = st.selectbox("enter your class: ",(1,2,3,4,5,))

button = st.button("Done")
if button:
    st.markdown(f"""
   Name:{name}
father name:{fname}
address:{adr}
class:{classdata}""")


