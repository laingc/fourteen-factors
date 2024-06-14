# Flask + HTMX + Socket.IO Example

This project demonstrates a basic Flask web application with real-time updates using HTMX and Socket.IO. It includes an API for programmatically controlling the app and a client application that subscribes to the WebSocket for real-time data analysis.

## Features

- Display and add items to a list with dynamic updates using HTMX.
- Real-time updates via WebSocket using Flask-SocketIO.
- API endpoints to interact with the application programmatically.
- A separate Python client application to subscribe to WebSocket updates for data analysis.

## Quickstart

### Prerequisites

- Python 3.x
- Virtual environment tool (optional but recommended)

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/flask-htmx-socketio-example.git
    cd flask-htmx-socketio-example
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv venv_2024-06-14_12.factor.app.extension.example_
    ```

3. **Activate the virtual environment:**
    - On macOS and Linux:
      ```sh
      source venv_2024-06-14_12.factor.app.extension.example_/bin/activate
      ```
    - On Windows:
      ```sh
      venv_2024-06-14_12.factor.app.extension.example_\Scripts\activate
      ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Flask application:**
    ```sh
    python app.py
    ```

6. **Open your browser and go to `http://127.0.0.1:5000/`:**
    - This will load the page with the item list and the form to add new items.
    - Any added items will appear in real-time for all connected clients.

7. **Run the separate Python client application:**
    ```sh
    python client.py
    ```
    - This client subscribes to WebSocket updates and prints any changes to the application state in real-time.

## API Endpoints

- **Get all items:**
    ```sh
    GET /api/items
    ```

- **Add a new item:**
    ```sh
    POST /api/items
    {
        "item": "New Item"
    }
    ```

- **Delete an item by ID:**
    ```sh
    DELETE /api/items/<item_id>
    ```

- **Get WebSocket URL:**
    ```sh
    GET /api/socket
    ```

## License

This project is licensed under the MIT License.
