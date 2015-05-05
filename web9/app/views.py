from flask import render_template
from flask import Flask, request, abort
from app import app

import hashlib
import time
@app.route('/',methods = ['GET', 'POST'])
def index():
	gw_address = request.args.get('gw_address')
	gw_port = request.args.get('gw_port')
	m = hashlib.md5();
	tt = time.time()
	tem = '%d' %tt
	m.update(tem);
	token = m.hexdigest()
	url = "http://"+gw_address+":"+gw_port+"/wifidog/auth?token="+token
	return render_template("index.html",url=url)


@app.route('/login',methods = ['GET'])
def login():
	gw_address_1 = request.args.get('gw_address')
	gw_port_1 = request.args.get('gw_port')
	return render_template("login.html",gw_address_1=gw_address_1,gw_port_1=gw_port_1)

@app.route('/ping')
def ping():
	return 'Pong'


@app.route('/auth')
def auth():
	return 'Auth: 1\nMessages: Allow Access\n';


@app.route('/portal')
def portal():
	return render_template("portal.html")
