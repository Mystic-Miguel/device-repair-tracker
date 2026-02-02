# Device Repair Tracker

Flask+SQLite mini ticketing app for repair jobs.

> **Ethics/Safety**: Any security testing stays inside my own lab or with explicit permission.

## Getting Started

1. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## API Documentation

### Check Health
`GET /health`
Returns `{"status": "ok"}`

### Create Ticket
`POST /tickets`
Body: `{"title": "Broken Screen", "description": "iPhone 13 screen cracked"}`
Returns: Created ticket object

### List Tickets
`GET /tickets`
Returns: List of all tickets

### Update Ticket Status
`PUT /tickets/<id>`
Body: `{"status": "in_progress"}`
Returns: Updated ticket object
