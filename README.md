# FlaskC2

FlaskC2 is a command and control (C2) server built with Flask, designed to manage and monitor multiple computers and clients from a centralized web interface. It provides a simple and intuitive way to remotely control and manage a network of machines, making it ideal for system administrators and IT professionals.

## Features

- **Centralized management:** Control multiple computers and clients from a single web interface.
- **Secure communication:** All communication between the server and clients is encrypted and authenticated.
- **Flexible architecture:** Easily extendable through custom plugins and modules.
- **Intuitive interface:** Simple and user-friendly interface for easy management of your network.

## Getting started

### Prerequisites

- Python 3.6 or higher
- Flask 1.1.2 or higher
- SQLAlchemy 1.4.0 or higher

### Installation

1. Clone the repository: `git clone https://github.com/Jeff53978/FlaskC2.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Create the database: `flask db migrate`
4. Start the server: `flask run`

### Usage

1. Open your web browser and go to `http://localhost:5000`
2. Monitor and manage your clients from the web interface

## Contributing

Contributions are welcome and appreciated! If you'd like to contribute to FlaskC2, please fork the repository and submit a pull request.

## License

FlaskC2 is released under the MIT License. See `LICENSE` for more information.
