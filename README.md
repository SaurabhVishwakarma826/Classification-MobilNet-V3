# Indian Sweet Classification using Transfer Learning with MobileNetV3

This project aims to classify Indian sweets using transfer learning with the MobileNetV3 Large model. The model is trained on a dataset containing images of various Indian sweet varieties.

## Overview

The project consists of the following components:

- **Scrap Data**: `scrapData.py` script for scrap data directly from google if you are unable to scrap the data directly download from [here](https://drive.google.com/file/d/1_U6wxKoALszTnXclzL8Fa3Ij8cYL_bVi/view?usp=sharing)
- **Spliting Dataset**: `split_dataset.py`: script for spliting dataset into training and validation
- **Training Script**: `transfer_learning_MobileNet-V3.ipynb` script for training the classification model using transfer learning with MobileNetV3 Large.
- **Predict Script**: `predict.py` script to predict sweet class directly by loading model
- **Flask App**: `app.py` Flask application with an API endpoint for image classification. Users can upload an image to classify the Indian sweet variety via API.
- **Templates interface**: `index.html` HTML file for a simple web interface allowing users to upload images for classification.

## Setup and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SaurabhVishwakarma826/Classification-MobilNet-V3.git
   cd Classification-MobilNet-V3
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Dataset:**

   - Run scrap_dataset.py this will scrap the dataset from google using selenium webscraping if you are unable to run the script then click [here](https://drive.google.com/file/d/1_U6wxKoALszTnXclzL8Fa3Ij8cYL_bVi/view?usp=sharing) to downlaod dataset

4. **Training the Model:**

   - Run the `transfer_learning_MobileNet-V3.ipynb` script to train the model using transfer learning.

   ```bash
   jupyter notebook
   ```

5. **Running the Flask App:**

   - Start the Flask app to provide the classification API endpoint.

   ```bash
   python app.py
   ```

6. **Accessing the Web Interface:**

   - Visit `http://localhost:5000` in your web browser to access the web interface.
   - Upload an image to classify the Indian sweet variety.

7. **Using the API Endpoint:**
   - Send a POST request to `http://localhost:5000/predict` with an image file attached to classify the Indian sweet variety.
   - The API will return the predicted class name.
