# Fourteen Factors

The 12-factor app paradigm is correct but incomplete. The 12-factor approach views the app as entirely atomic, expressly excluding the design of distributed systems into which this app fits. The premise is that a 12-factor style will create apps that can be neatly integrated in this way.

Since the development of 12-factor, the rise of AI - and in particular, agentic AI - necessitates that even an atomic view of apps must account for how they might integrate into both a distributed system and an AI-centric system.

In my view, this means the addition of two particular aspects to the 12-factor paradigm:

1. **Comprehensive API Exposure**
    - Every app must expose its core functionality via a comprehensive API. This enables AI to "put its hands on the steering wheel".

2. **High-Performance Data Extraction Interface**
    - Every app must enable a high-performance data extraction interface, possibly via the API directly but more optimally through a high-performance interface where access and permissioning is granted through the API. For AI, data streams are the equivalent of a UI for humans. Without this data stream, it's very hard to put control of the app in the hands of AI.

## Flask + HTMX + Socket.IO Example

This project demonstrates a basic Flask web application that adheres to these enhanced principles by providing comprehensive API exposure and enabling real-time data extraction via WebSocket. It includes:

- A web interface for displaying and adding items with dynamic updates using HTMX.
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
    python3 -m venv venv14
    ```

3. **Activate the virtual environment:**
    - On macOS and Linux:
      ```sh
      source venv14/bin/activate
      ```
    - On Windows:
      ```sh
      venv14\Scripts\activate
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
