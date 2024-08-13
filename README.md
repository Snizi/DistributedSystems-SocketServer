# Project README

## WebSocket Chat Server

### Overview
This project is a WebSocket-based chat server that allows clients to join chat rooms, send messages, and leave rooms. The server is capable of handling multiple clients simultaneously, enabling real-time communication within different chat rooms. The project is built using Python and employs threading for concurrent client management. It also integrates with a PostgreSQL database to manage users and messages.

### Features
- **WebSocket Handshake**: Handles WebSocket handshake to establish a connection with clients.
- **Room Management**: Allows users to join and leave chat rooms, and keeps track of which clients are in which rooms.
- **Message Broadcasting**: Broadcasts messages to all clients in a room.
- **Database Integration**: Stores user and message data in a PostgreSQL database.
- **Threaded Client Handling**: Manages multiple client connections simultaneously using threads.

### Project Structure
- **main.py**: The main server script. Handles client connections, WebSocket handshakes, message routing, and room management.
- **message_handlers.py**: Contains functions that interact with the PostgreSQL database to manage users, rooms, and messages.

### Setup and Installation

#### Prerequisites
- Python 3.x
- PostgreSQL

#### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Snizi/DistributedSystems-SocketServer
    cd https://github.com/Snizi/DistributedSystems-SocketServer
    ```

2. **Install dependencies**:
    Ensure you have all required Python packages installed:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up PostgreSQL Database**:
    - Create a PostgreSQL database.
    - Update the `connect()` function in `message_handlers.py` with your database credentials.
    - Initialize your database schema (tables for Users and Messages).

4. **Run the server**:
    ```bash
    python main.py
    ```
    The server will start running on `ws://0.0.0.0:8080`.