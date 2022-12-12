from flask import Flask, jsonify, render_template
import uuid
# 1, 
instance_id = uuid.uuid4().hex
app = Flask(__name__)

@app.route("/")
def get_instance_id():
    return f"Instance ID: {instance_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)