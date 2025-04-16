import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# -- Page config --
st.set_page_config(page_title="Data Visualizer", layout="wide")

# -- Optional header image --
st.image("https://img.freepik.com/premium-vector/graph-data-analysis-concept-chart-isolated-flat-illustration_18591-851.jpg", use_column_width=True)

# -- Title --
st.markdown("<h1 style='text-align:center; color:#3A81F1;'>📊 Data Visualizer</h1>", unsafe_allow_html=True)
st.markdown("---")

# -- Sidebar image & instructions --
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3588/3588531.png", width=100)
    st.markdown("### 📂 Upload Excel Files")
    st.markdown("You can upload multiple `.xlsx` files for comparison and analysis.")
    st.markdown("---")

# -- File Upload --
files = st.file_uploader("Upload your Excel files", type=["xlsx"], accept_multiple_files=True)

if files:
    files_name = [file.name for file in files]
    selected = st.multiselect("Select files to visualize", options=files_name, default=files_name[0])

    if selected:
        dataframes = {}
        for file in files:
            if file.name in selected:
                df = pd.read_excel(file, index_col=0)
                df.columns = df.columns.str.strip()
                dataframes[file.name] = df

        sanitized_columns = dataframes[selected[0]].columns.tolist()
        option = st.radio("Select column to visualize", options=sanitized_columns, index=0)

        if option:
            for file in selected:
                shop = dataframes[file]

                if option not in shop.columns:
                    st.error(f"'{option}' not found in {file}")
                    continue

                series = shop[option]
                st.subheader(f"📁 {file} — `{option}`")

                fig, ax = plt.subplots(figsize=(10, 4))

                if pd.api.types.is_numeric_dtype(series):
                    ax.plot(series.index, series.values, marker='o', linestyle='-', color='mediumseagreen')
                    ax.set_title(f"{option} Trend", fontsize=14)
                    ax.set_xlabel("Index")
                    ax.set_ylabel(option)
                    ax.grid(True)
                    st.pyplot(fig)

                elif pd.api.types.is_datetime64_any_dtype(series):
                    ax.plot(series.index, series.values, color='orange')
                    ax.set_title(f"{option} Over Time", fontsize=14)
                    ax.set_xlabel("Time")
                    ax.set_ylabel(option)
                    st.pyplot(fig)

                else:
                    # Categorical data
                    value_counts = series.value_counts()
                    ax.bar(value_counts.index.astype(str), value_counts.values, color='cornflowerblue')
                    ax.set_title(f"Category Distribution: {option}")
                    ax.set_xlabel(option)
                    ax.set_ylabel("Count")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

                # Display raw values if user wants
                with st.expander(f"🔎 View Raw Data for {file}"):
                    st.dataframe(series)

else:
    st.info("👈 Upload at least one `.xlsx` file to get started!")
