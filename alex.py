from flask import Flask, render_template, request, redirect, session, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import PIL
import os
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/home", methods = ["POST","GET"])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    
    if request.method == 'POST':
        print("Sample Image")
        img1 = request.files['img']
        print(img1,"Uploaded Image")        
        filename = img1.filename
        print(filename,os.getcwd())
        img1.save(os.path.join(os.getcwd(), filename))
        img1 = image.load_img(os.getcwd()+os.path.sep+filename,target_size=(128,128))
        img1 = image.img_to_array(img1)
        img1 = np.expand_dims(img1,axis=0)
        model = tf.keras.models.load_model('alexmodel.h5')
        pred = np.argmax(model.predict(img1))
        print("pred",pred)
        return render_template("home.html")
        

if __name__ == "__main__":   
        app.run(host='0.0.0.0',
                port=8008,
                debug = True,                
                threaded=True)