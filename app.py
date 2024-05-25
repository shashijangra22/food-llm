import streamlit as st
import requests

diet_plan_text = st.text_area('Enter your diet plan', height=220)
loc = st.selectbox('Select Location', ["Delhi", "Chennai", "Mumbai", "Bangalore"])
time = st.time_input('Select Time')


def get_time(time):
    return time.strftime("%H:%M")


if st.button("Submit"):
    body = {
        "plan": diet_plan_text,
        "loc": loc,
        "time": get_time(time)
    }
    response = requests.post("http://127.0.0.1:8000/recommendations", json=body)
    if response.status_code == 200:
        body = response.json()
        recommendations = body["recommendations"]
        error = body["error"]
        if error:
            st.error(f"Error: {error}")
        else:
            st.text_area("Here are the recommendations:", value=recommendations, height=300)
    else:
        st.error(f"Error {response.status_code}: Could not process the request!")
