import streamlit as st
import pandas as pd
from style import apply_styles
from data_handler import load_csv_data, initialize_smart_dataframe
from llm_handler import create_llm_model, handle_user_query

# Apply styles using the external style file
apply_styles()

# Streamlit UI
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.markdown("<h1>Data Analysis with PandasAI</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
st.markdown('</div>', unsafe_allow_html=True)

# If a file is uploaded, process it
if uploaded_file is not None:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    data = load_csv_data(uploaded_file)
    st.write(data.head(3))  # Show the first few rows of the file
    st.write(f"Number of rows: {data.shape[0]}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Initialize the LLM model and SmartDataframe
    model = create_llm_model()
    df = initialize_smart_dataframe(data, model)

    # Prompt input and response generation
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate Analysis"):
        if prompt:
            handle_user_query(df, prompt)
    st.markdown('</div>', unsafe_allow_html=True)
