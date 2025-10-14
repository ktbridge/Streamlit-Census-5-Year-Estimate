import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.markdown(
    f"""
    <style>
    .stApp {{
        background: #f9f5eb;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f'<style>.footer {{position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F0F0F0; color: #333; text-align: center; padding: 10px; font-size: 14px; border-top: 1px solid #ccc;}}</style><div class="footer">&copy; 2025 Copyright: Christina Trowbridge. All rights reserved.</div>', unsafe_allow_html=True)
#hide_streamlit_style = "<style>header[data-testid="stHeader"] {visibility: hidden;}</style>"
st.markdown(
    """
    <style>
        /* Hide only the main app header bar */
        [data-testid="stHeader"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.cache_data
def load_data(year):
    """Load census data for a specific year."""
    return pd.read_csv(f"census_data_{year}.csv")

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #FC8059; /* your custom color */
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] h2 {
        font-size: 24px;
        font-weight: bold;
        font-family: \"Georgia\", sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("Pick States to Filter by:")
st.write("")
st.write("")

st.markdown("""
            <div style='display: flex; align-items: center; gap: 10px;margin-top: 0px;'>
            <svg height="100px" width="100px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path style="fill:#E2DCBC;" d="M460.8,406.905H51.2c-23.812,0-43.116-19.304-43.116-43.116V94.316 C8.084,70.504,27.388,51.2,51.2,51.2h409.6c23.812,0,43.116,19.304,43.116,43.116v269.474 C503.916,387.601,484.612,406.905,460.8,406.905z"></path> <path style="fill:#F4EECB;" d="M460.8,385.347H51.2c-11.906,0-21.558-9.651-21.558-21.558V94.316 c0-11.906,9.651-21.558,21.558-21.558h409.6c11.906,0,21.558,9.651,21.558,21.558v269.474 C482.358,375.696,472.706,385.347,460.8,385.347z"></path> <path style="fill:#BFBBA3;" d="M385.347,428.463H126.653c-11.906,0-21.558-9.651-21.558-21.558l0,0 c0-11.906,9.651-21.558,21.558-21.558h258.695c11.906,0,21.558,9.651,21.558,21.558l0,0 C406.905,418.812,397.254,428.463,385.347,428.463z"></path> <path style="fill:#A3CCAA;" d="M385.347,331.453h-97.011V29.642c0-11.906,9.651-21.558,21.558-21.558h53.895 c11.906,0,21.558,9.651,21.558,21.558V331.453z"></path> <path style="fill:#80A886;" d="M331.453,331.453h-97.011V148.211c0-11.906,9.651-21.558,21.558-21.558h53.895 c11.906,0,21.558,9.651,21.558,21.558V331.453z"></path> <path style="fill:#FC8059;" d="M309.895,331.453h-97.011v-204.8c0-11.906,9.651-21.558,21.558-21.558h53.895 c11.906,0,21.558,9.651,21.558,21.558V331.453z"></path> <path style="fill:#BF5243;" d="M256,331.453h-97.011v-86.232c0-11.906,9.651-21.558,21.558-21.558h53.895 c11.906,0,21.558,9.651,21.558,21.558V331.453z"></path> <path style="fill:#FED766;" d="M234.442,331.453h-97.011V223.663c0-11.906,9.651-21.558,21.558-21.558h53.895 c11.906,0,21.558,9.651,21.558,21.558V331.453z"></path> <path style="fill:#4C4C4C;" d="M460.8,43.116h-67.368V29.642C393.432,13.298,380.134,0,363.789,0h-53.895 c-16.344,0-29.642,13.298-29.642,29.642v13.474H51.2c-28.231,0-51.2,22.969-51.2,51.2v269.474c0,28.231,22.969,51.2,51.2,51.2 h46.932c3.527,12.428,14.978,21.558,28.521,21.558H204.8v59.284h-99.705c-4.465,0-8.084,3.618-8.084,8.084s3.62,8.084,8.084,8.084 h301.811c4.466,0,8.084-3.618,8.084-8.084s-3.618-8.084-8.084-8.084H307.2v-59.284h78.147c13.543,0,24.994-9.13,28.522-21.558h46.93 c28.231,0,51.2-22.969,51.2-51.2V94.316C512,66.085,489.031,43.116,460.8,43.116z M296.421,29.642 c0-7.43,6.044-13.474,13.474-13.474h53.895c7.43,0,13.474,6.044,13.474,13.474v293.726h-59.284V126.653 c0-13.543-9.13-24.994-21.558-28.522V29.642z M288.337,113.179c7.43,0,13.474,6.044,13.474,13.474v196.716h-59.284v-99.705 c0-13.543-9.13-24.994-21.558-28.522v-68.488c0-7.43,6.044-13.474,13.474-13.474H288.337z M226.358,223.663v99.705h-80.842v-99.705 c0-7.43,6.044-13.474,13.474-13.474h53.895C220.314,210.189,226.358,216.233,226.358,223.663z M291.032,495.832h-70.063v-59.284 h70.063V495.832z M385.347,420.379h-86.232H126.653c-7.43,0-13.474-6.044-13.474-13.474s6.044-13.474,13.474-13.474h258.695 c7.43,0,13.474,6.044,13.474,13.474S392.777,420.379,385.347,420.379z M495.832,363.789c0,19.317-15.715,35.032-35.032,35.032 h-46.93c-3.527-12.428-14.978-21.558-28.522-21.558H126.653c-13.544,0-24.994,9.13-28.521,21.558H51.2 c-19.316,0-35.032-15.715-35.032-35.032V94.316c0-19.317,15.716-35.032,35.032-35.032h229.053v37.726h-45.811 c-16.345,0-29.642,13.298-29.642,29.642v67.368h-45.811c-16.345,0-29.642,13.298-29.642,29.642v99.705h-51.2 c-4.465,0-8.084,3.618-8.084,8.084c0,4.466,3.62,8.084,8.084,8.084h324.138c4.466,0,8.084-3.618,8.084-8.084 c0-4.466-3.618-8.084-8.084-8.084h-8.854V59.284H460.8c19.317,0,35.032,15.715,35.032,35.032V363.789z M441.937,331.453 c0,4.466-3.618,8.084-8.084,8.084h-1.588c-4.466,0-8.084-3.618-8.084-8.084c0-4.466,3.618-8.084,8.084-8.084h1.588 C438.318,323.368,441.937,326.987,441.937,331.453z"></path> </g>
            </svg>       
            <p style='color: #000042;font-size:35px; font-weight: bold;font-family: \"Georgia\", sans-serif; margin-top: 8px;'> Census 4-Year Estimates Dashboard (2019–2023)</p>
            """,unsafe_allow_html=True)

#st.markdown("Interactive dashboard built with **Streamlit** using U.S. Census data from 2019–2023.")

years = [2019, 2020, 2021, 2022, 2023]
selected_years = st.multiselect("Select Years to View Dashboard Data:", years, default=[2023])


dfs = []
for y in selected_years:
    df_year = load_data(y)
    df_year["Year"] = y
    dfs.append(df_year)

df = pd.concat(dfs)

# Sidebar filter for States
with st.sidebar.expander(""):
    states = st.multiselect("", df["State"].unique(), default=df["State"].unique())
df_filtered = df[df["State"].isin(states)]

st.sidebar.markdown("<br><br>", unsafe_allow_html=True) 
st.sidebar.metric("Total States (+ Washington, D.C. and Puerto Rico)", len(df["State"].unique()))

st.sidebar.markdown("<br>", unsafe_allow_html=True) 
st.sidebar.metric("Total US Population - 2023", f"{round(df[df['Year']==2023]['Population'].sum()):,}")

st.sidebar.markdown("<br>", unsafe_allow_html=True) 
st.sidebar.metric("Median US Age - 2023", f"{round(df[df['Year']==2023]['Median Age'].sum()/len(df[df['Year']==2023]))}")

# Population
st.header("Population Overview")

df["Year"] = df["Year"].astype(str).str.strip()
df["State"] = df["State"].astype(str).str.strip()
df_pivot = df_filtered.pivot_table(index="State", columns="Year", values="Population", aggfunc="sum").fillna(0)

colors = ["#772f1a", "#f58549", "#585123", "#eec170", "#f2a65a",  "#19D3F3"]

fig = go.Figure()
for i, year in enumerate(sorted(df_pivot.columns)):
    fig.add_trace(go.Bar(
        x=df_pivot.index, 
        y=df_pivot[year], 
        name=str(year),
        marker_color = colors[i]
    ))

base_width = 5000 
extra_width_per_year = 150  
fig_width = base_width + (len(selected_years) - 1) * extra_width_per_year
final_width = max(fig_width, 5000)

fig.update_layout(
    width = final_width,
    height = 600,
    title = "Population by State and Year",
    xaxis_title = "State",
    yaxis_title = "Population",
    barmode = "group",  
    bargap = 0.15,     
    xaxis = dict(categoryorder = "array", categoryarray = list(df_pivot.index), tickangle = -90),
    margin=dict(b=100),  
    plot_bgcolor="#f9f5eb",  
    paper_bgcolor="#f9f5eb")

st.plotly_chart(fig, use_container_width=False)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Median Age
st.header("Median Age Distribution")
fig_age = px.scatter(
    df_filtered,
    x = "State",
    y = "Median Age",
    size = "Population",
    color = "Median Age",
    title = "Median Age Across States by Year"
)

fig_age.update_layout(
    plot_bgcolor = "#f9f5eb",  
    paper_bgcolor = "#f9f5eb")

st.plotly_chart(fig_age, use_container_width=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Income
df_filtered_year = df_filtered[df_filtered["Year"].isin(selected_years)]

for year in sorted(selected_years):
    st.subheader(f"Income Data for {year}")
    df_year = df_filtered_year[df_filtered_year["Year"] == year]
    col1, col2 = st.columns(2)

    with col1:
        fig_hh_income = px.bar(
            df_year,
            x = "State",
            y = "Household Income",
            title = f"Median Household Income by State ({year})",
            color = "Household Income", 
            color_continuous_scale = ["#4f000b", "#720026", "#ce4257", "#ff7f51", "#ff9b54"]
        )
        fig_hh_income.update_layout(coloraxis_showscale = False, plot_bgcolor = "#f9f5eb", paper_bgcolor = "#f9f5eb")
        st.plotly_chart(fig_hh_income, use_container_width=True)

    with col2:
        fig_pc_income = px.bar(
            df_year,
            x="State",
            y="Per Capita Income",
            title=f"Per Capita Income by State ({year})",
            color="Household Income", 
            color_continuous_scale=px.colors.sequential.Viridis
        )
        fig_pc_income.update_layout(coloraxis_showscale=False, plot_bgcolor="#f9f5eb", paper_bgcolor="#f9f5eb")
        st.plotly_chart(fig_pc_income, use_container_width=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Poverty
for year in sorted(selected_years):
    st.subheader(f"Poverty Overview {year}")
    df_year = df_filtered_year[df_filtered_year["Year"] == year]
    
    fig_poverty = px.scatter(
        df_year,
        x="Poverty Rate",
        y="Household Income",
        size="Poverty Count",
        color="Poverty Rate",
        hover_name="State",
        title="Poverty Rate vs Household Income",
    )
    fig_poverty.update_layout(
    plot_bgcolor="#f9f5eb",  
    paper_bgcolor="#f9f5eb")
    st.plotly_chart(fig_poverty, use_container_width=True)

st.markdown("💡 Tip: Use the sidebar to filter states.")
