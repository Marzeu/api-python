from flask import Flask, request
from database import insertUser

app = Flask("My API")


@app.route("/olamundo", methods=["GET"])
def hellWord():
    return {"ola": "mundo"}


@app.route("/cadastra/usuario", methods=["POST"])
def cadastrarUser():

    body = request.get_json()

    if("name" not in body):
        return getResponse(400, "name is required")

    if("email" not in body):
        return getResponse(400, "email is required")

    if("password" not in body):
        return getResponse(400, "password is required")

    user = insertUser(body["name"], body["email"], body["password"])

    return getResponse(200, "Created user", "user", user)


def getResponse(status, message, name_of_content=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if(name_of_content and content):
        response[name_of_content] = content

    return response


app.run()
