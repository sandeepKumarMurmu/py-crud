from flask import Flask, request

app = Flask(__name__)

store = [{
        'name':'My Store',
        "items":[{
            "name":"product 1",
            "price": 25.23
        }]
}]

@app.get("/stores")
def getStore():
    return {"stores":store}