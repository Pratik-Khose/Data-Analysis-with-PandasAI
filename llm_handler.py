from pandasai.llm.local_llm import LocalLLM
import streamlit as st
from pandasai.exceptions import MaliciousQueryError, NoResultFoundError

def create_llm_model():
    return LocalLLM(
        api_base="http://localhost:11434/v1",
        model="llama3"
    )

def handle_user_query(df, prompt):
    with st.spinner("Generating response..."):
        try:
            response = df.chat(prompt)  # Execute the prompt using the LLM
            st.write(response)
        except MaliciousQueryError:
            st.error("Your query contained potentially malicious code. Please rephrase.")
        except NoResultFoundError:
            st.warning("No result was returned. Please modify your query.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
