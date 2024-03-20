from flask import Flask, request, jsonify
import os 
from predict import classify_image

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        img_path = "temp_image.jpg"
        file.save(img_path)
        resultText = classify_image(img_path)
        os.remove(img_path)  # Remove temporary image file
        return jsonify({'result': resultText})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
