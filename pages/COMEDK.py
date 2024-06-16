import pandas as pd
import streamlit as st
import os
from pathlib import Path

base_path = os.environ["BASE_PATH"]

@st.cache_data
def load_data():
    round1_22 = pd.read_excel(Path(base_path, "cutoffs/comedk/2022", "round1.xlsx"), engine="openpyxl")
    round2_22 = pd.read_excel(Path(base_path, "cutoffs/comedk/2022", "round2.xlsx"), engine="openpyxl")
    round3_22 = pd.read_excel(Path(base_path, "cutoffs/comedk/2022", "round3.xlsx"), engine="openpyxl")

    round1_21 = pd.read_excel(Path(base_path, "cutoffs/comedk/2021", "round1.xlsx"), engine="openpyxl")
    round2_21 = pd.read_excel(Path(base_path, "cutoffs/comedk/2021", "round2.xlsx"), engine="openpyxl")
    round3_21 = pd.read_excel(Path(base_path, "cutoffs/comedk/2021", "round3.xlsx"), engine="openpyxl")

    round1_23 = pd.read_excel(Path(base_path, "cutoffs/comedk/2023", "round1.xlsx"), engine="openpyxl")
    round2_23 = pd.read_excel(Path(base_path, "cutoffs/comedk/2023", "round2.xlsx"), engine="openpyxl")

    return {"2022": {"Round 1": round1_22, "Round 2": round2_22, "Round 3": round3_22}, "2021": {"Round 1": round1_21, "Round 2": round2_21, "Round 3": round3_21}, "2023": {"Round 1": round1_23, "Round 2": round2_23}}


data = load_data()

st.title("COMEDK Cutoffs")
st.write("This is a simple web app to view COMEDK cutoffs")

show_data = False

def filter_data(data, college_codes, year, round, branch, category):
    return data[year][round][data[year][round]["College Code"].isin(college_codes) & data[year][round]["Seat Category"].isin(category)][["College Name"] + branch]

with st.form(key="my_form"):
    year = st.multiselect("Select Year", ["2023","2022", "2021"], default=["2023"])
    colleges = st.multiselect("Select Colleges", data[year[0]]["Round 1"]["College Name"].unique())
    college_codes = data[year[0]]["Round 1"][data[year[0]]["Round 1"]["College Name"].isin(colleges)]["College Code"].unique()
    branch = st.multiselect("Select Branches", data[year[0]]["Round 1"].columns[4:].to_list())
    round = st.multiselect("Select Rounds", ["Round 1", "Round 2", "Round 3"])
    category = st.multiselect("Select Categories", data[year[0]]["Round 1"]["Seat Category"].unique())
    rank = st.number_input("Enter Rank", min_value=1, max_value=200000, value=1000)
    if st.form_submit_button("Filter", use_container_width=True):
        show_data = True

if show_data:
    for col, y in enumerate(year):
        if y=="2023":
            round = ["Round 1", "Round 2"]
        with st.container(border=True):
            for r in round:
                st.title(f"{y} {r}")
                st.write(filter_data(data, college_codes, y, r, branch, category))