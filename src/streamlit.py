import streamlit as st
import requests

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    url = 'http://127.0.0.1:5000/api/1.0/inventory'
    data = {'message': question}

    response = requests.post(url, json=data)
    print(response.json())  # Print response JSON

    # Check if the request was successful
    if response.status_code == 200:
        # Load JSON data from response content
        response_data = response.json()

        st.header("Answer")

        # Display JSON data using Streamlit
        st.write(response_data["result"])
    else:
        st.write(f"Error: Failed to retrieve data. Status code: {response.status_code}")
