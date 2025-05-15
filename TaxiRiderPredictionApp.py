import pickle as pkl
import streamlit as slt

tp=slt.title("Taxi Rider Prediction App")
ppw=slt.number_input("Enter Price per week")
pln=slt.number_input("Enter Population")
minc=slt.number_input("Enter Monthly Income")
ppm=slt.number_input("Enter Average parking per month")

button=slt.button("Predict")
if button:
    lr=pkl.load(open("taxi.pkl","rb"))
    res=lr.predict([[ppw,pln,minc,ppm]])[0]
    slt.markdown(f"weekly riders :{res}")