import pickle as pk
import streamlit as st
with open("decisio_tree_car_classifier.pkl","rb")as fi:
    loded_model=pk.load(fi)
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Car Evalution Using Decision Tress</h1>", unsafe_allow_html=True)
price = st.selectbox("SELECT THE PRICE:", ["Low","Medium","High","Very High"])
maintaince = st.selectbox("MAINTAINCE CHARGES:", ["Low","Medium","High","Very High"])
doors = st.select_slider("ENTER NUMBER OF DOORS:", ['2','3','4','5'])
persons = st.select_slider("ENTER NUMBER OF PERSONS CAN SIT:", ['1','2','3','4','5 or More'])
space = st.selectbox("LUGGAGE BOOT SPACE:", ["Small","Medium","Big"])
saftey = st.selectbox("ENTER THE SAFTEY LEVEL:", ['Low','Medium','High','Very High'])
price_map = {"Low":0, "Medium":1, "High":2, "Very High":3}
maint_map = {"Low":0, "Medium":1, "High":2, "Very High":3}
doors_map = {"2":2, "3":3, "4":4, "5":5}
persons_map = {"1":1, "2":2, "3":3, "4":4, "5 or More":5}
space_map = {"Small":0, "Medium":1, "Big":2}
safety_map = {"Low":0, "Medium":1, "High":2, "Very High":3}
price_num = price_map[price]
maint_num = maint_map[maintaince]
doors_num = doors_map[doors]
persons_num = persons_map[persons]
space_num = space_map[space]
safety_num = safety_map[saftey]

st.markdown(
    """
    <style>
    div.stButton {
        display: flex;
        justify-content: center;  /* centers horizontally */
    }
    div.stButton > button:first-child {
        background-color: blue;
        color: white;
        border-radius: 6px;
        padding: 12px 24px;
        font-size: 16px;
        cursor: pointer;
    }
    div.stButton > button:first-child:active {
        background-color: green;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Predict"):
    user_input = [[price_num, maint_num, doors_num, persons_num, space_num, safety_num]]
    prediction = loded_model.predict(user_input)
    if prediction==1:
        output=" ❌ Unacceptable "
    elif prediction==2:
        output="✅ Acceptable"
    elif prediction==3:
        output="👍 Good"
    else:
        output="😮Very Good"
    st.write("TOTAL TYPES :Unacceptable Acceptable Good Very Good")
    st.markdown(f"<h3 style='text-align: center;'>Prediction: {output}</h3>", unsafe_allow_html=True)