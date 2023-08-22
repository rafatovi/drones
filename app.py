from flask import Flask, request
from werkzeug.utils import secure_filename
import drones
import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os
from genre_detector import get_genre, load_model

app = Flask(__name__)
UPLOAD_FOLDER = './files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the pre-trained machine learning model
MODEL = load_model("./weights/model.json", "./weights/model_weights.h5")

@app.route('/drones', methods=['POST'])
def process_audio():
    # Check if the request contains a file
    if 'file' not in request.files:
        return 'No file provided', 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    # Predict the genre using the pre-trained machine learning model
    genre = get_genre(MODEL, file_path)

    # Make the corresponding drones.X() call based on the predicted genre
    
    if genre == 'classical':
        drones.classical()
    elif genre == 'country':
        drones.country()
    elif genre == 'disco':
        drones.disco()
    elif genre == 'hiphop':
        drones.hiphop()
    elif genre == 'jazz':
        drones.jazz()
    elif genre == 'metal':
        drones.metal()
    elif genre == 'reggae':
        drones.reggae()
    else:
        return 'Genre: ' + genre

@app.route("/")
def homedef():
    return "ola";
if __name__ == '__main__':
    print ("starting")
    app.run("0.0.0.0", 5000)
