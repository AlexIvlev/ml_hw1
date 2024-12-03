## Usage

The easiest way to run the application is using Docker Compose.

### Prerequisites

Ensure you have Docker and Docker Compose installed (see: https://www.docker.com).

### Running the application with Docker Compose

1. Build and start the services with:
```
docker-compose up --build
```
2. After the services are up, the application will be accessible at http://localhost:8080.

3. Access the interactive API documentation via:

- **Swagger UI**: [http://localhost:8080/docs](http://localhost:8080/docs)
- **ReDoc**: [http://localhost:8080/redoc](http://localhost:8080/redoc)

### Auto-restart
If you make any changes to the code, Docker Compose will automatically rebuild and restart the server without you needing to manually stop and restart the containers.

### Stopping the services
To stop the running containers, use:

```
docker-compose down
```
