import os 
from tensorflow.keras.preprocessing import image 
import numpy as np 
import tensorflow as tf 
import cv2

# get the list of categories :
categories = ['Balushahi', 'Besan ke Laddu', 'Jalebi', 'Kaju Katli', 'Modak', 'Peda', 'Rasgulla', 'Rasmalai', 'Soan Papdi']
categories.sort()

# load the saved model :
modelSavedPath = "./sweet_model.keras"
model = tf.keras.models.load_model(modelSavedPath)

# predict the image 

def classify_image(imageFile):
    x = []

    img = cv2.imread(imageFile)
    img = cv2.resize(img, (320, 320), interpolation=cv2.INTER_AREA)  # Resize image using OpenCV

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)

    # get the highest prediction value 
    categoryValue = np.argmax(pred, axis=1)
    categoryValue = categoryValue[0]
    
    print(categoryValue)

    result = categories[categoryValue]

    return result


# img_path = "G:/desktop/project/sweetClassification/besan ke laddu_96.jpg"
# resultText = classify_image(img_path)
# print(resultText)
#
# img = cv2.imread(img_path)
# img = cv2.putText(img , resultText, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
