from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Inventario Básico con Flask"


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = {"id": user_id , "name":"test", "telefono":"993-918-162"}
    # /user/434?query=query_test
    query= request.args.get("query")
    if(query):
        user["query"] = query
    
    return jsonify(user), 200


@app.route("/user", methods=["POST"])
def create_user():
    data= request.get_json()
    data["status"]="user created"

    return jsonify(data),201


if __name__ == '__main__':
    app.run(debug=True)
