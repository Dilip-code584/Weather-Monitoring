
Real-Time Weather Monitoring System with Rollups and Aggregates

Use weather_monitor.py for this

![image](https://github.com/user-attachments/assets/cd5a0087-5222-4360-bdc7-0b23335eeb38)

![image](https://github.com/user-attachments/assets/2158a159-ed90-4c2d-af06-2bbef6c553a6)

With Average Temperature(Please Use Weather_monitor1.py for this, I've used the same filename with different code)
![image](https://github.com/user-attachments/assets/83581646-6b41-45da-9582-215363d5b778)

![image](https://github.com/user-attachments/assets/43b47440-1879-4ede-9a93-28b84f2c216c)


This project is a real-time data processing system that monitors weather conditions across major metropolitan cities in India. Using data from the OpenWeatherMap API, it retrieves, processes, and summarizes weather data at configurable intervals, providing useful insights via rollups and aggregates.

Features✨
Real-time weather data: Continuously fetches weather data for major Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).

Configurable polling interval: Set how frequently the system retrieves new weather data (e.g., every 30 seconds).

Weather metrics: Focuses on key weather parameters such as temperature, humidity, wind speed, and atmospheric pressure.

Rollups and aggregates: Summarized insights such as average, minimum, and maximum values over time for easy analysis.(Additional Functionalities)

Security Points:✨
API Key Management:

Store the API key in environment variables (.env file), not hardcoded in the source code.
Use libraries like python-dotenv to securely load the API key into the application.
Regenerate API keys periodically and limit the scope/permissions of the key where possible.
Rate Limiting:

Implement rate-limiting logic to avoid exceeding the OpenWeatherMap API's quota. Consider caching results for a short period to avoid redundant requests.
Data Sanitization:

Sanitize and validate inputs, such as city names or user inputs (if applicable) to prevent injection attacks or malformed requests.
Secure Web Access (Optional Web Interface):

If you develop a web-based dashboard (Flask/Django), ensure HTTPS is used.
Implement strong session management, and secure cookies (HttpOnly, Secure, etc.).
Sensitive Data Protection:

If storing weather data for a longer term (in databases like SQLite/PostgreSQL), ensure the database is properly secured with authentication and encryption.
Access Control:

Limit access to certain functionalities (e.g., admin features) and protect the interface using proper authentication mechanisms.
Performance Points:✨
Efficient Data Fetching:

Use asynchronous programming (e.g., asyncio, aiohttp) to fetch weather data concurrently for multiple cities rather than sequentially.
Minimize redundant API calls by caching weather data for a configurable duration.
Database Optimization (Optional):

If you store data for historical analysis, ensure the database schema is optimized for time-series data. Use appropriate indexing for faster queries on weather data.
Load Balancing (Optional Web Interface):

If scaling the application with a web interface, implement load balancing to distribute incoming requests across multiple instances for better performance.
Optimize Data Processing:

Use pandas for efficient data processing and summarization of weather data (min, max, average) across time intervals.
Batch-process large amounts of data rather than processing each weather record individually to reduce overhead.
Resource Management:

Limit system resource usage by setting configurable timeouts for API calls and offload intensive tasks (like aggregating historical data) to background workers (e.g., Celery).
Concurrency & Scheduling:

Use task scheduling libraries (e.g., Celery, APScheduler) to ensure weather data is retrieved efficiently and at consistent intervals without blocking the main application thread.

Tech Stack✨
Python 3: Core programming language.

OpenWeatherMap API: Data source for weather conditions.

SQLite3/PostgreSQL: Database for storing weather data (optional, if long-term storage or rollups are needed).

Pandas: For processing and aggregating data.

Flask/Django (Optional): Web interface for displaying summarized data.

Celery (Optional): For scheduling periodic data retrieval.


Installation✨
Clone the repository:

cd weather-monitoring-system

Create a virtual environment and install dependencies:

to run it via virtual environment 

python3 -m venv venv

source venv/bin/activate


Get your free API key from OpenWeatherMap.

Create a .env file in the root directory and add your API key:

API_KEY=your_openweathermap_api_key

Usage

Configure cities and polling interval: Edit the config.py file to customize the list of cities and how often data is retrieved.

Run the application:

python weather_monitor.py

This will start the system, which will retrieve weather data at regular intervals as defined in the configuration.

View rollups and aggregates: Insights such as average temperature, humidity trends, and more will be available in the terminal or the optional web interface.

Example

Cities monitored: ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
Polling interval: 30 seconds


Roadmap
Add support for more cities and weather parameters.

Implement historical data storage and analysis using databases.

Develop a web-based dashboard using Flask/Django to visualize data.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! Please submit pull requests for any enhancements or bug fixes.
