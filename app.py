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
        model = tf.keras.models.load_model('model.h5')
        pred = np.argmax(model.predict(img1))
        
        if pred == 0:
            return render_template('Actinic_keratosis.html')
        elif pred == 1:
            return render_template('Basal_Cell_Carcinoma.html')
        elif pred == 2:
            return render_template('Vascular_Lesions.html')
        elif pred == 3:
            return render_template('Melanoma.html')
        elif pred == 4:
            return render_template('Melanocytic_Nevi.html')
        elif pred == 5:
            return render_template('Dermatofibroma.html')
        elif pred == 6:
            return render_template('Benign_Keratosis_Like_Lesions.html')
        
        print("pred",pred)
        return render_template("home.html")
        

if __name__ == "__main__":   
        app.run(host='0.0.0.0',
                port=8008,
                debug = True,                
                threaded=True)