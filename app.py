import streamlit as st
import pandas as pd
import requests
from typing import Dict, List
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the page with a proper title and icon
st.set_page_config(
    page_title="Business Search Application",
    page_icon="🏪",
    layout="wide"
)

# Hide Streamlit's default footer and add custom one
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Get API key from environment variables
DEFAULT_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', '')

# Function to format price level
def format_price_level(x):
    if isinstance(x, (int, float)):
        return "".join(["$" * int(x)])
    return "N/A"

# Function to perform the business search
def search_businesses(
    api_key: str,
    business_type: str,
    location: str,
    radius: int,
    min_rating: float,
    open_now: bool,
    max_price: int,
    keyword: str
) -> List[Dict]:
    """
    Search for businesses using the Google Places API
    Returns a list of business details matching the search criteria
    """
    # Construct the initial search URL
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_query = f"{business_type} in {location}"
    
    # Parameters for the API request
    params = {
        "query": search_query,
        "radius": radius,
        "key": api_key,
        "opennow": "true" if open_now else "false"
    }
    
    if keyword:
        params["keyword"] = keyword

    try:
        # Make the initial search request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for place in data.get('results', []):
            # Get detailed information for each place
            details_url = "https://maps.googleapis.com/maps/api/place/details/json"
            details_params = {
                "place_id": place['place_id'],
                "fields": "name,formatted_address,rating,user_ratings_total,types,website,formatted_phone_number,geometry,price_level",
                "key": api_key
            }
            
            details_response = requests.get(details_url, params=details_params)
            details_response.raise_for_status()
            details = details_response.json().get('result', {})
            
            # Filter categories for more relevant ones
            categories = [cat for cat in details.get('types', []) 
                        if cat not in ['point_of_interest', 'establishment', 'store']]
            
            # Create a result dictionary with business details
            result = {
                'name': details.get('name', 'N/A'),
                'category': ', '.join(categories) if categories else 'N/A',
                'rating': details.get('rating', 'N/A'),
                'user_ratings_total': details.get('user_ratings_total', 'N/A'),
                'address': details.get('formatted_address', 'N/A'),
                'website': details.get('website', 'N/A'),
                'phone': details.get('formatted_phone_number', 'N/A'),
                'price_level': details.get('price_level', 'N/A')
            }
            
            # Filter results based on minimum rating and maximum price
            if (result['rating'] != 'N/A' and float(result['rating']) >= float(min_rating) and
                (result['price_level'] == 'N/A' or 
                 (isinstance(result['price_level'], (int, float)) and 
                  int(result['price_level']) <= int(max_price)))):
                results.append(result)
        
        return results
    
    except requests.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
        return []

# Initialize session state for storing search results
if 'search_results' not in st.session_state:
    st.session_state.search_results = []

# Main title and description
st.title("🏪 Business Search Application")
st.markdown("""
This application helps you find businesses in your area based on various criteria.
Enter your search parameters below to get started.
""")

# Create a form for search parameters
with st.form("search_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        business_type = st.text_input("Business Type", "restaurant")
        location = st.text_input("Location", "New York")
        keyword = st.text_input("Additional Keywords (optional)")
    
    with col2:
        radius = st.slider("Search Radius (meters)", 1000, 50000, 5000, step=1000)
        min_rating = st.slider("Minimum Rating", 0.0, 5.0, 4.0, step=0.5)
        max_price = st.select_slider("Maximum Price Level", options=[1, 2, 3, 4], value=3)
        open_now = st.checkbox("Open Now", value=False)
    
    # API key input (use environment variable as default)
    api_key = st.text_input("Google Maps API Key", 
                           value=DEFAULT_API_KEY,
                           type="password")
    
    submitted = st.form_submit_button("Search")
    
    if submitted:
        if not api_key:
            st.error("Please provide a Google Maps API key")
        else:
            # Perform the search and store results in session state
            results = search_businesses(
                api_key, business_type, location, radius,
                min_rating, open_now, max_price, keyword
            )
            st.session_state.search_results = results

# Display search results
if st.session_state.search_results:
    st.subheader("Search Results")
    
    # Convert results to DataFrame for easier display
    df = pd.DataFrame(st.session_state.search_results)
    
    # Display the results in a table
    st.dataframe(
        df,
        column_config={
            "website": st.column_config.LinkColumn("Website"),
            "rating": st.column_config.NumberColumn(
                "Rating",
                help="Business rating out of 5",
                format="%.1f ⭐"
            ),
            "price_level": st.column_config.TextColumn(
                "Price Level",
                help="Price level from $ to $$$$"
            )
        },
        hide_index=True,
        use_container_width=True  # Makes the table use full width
    )
    
    # Update the price level display after showing the dataframe
    if 'price_level' in df.columns:
        df['price_level'] = df['price_level'].apply(format_price_level)
    
    # Export functionality
    if st.button("Export to CSV"):
        # Convert DataFrame to CSV
        csv = df.to_csv(index=False).encode('utf-8')
        
        # Create download button
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="business_search_results.csv",
            mime="text/csv"
        )
        
    # Save functionality (storing in JSON for this proof of concept)
    if st.button("Save Search Results"):
        # Get existing saved searches or initialize empty list
        saved_searches = json.loads(st.session_state.get('saved_searches', '[]'))
        
        # Add current search results
        saved_searches.append({
            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
            'results': st.session_state.search_results
        })
        
        # Store back in session state
        st.session_state.saved_searches = json.dumps(saved_searches)
        st.success("Search results saved successfully!")

# Display saved searches if any exist
if 'saved_searches' in st.session_state:
    saved_searches = json.loads(st.session_state.saved_searches)
    if saved_searches:
        st.subheader("Saved Searches")
        for i, search in enumerate(saved_searches):
            with st.expander(f"Search from {search['timestamp']}"):
                st.dataframe(
                    pd.DataFrame(search['results']),
                    hide_index=True,
                    use_container_width=True  # Makes saved search tables use full width too
                )

# Add credits
st.markdown("---")
st.markdown("Made with ❤️ by Jaime Mantilla, MSIT + AI")


if __name__ == "__main__":
    # You can add any initialization code here
    pass