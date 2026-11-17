import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="StudentFlight Finder", page_icon="✈️", layout="wide")

st.title("✈️ StudentFlight Finder")
st.write("Tell me where you want to go in plain English. I’ll find the cheapest flexible options.")

query = st.text_area(
    "Your request",
    placeholder="Example: Cheap flight to Chicago next weekend under $180. Can leave Thu–Sat, okay with BOS, JFK or EWR.",
    height=100
)

if st.button("Find flights", type="primary") and query:
    with st.spinner("Thinking and searching..."):
        # TODO: 1. Extract parameters with LLM
        # TODO: 2. Search flights (Amadeus / SerpAPI / etc.)
        # TODO: 3. Rank and display results
        st.info("Framework ready. Next: add LLM extraction + flight API.")