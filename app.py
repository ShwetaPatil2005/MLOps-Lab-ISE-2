
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

INVENTORY = [
    {"item": "Laptop", "stock": 12, "minimum": 5},
    {"item": "Keyboard", "stock": 3, "minimum": 5},
    {"item": "Mouse", "stock": 18, "minimum": 8},
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SmartShelfX Inventory Monitor</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f3f6fa; }
        h1 { color: #183153; }
        table { border-collapse: collapse; width: 100%; background: white; }
        th, td { padding: 14px; border: 1px solid #ddd; text-align: left; }
        th { background: #183153; color: white; }
        .low { color: #c62828; font-weight: bold; }
        .ok { color: #218838; font-weight: bold; }
    </style>
</head>
<body>
    <h1>SmartShelfX Inventory Monitor</h1>
    <p>CI/CD Lab ISE 2 — Flask Web Application</p>
    <table>
        <tr><th>Item</th><th>Stock</th><th>Minimum Stock</th><th>Status</th></tr>
        {% for x in inventory %}
        <tr>
            <td>{{ x.item }}</td><td>{{ x.stock }}</td>
            <td>{{ x.minimum }}</td>
            <td class="{{ 'low' if x.stock < x.minimum else 'ok' }}">
                {{ 'Low Stock' if x.stock < x.minimum else 'In Stock' }}
            </td>
        </tr>
        {% endfor %}
    </table>
    <p>Health check: <a href="/health">/health</a></p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, inventory=INVENTORY)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
