flask
from flask import Flask, request, jsonify
from axi_core import Axi

app = Flask(__name__)
axi = Axi()

@app.route("/axi", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    response = axi.process(user_message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from integrations import calendar, email, tasks, research, docs, projects, comms, reminders

class Axi:
    def __init__(self):
        self.name = "Axi"

    def process(self, message: str) -> str:
        msg = message.lower()
        if "calendario" in msg or "cita" in msg:
            return calendar.handle(message)
        elif "correo" in msg:
            return email.handle(message)
        elif "tarea" in msg:
            return tasks.handle(message)
        elif "investiga" in msg or "buscar" in msg:
            return research.handle(message)
        elif "documento" in msg:
            return docs.handle(message)
        elif "proyecto" in msg:
            return projects.handle(message)
        elif "llamada" in msg or "mensaje" in msg:
            return comms.handle(message)
        elif "recordatorio" in msg:
            return reminders.handle(message)
        else:
            return f"Soy {self.name}. Puedo ayudarte con calendario, correos, tareas, documentos, proyectos, mensajes y recordatorios."
# Archivo vacío, sirve para que Python reconozca la carpeta como un paquete
def handle(message: str) -> str:
    if "agendar" in message.lower():
        return "He agendado tu cita en el calendario 📅 (simulado)."
    elif "mostrar" in message.lower():
        return "Tus próximas citas: reunión lunes a las 10 AM."
    return "¿Quieres agendar o mostrar citas en el calendario?"
def handle(message: str) -> str:
    if "enviar" in message.lower():
        return "Correo enviado 📧 (simulado)."
    elif "leer" in message.lower():
        return "Tienes 2 correos nuevos: uno de tu jefe y otro de la universidad."
    return "¿Quieres enviar o leer correos?"
def handle(message: str) -> str:
    if "agregar" in message.lower():
        return "He agregado una nueva tarea ✅ (simulado)."
    elif "listar" in message.lower():
        return "Tus tareas: 1) Terminar informe 2) Reunión mañana 3) Comprar material."
    return "¿Quieres agregar o listar tareas?"
def handle(message: str) -> str:
    return "Estoy investigando en línea 🔎 (simulado, aquí podrías conectar una API real)."
def handle(message: str) -> str:
    return "He organizado tus documentos en carpetas por fecha 📂 (simulado)."
def handle(message: str) -> str:
    return "He actualizado el estado de tu proyecto 🚀 (simulado)."
def handle(message: str) -> str:
    if "llamada" in message.lower():
        return "He iniciado una llamada 📞 (simulado)."
    elif "mensaje" in message.lower():
        return "He enviado un mensaje 💬 (simulado)."
    return "¿Quieres hacer una llamada o enviar un mensaje?"
def handle(message: str) -> str:
    if "crear" in message.lower():
        return "He creado un recordatorio ⏰ (simulado)."
    elif "mostrar" in message.lower():
        return "Tus recordatorios: 1) Reunión mañana 2) Llamar al médico."
    return "¿Quieres crear o mostrar recordatorios?"
