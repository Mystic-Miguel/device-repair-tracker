from flask import Flask, request, jsonify
app = Flask(__name__)
DB = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items")
def create_item():
    body = request.get_json(force=True)
    iid = str(len(DB)+1)
    DB[iid] = {"id": iid, **body}
    return jsonify(DB[iid]), 201

@app.get("/items")
def list_items():
    return jsonify(list(DB.values()))

if __name__ == "__main__":
    app.run(debug=True)
