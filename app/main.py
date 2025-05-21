import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Solar Energy Dashboard",
    layout="wide"
)

# Custom CSS for better mobile experience
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stPlotlyChart, .stDataFrame {
        width: 100%;
    }
    h1 {
        font-size: 2rem;
    }
    @media (max-width: 640px) {
        h1 {
            font-size: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("Cross-Country Solar Energy Dashboard")
st.markdown("""
Explore and compare key solar radiation metrics across Benin, Sierra Leone, and Togo. 
Use the filters below to visualize the data and identify the best locations for solar investment.
""")

# Function to load and prepare data
@st.cache_data
def load_data():
    # Load data from CSV files
    try:
        df_benin = pd.read_csv("data/benin-cleaned.csv")
        df_sierra_leone = pd.read_csv("data/sierraleone-cleaned.csv")
        df_togo = pd.read_csv("data/togo-cleaned.csv")
        
        # Add country column to each DataFrame
        df_benin["country"] = "Benin"
        df_sierra_leone["country"] = "Sierra Leone"
        df_togo["country"] = "Togo"
        
        # Concatenate DataFrames
        df_all = pd.concat([df_benin, df_sierra_leone, df_togo], ignore_index=True)
        
        return df_all
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load data
df_all = load_data()

if df_all is not None:
    # Sidebar controls
    with st.sidebar:
        st.header("Filter Options")
        
        # Country selection
        countries = ["Benin", "Sierra Leone", "Togo"]
        selected_countries = st.multiselect(
            "Select Countries",
            options=countries,
            default=countries
        )
        
        # Metric selection
        metric_options = {
            "GHI (Global Horizontal Irradiance)": "GHI",
            "DNI (Direct Normal Irradiance)": "DNI",
            "DHI (Diffuse Horizontal Irradiance)": "DHI"
        }
        
        selected_metric_name = st.selectbox(
            "Select Solar Metric",
            options=list(metric_options.keys())
        )
        selected_metric = metric_options[selected_metric_name]
        
        st.markdown("---")
        st.markdown("### About the Metrics")
        st.markdown("""
        - **GHI**: Total solar radiation received on a horizontal surface
        - **DNI**: Solar radiation received directly from the sun
        - **DHI**: Diffuse solar radiation scattered by the atmosphere
        """)
    
    # Filter data based on selection
    if not selected_countries:
        st.warning("Please select at least one country.")
        filtered_df = df_all
    else:
        filtered_df = df_all[df_all["country"].isin(selected_countries)]
    
    # Main visualization
    st.subheader(f"{selected_metric_name} Comparison")
    
    # Create figure with appropriate size
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create boxplot
    sns.set_style("whitegrid")
    sns.boxplot(
        x="country", 
        y=selected_metric, 
        data=filtered_df,
        palette="viridis",
        ax=ax
    )
    
    ax.set_title(f"{selected_metric} Distribution by Country", fontsize=14)
    ax.set_xlabel("Country", fontsize=12)
    ax.set_ylabel(f"{selected_metric} (kWh/m²/day)", fontsize=12)
    
    # Display the plot
    st.pyplot(fig, use_container_width=True)
    
    # Summary statistics table
    st.subheader("Summary Statistics")
    
    # Calculate statistics
    summary_stats = filtered_df.groupby("country")[selected_metric].agg([
        ("Mean", "mean"),
        ("Median", "median"),
        ("Std Dev", "std"),
        ("Min", "min"),
        ("Max", "max")
    ]).reset_index()
    
    # Round values for better display
    numeric_columns = summary_stats.columns.difference(["country"])
    summary_stats[numeric_columns] = summary_stats[numeric_columns].round(2)
    
    # Display the table
    st.dataframe(summary_stats, use_container_width=True)
    
    # ANOVA section
    st.subheader("Statistical Analysis")
    
    # Only perform ANOVA if we have at least 2 countries selected
    if len(selected_countries) >= 2:
        # Prepare data for ANOVA
        groups = [filtered_df[filtered_df["country"] == country][selected_metric].values 
                 for country in selected_countries]
        
        # Run ANOVA
        f_stat, p_value = stats.f_oneway(*groups)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("F-statistic", f"{f_stat:.2f}")
        
        with col2:
            st.metric("p-value", f"{p_value:.4f}")
        
        # Interpretation
        if p_value < 0.05:
            interpretation = f"The p-value ({p_value:.4f}) is less than 0.05, indicating statistically significant differences in {selected_metric} values across the selected countries."
        else:
            interpretation = f"The p-value ({p_value:.4f}) is greater than 0.05, suggesting no statistically significant differences in {selected_metric} values across the selected countries."
        
        st.info(interpretation)
        
        st.markdown("""
        **What does this mean?**
        
        A p-value < 0.05 indicates statistically significant differences in solar potential across countries.
        This can help identify which countries might be better candidates for solar energy investments.
        """)
    else:
        st.warning("Select at least two countries to perform statistical comparison.")
    
    # Additional insights
    st.subheader("Key Insights")
    
    # Calculate the country with highest mean for selected metric
    if not filtered_df.empty:
        best_country = filtered_df.groupby("country")[selected_metric].mean().idxmax()
        best_value = filtered_df.groupby("country")[selected_metric].mean().max().round(2)
        
        st.success(f"**{best_country}** has the highest average {selected_metric} value ({best_value} kWh/m²/day) among the selected countries.")
        
        # Create a histogram for distribution
        st.subheader(f"{selected_metric} Distribution")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for country in selected_countries:
            country_data = filtered_df[filtered_df["country"] == country][selected_metric]
            sns.histplot(country_data, kde=True, label=country, alpha=0.6)
        
        plt.legend()
        plt.xlabel(f"{selected_metric} (kWh/m²/day)")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {selected_metric} Values by Country")
        
        st.pyplot(fig, use_container_width=True)
else:
    st.error("Failed to load data. Please check that the CSV files exist in the data/ folder.")