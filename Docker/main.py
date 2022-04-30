import socket
from flask import Flask, render_template, request, redirect, url_for, session
from requests import get
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def proxy_client():
    headers = request.headers
    return "Request headers:\n" + str(headers)

@app.route('/proxy-client_x')
def proxy_client_x():
    ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
    return '<h1> Your IP address is:' + ip_addr
