import streamlit as st
import requests
import plotly.graph_objs as go

st.set_page_config(page_title="ISS Position Tracker", page_icon="🛰️")

# Function to fetch the ISS position with error handling
def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        position = response.json()['iss_position']
        return float(position['latitude']), float(position['longitude'])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching ISS data: {e}")
        return None, None

# Streamlit App
def app():
    st.title("Live ISS Position Tracker")
    st.write("Press F5 to refresh the position.")

    latitude, longitude = get_iss_position()
    if latitude is not None and longitude is not None:
        # Create the Plotly map
        fig = go.Figure(go.Scattergeo(
            lon=[longitude],
            lat=[latitude],
            mode='markers',
            marker=dict(size=10, color='red'),
            name='ISS Position'
        ))
        fig.update_geos(projection_type="orthographic")
        fig.update_layout(
            title='Current ISS Position',
            geo_scope='world',
            geo=dict(
                showland=True,
                landcolor="rgb(243, 243, 243)",
                subunitcolor="rgb(217, 217, 217)",
                countrycolor="rgb(217, 217, 217)",
                projection_rotation=dict(lon=longitude, lat=latitude, roll=0)    
            ),
        )
        
        st.plotly_chart(fig)
        st.write(f"**Latitude:** {latitude}, **Longitude:** {longitude}")

if __name__ == "__main__":
    app()