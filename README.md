# Public Bus Location Tracking POC

This is a Python project that serves as a Proof of Concept (POC) for adding location tracking to public buses, aiming to make public transportation more accessible and efficient while reducing waiting times at bus stops.

## Overview

The project utilizes the Flask web framework and MongoDB for data storage. It allows users to log in, track bus locations, and manage bus seating information. Below, you'll find an explanation of the main components and functionalities of the project.

## Features

### User Authentication

- Users can log in with their email and password.
- The session is used to keep users authenticated.

### Bus Location Tracking

- Bus location data is collected and stored in MongoDB.
- The `/post` endpoint allows for posting bus location data (latitude and longitude).

### Conductor Dashboard

- Conductor-specific functionalities are available.
- The `/cbuses` and `/cbuses/r` endpoints are for managing bus seating information.

### Admin Dashboard

- Administrators (e.g., admin@gmail.com) can access the admin dashboard.
- The `/locs` and `/buses` endpoints provide access to location and seating data, respectively.

### API Endpoint

- The `/api/test` endpoint serves as a simple test API.

## Dependencies

The project uses the following dependencies:

- Flask: A micro web framework for Python.
- Flask-PyMongo: Extension for Flask that simplifies MongoDB integration.

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/public-bus-tracking.git
   cd public-bus-tracking
   ```

2. Install the required dependencies:

   ```
   pip install Flask flask-pymongo
   ```

3. Start the Flask application:

   ```
   python app.py
   ```

The application should now be running locally on `http://localhost:5000`.

## Usage

1. Visit `http://localhost:5000` in your web browser.
2. Log in using your email and password.
3. Explore the various functionalities of the application.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. We welcome contributions from the community.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author

- Your Name
- Contact: your.email@example.com

Feel free to contact the author with any questions or feedback regarding this project.
