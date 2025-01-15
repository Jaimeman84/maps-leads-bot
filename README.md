# 🏪 Business Search Application

A Streamlit-based application that helps users search for businesses using the Google Maps API. The application provides a user-friendly interface to search for businesses based on various criteria and view detailed information about them.

## ✨ Features

- 🔍 Search for businesses by type, location, and keywords
- ⭐ Filter results by rating and price level
- 📋 View business details including ratings, address, website, and phone number
- 📊 Export search results to CSV
- 💾 Save and view search history
- 📱 Full-width results table for better readability
- 🎨 Custom styled interface with hidden Streamlit footer

## 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 🔑 Google Maps API key with Places API enabled
- 📦 pip (Python package installer)

## 🔑 Getting Your Google Maps API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Places API:
   - In the left sidebar, click on "APIs & Services" > "Library"
   - Search for "Places API"
   - Click on "Places API"
   - Click "Enable"
4. Create credentials:
   - In the left sidebar, click on "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "API key"
   - Your new API key will be displayed
5. (Optional but recommended) Restrict the API key:
   - In the credentials page, click on the newly created API key
   - Under "Application restrictions", choose "HTTP referrers"
   - Under "API restrictions", choose "Restrict key"
   - Select "Places API" from the dropdown
   - Click "Save"

## ⚙️ Installation and Setup

1. Clone this repository or download the source files:
```bash
git clone https://github.com/Jaimeman84/maps-leads-bot
cd maps-leads-bot
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google Maps API key:
```env
GOOGLE_MAPS_API_KEY=your_api_key_here
```

## 📁 Project Structure

```
business_search/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## 🚀 Running the Application

1. Make sure your virtual environment is activated

2. Start the Streamlit server:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## 📱 Using the Application

1. Enter your search criteria:
   - 🏢 Business Type (e.g., "restaurant", "cafe", "gym")
   - 📍 Location (e.g., "New York", "London")
   - 🔤 Additional Keywords (optional)
   - 🎯 Search Radius (1000-50000 meters)
   - ⭐ Minimum Rating (0-5 stars)
   - 💰 Maximum Price Level (1-4 dollar signs)
   - 🕒 Open Now option

2. View Results:
   - 📊 Results are displayed in a full-width table
   - 🔄 Click column headers to sort
   - 🔗 Click website links to visit business websites

3. Export and Save:
   - 📥 Use "Export to CSV" to download results
   - 💾 Use "Save Search Results" to keep results for later viewing

## ❗ Troubleshooting

Common issues and solutions:

1. **🔑 API Key Issues**
   - Error message about invalid API key: Verify your API key is correctly set in the `.env` file
   - No results: Ensure the Places API is enabled in your Google Cloud Console
   - Quota exceeded: Check your API usage in the Google Cloud Console

2. **⚙️ Installation Problems**
   - Package conflicts: Create a fresh virtual environment
   - Streamlit not found: Verify installation with `pip list`
   - Python version issues: Use Python 3.8 or higher

3. **🐞 Runtime Errors**
   - No results found: Try broadening your search criteria
   - Connection errors: Check your internet connection
   - Table display issues: Clear your browser cache

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- 🎨 Built with Streamlit
- 🗺️ Powered by Google Maps Platform
- 💡 Inspired by the need for an easy-to-use business search tool