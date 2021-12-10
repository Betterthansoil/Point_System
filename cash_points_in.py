from flask import Flask, request, jsonify
import json 

from flask.json import dumps

app = Flask(__name__)

simple_user_database = {
    'Master Moonlarkian':15,
    'yap30317' : 0,
    'faithyhuong' : 0,
    'Siti Jazmina Abd Rashid' : 0,
    'Tester' : 0,
    'nellytingshisiu' : 0,
    'ernernmooi' : 0,
    'bor' : 0
}

simple_prize_database = { 
    'Hoodie' : 1500 ,
    'Bottle' : 1000 ,
    'Notebook' : 1000 ,
    'Phone case' : 1700,
    'Custom Playing Cards' : 5000
 }

def prizeItems (item) :
    if item in simple_prize_database:
        # if item does exist, return the point
        return simple_prize_database [item]
    else:
        #if item doesn't exist, throw an error
        raise ValueError ("Category doesn/'t exist")

def deductPoints (user,points):
    #deduct points to existing points
    if user in simple_user_database:
        simple_user_database[user] -= points
    else:
        simple_user_database[user] = points
    
    return simple_user_database [user]

@app.route('/deduct')
def deductjson():
    user_points = (simple_user_database)
    json_dumps = json.dumps(user_points)
    return json_dumps


@app.route('/deduct', methods = ['POST'])
def deduct ():
        body = json.loads(request.data)
        result = deductPoints (body["item"] , body["points"])
        return jsonify (result) 
   


app.run()





