import streamlit as st
import os
os.environ["BASE_PATH"] = os.path.dirname(__file__)

st.set_page_config(page_title="Bangalore College Cutoffs", page_icon="🎓", layout="wide")
st.title("Bangalore College Cutoffs")

st.markdown('''- This is a simple web app to view Bangalore college cutoffs. 
- The data for COMEDK and KCET is available.
- The data is available for the years 2021 and 2022.
- The data is available for rounds 1, 2, and 3.
- The data is available for all branches and categories.
- The data is available for all colleges in Bangalore.
- The data is sourced from the official KEA and COMEDK websites.
- Click on the respective links in the sidebar to view the cutoffs.
''')

