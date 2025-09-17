import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ===== Asistente Virtual Axi =====
class Axi:
    def __init__(self):
        self.tareas = []
        self.calendario = {}
        self.correos = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        return f"Tarea '{tarea}' añadida ✅"

    def ver_tareas(self):
        return self.tareas if self.tareas else ["No tienes tareas pendientes."]

axi = Axi()

# ===== Rutas de la app =====
@app.route("/")
def home():
    return "👋 Hola, soy Axi, tu asistente virtual!"

@app.route("/tarea", methods=["POST"])
def tarea():
    data = request.get_json()
    return jsonify({"respuesta": axi.agregar_tarea(data.get("tarea", ""))})

@app.route("/tareas", methods=["GET"])
def tareas():
    return jsonify({"tareas": axi.ver_tareas()})

# ===== Ejecutar app en Render =====
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Puerto que Render asigna
    app.run(host="0.0.0.0", port=port)
