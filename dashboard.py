import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Ensure the page is wide and title is set
st.set_page_config(page_title="Climate Scope", page_icon="🌍", layout="wide")

st.markdown("""
<style>
/* Clean dark theme aesthetics */
div[data-testid="metric-container"] {
    background-color: #1E293B;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_weather_data.csv')
    df['last_updated']  = pd.to_datetime(df['last_updated'])
    df['date']          = df['last_updated'].dt.normalize()
    df['month']         = df['last_updated'].dt.month
    df['month_name']    = df['last_updated'].dt.strftime('%b')
    df['hour']          = df['last_updated'].dt.hour
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Ensure 'data/cleaned_weather_data.csv' exists.")
    st.stop()

# --- SIDEBAR NAV & FILTERS ---
st.sidebar.title("🌍 Climate Scope")
st.sidebar.markdown("**Global Weather Analytics**")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigation", [
    "> Overview", 
    "> Temperature", 
    "> Time Series Analysis",
    "> Extreme Events", 
    "> Regional Comparison"
])

st.sidebar.markdown("---")
st.sidebar.header("Global Filters")

all_countries = sorted(df['country'].dropna().unique())
selected_countries = st.sidebar.multiselect("Select Country(s)", all_countries, default=[])

months = sorted(df['month'].dropna().unique())
if len(months) > 1:
    month_range = st.sidebar.slider("Month Range (Jan-Dec)", min_value=int(min(months)), max_value=int(max(months)), value=(int(min(months)), int(max(months))))
else:
    month_range = (min(months), max(months)) if months else (1, 12)

# Filter dataset globally
filtered_df = df.copy()
if selected_countries:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]
if months:
    filtered_df = filtered_df[(filtered_df['month'] >= month_range[0]) & (filtered_df['month'] <= month_range[1])]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()


# --- PAGE INTERFACES ---

if page == "> Overview":
    st.title("Global Weather Overview")
    
    # KPI Cards
    col1, col2, col3 = st.columns(3)
    avg_temp = filtered_df['temperature_celsius'].mean()
    avg_precip = filtered_df['precip_mm'].mean()
    avg_wind = filtered_df['wind_mph'].mean()
    
    col1.metric("🌡️ Global Avg Temp (°C)", f"{avg_temp:.1f}")
    col2.metric("💧 Avg Precipitation (mm)", f"{avg_precip:.2f}")
    col3.metric("🌬️ Avg Wind Speed (mph)", f"{avg_wind:.1f}")
    
    st.markdown("---")
    
    st.markdown("---")
    st.subheader("💡 Key Insights")
    st.info("Temperature is the most spatially variable metric, driven primarily by latitude and climate zone. Global trends strongly follow seasonal variations, especially visible in the northern hemisphere.")
    


    
    # Interactive Choropleth Map
    st.subheader("Interactive Global Map")
    map_metric = st.selectbox("Select Metric to Visualize on Map:", 
                              ["temperature_celsius", "humidity", "wind_mph", "precip_mm"], 
                              format_func=lambda x: x.replace('_', ' ').title().replace('Celsius', '(°C)').replace('Mph', '(mph)').replace('Mm', '(mm)'))
    
    country_agg = filtered_df.groupby('country').agg({
        'temperature_celsius': 'mean',
        'humidity': 'mean',
        'wind_mph': 'mean',
        'precip_mm': 'mean',
        'iso_alpha': 'first'
    }).reset_index()
    
    # Dynamic color scale based on metric
    color_scale_map = {
        'temperature_celsius': px.colors.diverging.RdYlBu_r,
        'humidity': 'Teal',
        'wind_mph': 'Purples',
        'precip_mm': 'Blues'
    }

    fig_map = px.choropleth(
        country_agg, 
        locations="iso_alpha", 
        locationmode="ISO-3",
        color=map_metric, 
        hover_name="country",
        hover_data={"temperature_celsius": ':.1f', "humidity": ':.1f', "wind_mph": ':.1f', "precip_mm": ':.2f'},
        color_continuous_scale=color_scale_map[map_metric],
        title=f"Global Average {map_metric.replace('_', ' ').title()}"
    )
    fig_map.update_layout(margin={"r":0,"t":40,"l":0,"b":0}, geo=dict(showcoastlines=True, projection_type="equirectangular"))
    st.plotly_chart(fig_map)

elif page == "> Temperature":
    st.title("Temperature & Seasonal Trends")
    



    # Line Chart: Avg Temp by Month
    st.subheader("Average Temperature by Month")
    temp_trend = filtered_df.groupby(['month', 'country'])['temperature_celsius'].mean().reset_index()
    
    # Note: If there are too many countries, it becomes messy. Limit to top 10 if none selected globally.
    plot_countries = selected_countries if selected_countries else (temp_trend['country'].value_counts().head(10).index.tolist())
    temp_trend_subset = temp_trend[temp_trend['country'].isin(plot_countries)]
    
    fig_line = px.line(
        temp_trend_subset, x='month', y='temperature_celsius', color='country', markers=True,
        labels={"temperature_celsius": "Temp (°C)", "month": "Month"},
        title="Avg Monthly Temp"
    )
    fig_line.update_layout(hovermode="x unified")
    st.plotly_chart(fig_line)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Temperature Distribution")
        fig_hist = px.histogram(
            filtered_df, x="temperature_celsius", nbins=40, marginal="box", 
            title="Histogram + Box", color_discrete_sequence=['#ef553b']
        )
        st.plotly_chart(fig_hist)
        
    with col2:
        st.subheader("Correlation Heatmap")
        vars_corr = ['temperature_celsius', 'humidity', 'wind_mph', 'uv_index', 'precip_mm']
        corr_matrix = filtered_df[vars_corr].corr()
        fig_corr = px.imshow(
            corr_matrix, text_auto=".2f", aspect="auto",
            color_continuous_scale='RdBu_r', zmin=-1, zmax=1,
            title="Correlation Matrix"
        )
        st.plotly_chart(fig_corr)

    st.markdown("---")
    st.subheader("💡 Key Insights")
    st.info("UV Index and Temperature move together globally, both peaking in summer months. Humidity shows a moderate negative correlation with temperature indicating hotter regions tend to be drier.")

elif page == "> Time Series Analysis":
    st.title("Time Series & Rolling Averages")
    
    st.markdown("### Country Comparison Time Series")
    ts_countries = st.multiselect("Select Countries to Compare over Time", all_countries, default=selected_countries[:3] if selected_countries else ["United States of America", "India", "Brazil"])
    
    if ts_countries:
        ts_df = filtered_df[filtered_df['country'].isin(ts_countries)]
        daily_country_temp = ts_df.groupby(['date', 'country'])['temperature_celsius'].mean().reset_index()
        
        fig_ts_comp = px.line(
            daily_country_temp, x='date', y='temperature_celsius', color='country',
            labels={'temperature_celsius': 'Temperature (°C)', 'date': 'Date'},
            title="Daily Average Temperature Comparison",
            markers=True
        )
        fig_ts_comp.update_layout(hovermode="x unified")
        st.plotly_chart(fig_ts_comp)
    else:
        st.info("Select countries above to view the time series comparison.")
    
    st.markdown("### Multi-Metric Time Series")
    metric_choice = st.selectbox("Select Metric for Trend Analysis", ["humidity", "wind_mph", "uv_index", "precip_mm", "pressure_mb"])
    
    daily_metric = filtered_df.groupby('date')[metric_choice].mean().reset_index()
    daily_metric['7_Day_Rolling_Avg'] = daily_metric[metric_choice].rolling(window=7).mean()
    
    fig_metric = px.line(
        daily_metric, x='date', y=[metric_choice, '7_Day_Rolling_Avg'],
        labels={'value': f"{metric_choice.replace('_', ' ').title()}", 'variable': 'Metric', 'date': 'Date'},
        title=f"Global Daily Average {metric_choice.replace('_', ' ').title()} (7-Day Rolling)",
        color_discrete_sequence=['#9467bd', '#d62728']
    )
    fig_metric.update_layout(hovermode="x unified")
    st.plotly_chart(fig_metric)

    st.markdown("---")
    st.subheader("💡 Key Insights")
    st.info("Strong seasonal cycles are visible in mid-latitude countries, while near-equatorial zones show less monthly temperature variation.")

elif page == "> Extreme Events":
    st.title("Extreme Weather Events")
    
    st.markdown("### Identify Extreme Events")
    col1, col2, col3 = st.columns(3)
    heat_thresh = col1.slider("Extreme Heat Threshold (°C)", min_value=30.0, max_value=55.0, value=40.0, step=1.0)
    rain_thresh = col2.slider("Heavy Rain Threshold (mm)", min_value=1.0, max_value=100.0, value=20.0, step=1.0)
    wind_thresh = col3.slider("High Wind Threshold (mph)", min_value=10.0, max_value=150.0, value=30.0, step=1.0)
    
    event_type = st.radio("Select Event Type to View:", ["Extreme Heat", "Heavy Rain", "High Wind"], horizontal=True)
    
    if event_type == "Extreme Heat":
        ev_df = filtered_df[filtered_df['temperature_celsius'] >= heat_thresh]
        metric_col = 'temperature_celsius'
        color_s = 'Reds'
    elif event_type == "Heavy Rain":
        ev_df = filtered_df[filtered_df['precip_mm'] >= rain_thresh]
        metric_col = 'precip_mm'
        color_s = 'Blues'
    else:
        ev_df = filtered_df[filtered_df['wind_mph'] >= wind_thresh]
        metric_col = 'wind_mph'
        color_s = 'Purples'
        
    if ev_df.empty:
        st.warning(f"No {event_type} events found with the given threshold and filters.")
    else:
        st.subheader(f"Map: Locations of {event_type}")
        fig_geo = px.scatter_geo(
            ev_df, lat='latitude', lon='longitude', color=metric_col,
            hover_name='location_name', hover_data=['country', metric_col, 'date'],
            color_continuous_scale=color_s, size=metric_col,
            title=f"{event_type} Map"
        )
        st.plotly_chart(fig_geo)
        
        col_b, col_t = st.columns([1, 1])
        with col_b:
            st.subheader(f"Distribution ({metric_col})")
            fig_box = px.box(ev_df, x='country', y=metric_col, title=f"Box Plot by Country")
            st.plotly_chart(fig_box)
            
        with col_t:
            st.subheader("Top Events")
            top_events = ev_df[['country', 'location_name', metric_col, 'date']].sort_values(by=metric_col, ascending=False).head(10)
            st.dataframe(top_events, hide_index=True)

    st.markdown("---")
    st.markdown("### 🚨 Statistical Anomaly Detection (Z-Score)")
    st.markdown("Detect anomalous events based on statistical deviations (Z-score > 2.5) compared to country baselines.")
    
    anomaly_metric = st.selectbox("Select Metric for Anomaly Detection", ["temperature_celsius", "humidity", "wind_mph", "precip_mm"], index=0)
    
    anomaly_df = filtered_df.copy()
    
    def calc_zscore(x):
        if x.std() == 0 or pd.isna(x.std()):
            return pd.Series(0, index=x.index)
        return (x - x.mean()) / x.std()

    anomaly_df['z_score'] = anomaly_df.groupby('country')[anomaly_metric].transform(calc_zscore)
    anomaly_df['is_anomaly'] = anomaly_df['z_score'].abs() > 2.5
    
    anomalies = anomaly_df[anomaly_df['is_anomaly']]
    
    if anomalies.empty:
        st.success(f"No statistical anomalies detected for {anomaly_metric} in the current selection.")
    else:
        st.warning(f"Found {len(anomalies)} anomalies for {anomaly_metric}!")
        st.dataframe(anomalies[['country', 'location_name', 'date', anomaly_metric, 'z_score']].sort_values(by='z_score', key=abs, ascending=False).head(15))

    st.markdown("---")
    st.subheader("💡 Key Insights")
    st.info("Extreme weather events (heat, rain, wind) are geographically clustered, not random. Precipitation is highly irregular and skewed — rare but extreme events dominate totals in monsoon regions.")

elif page == "> Regional Comparison":
    st.title("Regional Comparison")
    
    sel_countries = st.multiselect(
        "Select Countries to Compare", 
        options=all_countries, 
        default=["India", "United States of America", "Brazil", "Russia", "Australia"] if len(all_countries) > 5 else all_countries[:5]
    )
    
    metric_map = {
        "Temperature (°C)": "temperature_celsius",
        "Humidity (%)": "humidity",
        "Precipitation (mm)": "precip_mm",
        "Wind Speed (mph)": "wind_mph"
    }
    sel_metric_label = st.selectbox("Select Metric", options=list(metric_map.keys()))
    sel_metric = metric_map[sel_metric_label]
    
    if sel_countries:
        comp_df = filtered_df[filtered_df['country'].isin(sel_countries)]
        
        if comp_df.empty:
            st.warning("No data for these countries.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"Average {sel_metric_label} by Country")
                agg_comp = comp_df.groupby('country')[sel_metric].mean().sort_values(ascending=True).reset_index()
                fig_bar = px.bar(
                    agg_comp, x=sel_metric, y='country', orientation='h', color=sel_metric,
                    color_continuous_scale='Viridis'
                )
                st.plotly_chart(fig_bar)
            
            with col2:
                st.subheader(f"Distribution of {sel_metric_label}")
                fig_violin = px.violin(
                    comp_df, x='country', y=sel_metric, color='country', 
                    box=True, points="all"
                )
                st.plotly_chart(fig_violin)
                
            st.subheader("Interactive Temperature vs Humidity")
    
            scatter_size_metric = st.selectbox("Select Bubble Size Metric:", ["wind_mph", "precip_mm", "uv_index"], format_func=lambda x: x.replace('_', ' ').title())
            
            fig_scatter = px.scatter(
                comp_df, x="temperature_celsius", y="humidity", color="country",
                size=scatter_size_metric, size_max=40,
                hover_name="location_name",
                hover_data={"temperature_celsius": ':.1f', "humidity": ':.1f', scatter_size_metric: True},
                opacity=0.7,
                title=f"Temp vs Humidity (Size: {scatter_size_metric.replace('_', ' ').title()})"
            )
            st.plotly_chart(fig_scatter)

    st.markdown("---")
    st.subheader("💡 Key Insights")
    st.info("Regional comparisons highlight distinct climate groupings: equatorial countries dominate top temperatures while coastal/island nations lead in humidity and precipitation.")

