import asyncio
import asyncpg
import json
from fastapi import FastAPI,WebSocket,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__),"templates"))

async def stream_data(websocket:WebSocket):
     # Fetch environment variables
     db_user = os.getenv("DB_USER")
     db_password = os.getenv("DB_PASSWORD")
     db_host = os.getenv("DB_HOST")
     db_name = os.getenv("DB_NAME")
   
     #Establish an connection
     connection = await asyncpg.connect(
          user=db_user, password=db_password,
        host=db_host, database=db_name
     )
     
     try:
         async with connection.transaction():
            async for record in connection.cursor('SELECT * FROM student'):
                   # Serialize each record to JSON format
               json_data = json.dumps({"id": record['id'], "name": record['name'],"place":record['place'],"phone_number":record['phone_number'],"class":record['class']})
               # Send JSON data to the connected WebSocket client
               await websocket.send_text(json_data)  
               await asyncio.sleep(1) #delay the messages
               
     finally:
        # Close the database connection when done
        await connection.close()        
     
#Websocket endpoint for streaming the data
@app.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
     await websocket.accept()
     await stream_data(websocket)
     

#Explore page:
@app.get("/",response_class=HTMLResponse)
async def read_root(request: Request):
   return templates.TemplateResponse("explore.html", {"request": request})