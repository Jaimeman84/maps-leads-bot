# Business Search Application

A Streamlit-based application for searching and analyzing businesses using the Google Maps API.

## Prerequisites

- Python 3.8 or higher
- Google Maps API key with Places API enabled

## Setup Instructions

1. Clone the repository or download the source files

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Configure the environment:
- Copy the `.env.example` file to `.env`
- Add your Google Maps API key to the `.env` file
- Modify other configuration options as needed

## Project Structure

```
business_search/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create from .env.example)
└── README.md             # Project documentation
```

## Running the Application

1. Make sure your virtual environment is activated

2. Start the Streamlit server:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Features

- Search for businesses based on various criteria
- Filter results by rating and price level
- Export search results to CSV
- Save and view search history
- User-friendly interface

## Google Maps API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Places API for your project
4. Create credentials (API key)
5. Add the API key to your `.env` file

## Troubleshooting

Common issues and solutions:

1. **API Key Issues**
   - Ensure your API key is correctly set in the `.env` file
   - Verify that the Places API is enabled in your Google Cloud Console
   - Check if your API key has any restrictions that might prevent it from working

2. **Installation Problems**
   - Make sure you're using Python 3.8 or higher
   - Try upgrading pip: `pip install --upgrade pip`
   - If you encounter package conflicts, try creating a fresh virtual environment

3. **Application Errors**
   - Check the console for error messages
   - Verify that all required environment variables are set
   - Ensure you have an active internet connection

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.