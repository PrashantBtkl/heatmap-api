# takes json input from frontend and send it to db
from flask import Flask 
from flask_cors import CORS
import db
app = Flask(__name__) #creating the Flask class object


cors = CORS(app, resources={r"/*": {"origins": "*"}}) 
   
@app.route('/get_xy/<page_id>',methods = ['GET'])
def mapping(page_id):
	conn = db.get_conn()

	try:
		res = db.get_positions(page_id, conn)
	except Exception as e:
		print("exception occured :", e)
	finally:
		conn.close()

	# response should be like this -> [{ x: 10, y: 15, value: 5}, { x: 50, y: 50, value: 2}, ...]
	hmap_conf = []
	hmap_set = set()

	#Build heatmap config
	for coord in res:
		X = coord[0]
		Y = coord[1]

		xy = (X, Y)
		if xy in hmap_set:
			for conf in hmap_conf:
				if conf["id"] == xy:
					val = conf["value"] + 1
					xy = {"id":xy, "x": X, "y": Y, "value": val}
					conf.update(xy)
		else:
			hmap_set.add(xy)
			xy = {"id":xy, "x": X, "y": Y, "value": 1}
			hmap_conf.append(xy)

	#delete redundant json key
	for conf in hmap_conf:
		conf.pop("id")

	return { "data" : hmap_conf}
	

if __name__ =='__main__':  
    app.run(debug = True)