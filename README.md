# ISS Position Tracker

This Streamlit app displays the current position of the International Space Station (ISS).
It gets the latest ISS coordinates from the API `http://api.open-notify.org/iss-now.json`.

<p align="center">
<img src="/img/screenshot.png" alt="ISS Position Tracker">
</p>

## About This Project
This project was created as a learning exercise to explore Docker and containerized applications.


## Getting Started

### Installation & Usage

### Prerequisites
Ensure that **Docker** is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop/).

1. **Clone the Repository**
   ```sh
   git clone https://github.com/hanneskoessl/iss-tracker.git
   cd iss-tracker
   ```

2. **Start the Application**  
   Run the following command in the terminal to launch the app:
   ```sh
   docker-compose up -d --build
   ```

3. **Access the Application**  
   Open your web browser and visit:
   ```
   http://localhost:8501
   ```

4. **Stop the Application**  
   To stop the running containers, use:
   ```sh
   docker-compose stop
   ```

5. **Remove the Containers and Images**  
   To completely remove all containers and images created by the application, run:
   ```sh
   docker-compose down --rmi all
   ```