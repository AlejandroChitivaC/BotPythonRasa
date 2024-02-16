from flask import Flask, render_template, request, Response
from flask_cors import CORS
from rasa.core.agent import Agent

app = Flask(__name__)
CORS(app)
rasa_agent = Agent.load("models")


# @app.route("/api")
# def home():
#     return render_template("index.html")
@app.route("/get_response", methods=["POST"])
async def get_response():
    user_message = request.form["user_message"]
    responses = await rasa_agent.handle_text(user_message)
    bot_response = responses[0]["text"]
    return {"response": bot_response}


if __name__ == "__main__":
    app.run(debug=True)
