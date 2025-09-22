import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__) # Create a Flask application instance

@app.route("/api/v1/details") # Define the route for the root URL

def details():
   return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on  %B %D %Y"),
        'hostname': socket.gethostname()
   }) # Response displayed in the browser

@app.route("/api/v1/healthz") # Define the route for the root URL

def health():
   return jsonify({
        'status': 'up'
   }), 200 # Response displayed in the browser

if __name__ == "__main__":

   app.run(host="0.0.0.0") # Run the development server

#'/api/v1/details'
#'/api/v1/healthz'