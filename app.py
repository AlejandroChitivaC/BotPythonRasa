from flask import Flask, render_template, request
from rasa.core.agent import Agent

app = Flask(__name__)
rasa_agent = Agent.load("models")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
async def get_response():
    user_message = request.form["user_message"]
    responses = await rasa_agent.handle_text(str(user_message))
    bot_response = responses[0]["text"]
    return {"response": bot_response}
# async def get_response():
#     user_message = request.form["user_message"]
#     responses = await rasa_agent.handle_text(str(user_message))
#
#     # Obtén la respuesta del bot
#     bot_response = responses[0]["text"]
#
#     # Obtén los botones, si están disponibles
#     buttons = responses[0].get("buttons", [0])
#
#     return {"response": bot_response, "buttons": buttons}


if __name__ == "__main__":
    app.run(debug=True)
