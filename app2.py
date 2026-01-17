import streamlit as st
import pickle
from PIL import Image
def main():
    st.title(":blue[IRIS FLOWER REPORT]")
    img = Image.open("download.webp")
    st.image(img, width=800)
    sepellengthcm=st.text_input("enter the sepellenght in cm:"," ")
    sepelwidthcm = st.text_input("enter the sepelwidth in cm:", " ")
    petallengthcm = st.text_input("enter the petallenght in cm:", " ")
    petalwidthcm = st.text_input("enter the petalwidth in cm:", " ")
    features=[sepellengthcm,sepelwidthcm,petallengthcm,petalwidthcm]
    scalar=pickle.load(open("scalar.sav","rb"))
    model=pickle.load(open("modelknn.sav","rb"))
    pred=st.button("predict")
    if pred:

        result=model.predict(scalar.transform([features]))
        st.write("Species",result)
main()