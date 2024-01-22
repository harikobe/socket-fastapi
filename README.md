
# Socket-FastAPI

This project features a simple WebSocket implementation in FastAPI to retrieve data from a PostgreSQL database in JSON format.

## FastAPI with PostgreSQL and pgAdmin using Docker Compose

This Docker Compose configuration sets up a development environment with FastAPI, PostgreSQL, and pgAdmin.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/harikobe/socket-fastapi.git
   ```

2. Create an `.env` file:

   ```env
   # .env
   DB_USER=myuser
   DB_PASSWORD=mypassword
   DB_NAME=mydatabase

   PGADMIN_EMAIL=admin@example.com
   PGADMIN_PASSWORD=adminpassword
   ```

3. Start the services:

   ```bash
   docker-compose up -d
   ```

### Note

- You need to create the data in pgAdmin before accessing the FastAPI at http://127.0.0.1:8000.
- Make adjustments in the `app.py` file:

   ```python
   async for record in connection.cursor('SELECT * FROM student'):
   ```

   Change the table name according to the table created.

   ```python
   json_data = json.dumps({
       "id": record['id'],
       "name": record['name'],
       "place": record['place'],
       "phone_number": record['phone_number'],
       "class": record['class']
   })
   ```

   Adjust the keys and values with the columns of the table you created.

- `client.py` will work if you mention it in the Dockerfile and compose file.

### Result

An HTML page with the heading of "Data" will display the data from pgAdmin in JSON format.
```


