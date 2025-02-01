
# 🌟 Day 92: Build Your Own Weather App with API Integration ✅

### 🎉 Today’s Highlights:

* **Weather Data Fetching:** Developed a weather app that fetches weather data from the Open-Meteo API based on your location (latitude & longitude).

* **Weather Code Translation:** Translated weather codes into human-readable descriptions to make the forecast more understandable.

* **Max & Min Temperature Display:** Displayed the maximum and minimum temperatures for the day in a clear and friendly format.

### 🔍 Key Concepts:

* **API Integration:** Integrated the Open-Meteo API to fetch real-time weather data based on latitude and longitude.

* **Dynamic Weather Code Mapping:** Mapped numeric weather codes to descriptive weather conditions (e.g., clear sky, cloudy).

* **JSON Parsing:** Extracted data from the API response and parsed it using the ```json``` module to display relevant details.

### 💪 Day 92 Challenge: Customize the starter code to display your local weather forecast with a user-friendly output.

**Steps:**

  1. Customize the latitude, longitude, and timezone for your area in the API request.

  2. Fetch and parse the weather data from the API.

  3. Convert the weather codes into descriptive text.

  4. Output the weather description along with the maximum and minimum temperatures for today.

### 💪 Common Challenges & Fixes:

* **Incorrect Weather Codes:**

     * **Issue:** Some weather codes weren't displaying as expected.
     * **Fix:** Corrected the mapping of weather codes to human-readable descriptions.

* **API Connectivity Issues:**

     * **Issue:** The API request sometimes failed due to connection issues.
     * **Fix:** Added error handling to catch and display API request failures.

* **Formatting Output:**

     * **Issue:** Weather data appeared cluttered or hard to read.
     * **Fix:** Used string formatting and clear output design to make the data more readable.
