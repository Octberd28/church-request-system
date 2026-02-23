# Request Management Microservice  
CS361 - Group 5 | Devs: Octavio & Thomas

## Overview
A REST API microservice for managing in-game action requests in a sci-fi space station text adventure game.  
Players submit requests (e.g., access restricted bays, repair systems), and a game administrator can approve or reject them.

---

## Endpoints & Communication Contract

### 1. Submit a Request
- **Method:** POST  
- **URL:** `/api/requests`  
- **Body (JSON):**
```json
{
    "title": "string",
    "description": "string",
    "requester": "string",
    "category": "string"
}


Response: JSON object with request details and unique request_id

Status Codes:
201 – success
400 – missing fields


Retrieve Requests

Method: GET
URL: /api/requests
Query Params: status (pending | approved | rejected)
Response: JSON array of request objects (newest first)
Status Codes:
200 – success
400 – invalid status

Update Request Status

Method: PUT
URL: /api/requests/{request_id}
Body (JSON):

{
    "status": "approved | rejected | pending",
    "approval_notes": "string (optional, max 500 chars)"
}

Response: JSON object of updated request

Status Codes:

200 – success
400 – invalid data
404 – request not found

Retrieve Single Request

Method: GET
URL: /api/requests/{request_id}

Response: JSON object of the requested ID

Status Codes:
200 – success
404 – request not found


import requests

# Submit a new request
response = requests.post('http://localhost:5000/api/requests', json={
    "title": "Access Engineering Bay",
    "description": "Repair life support systems",
    "requester": "Player_Captain_Sarah",
    "category": "game_action"
})
print(response.json())

# Retrieve pending requests
response = requests.get(
    'http://localhost:5000/api/requests',
    params={"status": "pending"}
)
print(response.json())

# Update a request
response = requests.put(
    'http://localhost:5000/api/requests/REQ-001',
    json={
        "status": "approved",
        "approval_notes": "Access granted."
    }
)
print(response.json())

Notes:

The microservice uses in-memory storage (no persistent database)
All timestamps are UTC ISO formatted
Maximum approval_notes length is 500 characters



![UML Sequence Diagram](UML.png)

