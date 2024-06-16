import pandas as pd
import streamlit as st
import os
from pathlib import Path

base_path = os.environ["BASE_PATH"]

@st.cache_data
def load_data():
    round1_22 = pd.read_excel(Path(base_path, "cutoffs/kcet/2022", "round1.xlsx"), engine="openpyxl")
    round1_22.rename(columns={"2022Round1":"GM"}, inplace=True)
    round2_22 = pd.read_excel(Path(base_path, "cutoffs/kcet/2022", "round2.xlsx"), engine="openpyxl")
    round2_22.rename(columns={"2022Round2":"GM"}, inplace=True)
    round3_22 = pd.read_excel(Path(base_path, "cutoffs/kcet/2022", "round3.xlsx"), engine="openpyxl")
    round3_22.rename(columns={"2022Round3":"GM"}, inplace=True)

    round1_21 = pd.read_excel(Path(base_path, "cutoffs/kcet/2021", "round1.xlsx"), engine="openpyxl")
    round1_21.rename(columns={"2021Round1":"GM"}, inplace=True)
    round2_21 = pd.read_excel(Path(base_path, "cutoffs/kcet/2021", "round2.xlsx"), engine="openpyxl")
    round2_21.rename(columns={"2021Round2":"GM"}, inplace=True)
    round3_21 = pd.read_excel(Path(base_path, "cutoffs/kcet/2021", "round3.xlsx"), engine="openpyxl")
    round3_21.rename(columns={"2021Round3":"GM"}, inplace=True)


    return {"2022": {"Round 1": round1_22, "Round 2": round2_22, "Round 3": round3_22}, "2021": {"Round 1": round1_21, "Round 2": round2_21, "Round 3": round3_21}}

def filter_data(data, college_codes, year, round, branch, category):
    return data[year][round][data[year][round]["College Code"].isin(college_codes) & data[year][round]["Branch"].isin(branch)][["College Name", "Branch"] + category].sort_values(by=category)

data = load_data()

st.title("KCET Cutoffs")
st.write("This is a simple web app to view KCET cutoffs")


show_data = False

with st.form(key="my_form"):
    year = st.multiselect("Select Year", ["2022", "2021"], default=["2022"])
    colleges = st.multiselect("Select Colleges", data[year[0]]["Round 1"]["College Name"].unique())
    branch = st.multiselect("Select Branches", data[year[0]]["Round 1"]["Branch"].unique())
    college_codes = data[year[0]]["Round 1"][data[year[0]]["Round 1"]["College Name"].isin(colleges)]["College Code"].unique()
    round = st.multiselect("Select Rounds", ["Round 1", "Round 2", "Round 3"])
    category = st.multiselect("Select Categories", data[year[0]]["Round 1"].columns[3:24].to_list())

    if st.form_submit_button("Filter", use_container_width=True):
        show_data = True


if show_data:
    for col, y in enumerate(year):
            with st.container(border=True):
                for r in round:
                    st.title(f"{y} {r}")
                    st.write(filter_data(data, college_codes, y, r, branch, category))





