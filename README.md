# Cheap Flight Finder

A Python-based flight price tracking project that searches for affordable flights between selected destinations and helps identify low-fare options.

## Features

* Search for available flight prices
* Compare flight prices for selected routes
* Use Google Flights data through SerpApi
* Convert and display prices in the required currency
* Store destination and tracking information
* Automate flight price checking
* Designed to be extended with notifications for price drops

## Technologies Used

* Python
* Requests
* SerpApi
* Google Flights API
* Sheety API
* Environment Variables
* REST APIs

## How It Works

```text
User / Flight Search
        ↓
Python Application
        ↓
SerpApi
        ↓
Google Flights Data
        ↓
Process Flight Information
        ↓
Compare Prices
        ↓
Display / Track Cheap Flights
```

## Project Structure

```text
Cheap-Flight-Finder/
│
├── main.py
├── flight_search.py
├── flight_data.py
├── data_manager.py
├── notification_manager.py
├── .env
├── .gitignore
└── README.md
```

> File names may differ depending on your current project structure.

## APIs Used

### SerpApi

Used to retrieve Google Flights search results and flight pricing information.

### Sheety

Used to store and manage destination/tracking information through a spreadsheet-based API.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/HaritSharma-07/Cheap-Flight-Finder.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create environment variables

Create a `.env` file and add your API credentials:

```env
SERPAPI_KEY=your_serpapi_key
SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password
```

Do not upload your real API keys or passwords to GitHub.

### 4. Run the project

```bash
python main.py
```

## Example

The program can search routes such as:

```text
Bangalore → Tokyo
Bangalore → Paris
Bangalore → London
```

The application retrieves available flight information and processes the prices so that cheaper options can be identified.

## Future Improvements

* Add automatic email notifications
* Add WhatsApp price alerts
* Track prices over time
* Add multiple departure airports
* Build a web interface
* Add scheduled automatic searches
* Store historical flight prices

## Learning Outcomes

Through this project, I practiced:

* Working with REST APIs
* Sending HTTP requests using Python
* Handling JSON responses
* Working with external API services
* Managing environment variables
* Processing and comparing data
* Automating repetitive tasks
* Building a practical Python application

## Author

**Harit Sharma**

B.Tech Computer Science Engineering

GitHub: [HaritSharma-07](https://github.com/HaritSharma-07)
