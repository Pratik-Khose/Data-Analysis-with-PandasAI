import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #c9eaf3, #e3f2fd);
            font-family: 'Arial', sans-serif;
        }
        .glass-container {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            margin-bottom: 20px;
        }
        .glass-container h1 {
            color: #007acc;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 30px;
        }
        .glass-container input, .glass-container textarea {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            border-radius: 10px;
            border: none;
            background-color: rgba(255, 255, 255, 0.7);
        }
        .glass-container button {
            background-color: #007acc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            font-size: 1.2rem;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        .glass-container button:hover {
            background-color: #005f99;
        }
        .data-preview {
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
