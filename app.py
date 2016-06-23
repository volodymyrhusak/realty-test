# -*- coding: utf-8 -*-
import json
import ast
from flask import Flask, render_template, jsonify
# from flask.ext.googlemaps import GoogleMaps
# from flask.ext.googlemaps import Map
# import googlemaps
from coord import get_poligon_oblast, get_poligon_reg, get_object

app = Flask(__name__)
#GoogleMaps(app)
# AIzaSyBjkoKoHc_eFrrkP2cRbsAKO_3diK-ecQc

@app.route("/")
def mapview():

	with open('oblPoligons.json','r') as f: 
		poligons=json.dumps(f.read())

	with open('regPoligons.json','r') as f: 
		poligonsReg=json.dumps(f.read())
	with open('pointPoligons.json','r') as f:
		dictOdject=json.dumps(f.read())
    
	# poligons=json.dumps(get_poligon_oblast()[0])
	# poligonsReg=json.dumps(get_poligon_reg()[0])
    # with open('static/poligon.json','r') as f: 
    #     poligons=json.dumps(f.read())
    # print poligons
	# listObject=get_object()
	# print len(listObject)
	# dictOdject=[]
	# for x in listObject:
		# descr=x[0]
		# coord=x[1]
		# coord=list(ast.literal_eval(coord))
		# dictOdject['descr']=descr
		# dictOdject.append(coord)
		# print dictOdject
	
	# dictOdject=json.dumps(dictOdject)
	# with open('pointPoligons.json','w') as f: 
		# f.write(dictOdject)
	 # poligons=poligons, poligonsReg=poligonsReg, dictOdject=dictOdject
	return render_template('home.html',poligons=poligons, poligonsReg=poligonsReg, dictOdject=dictOdject)

if __name__ == "__main__":
	app.run(debug=True)

