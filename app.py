from flask import Flask, request, jsonify, render_template
import os 
from predict import classify_image
from PIL import Image
import tempfile

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file.save(temp_file)
            temp_file.seek(0)
            resultText = classify_image(temp_file.name)
        
        return jsonify({'result': resultText})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def indexView():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
