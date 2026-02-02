from flask import Flask, request, jsonify
app = Flask(__name__)
DB = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tickets")
def create_ticket():
    body = request.get_json(force=True)
    iid = str(len(DB)+1)
    DB[iid] = {"id": iid, "status": "open", **body}
    return jsonify(DB[iid]), 201

@app.get("/tickets")
def list_tickets():
    return jsonify(list(DB.values()))

@app.put("/tickets/<id>")
def update_ticket(id):
    if id not in DB:
        return jsonify({"error": "Ticket not found"}), 404
    
    body = request.get_json(force=True)
    ticket = DB[id]
    
    if "status" in body:
        ticket["status"] = body["status"]
        
    return jsonify(ticket)

if __name__ == "__main__":
    app.run(debug=True)
