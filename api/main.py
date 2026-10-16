from flask import Flask,jsonify,request
import json
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/drinks")
def return_drinks():
    return {"drink":"drank"}