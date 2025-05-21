import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin-cleaned.csv")
    sierra_leone = pd.read_csv("data/sierraleone-cleaned.csv")
    togo = pd.read_csv("data/togo-cleaned.csv")
    benin["country"] = "Benin"
    sierra_leone["country"] = "Sierra Leone"
    togo["country"] = "Togo"
    return pd.concat([benin, sierra_leone, togo])

df = load_data()

# UI Elements
st.title("🌞 Cross-Country Solar Data Dashboard")

selected_country = st.selectbox("Select a Country", df["country"].unique())
metric = st.selectbox("Select a Metric", ["GHI", "DNI", "DHI"])

# Filter and Plot
filtered_df = df[df["country"] == selected_country]

st.subheader(f"{metric} Distribution in {selected_country}")
fig, ax = plt.subplots()
sns.histplot(filtered_df[metric].dropna(), kde=True, ax=ax)
st.pyplot(fig)