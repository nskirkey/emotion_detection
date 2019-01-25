# emotion.py by Nicolas Skirkey
# 8/15/207
# CIS 527 Final Project
# This emotion detector uses Microsoft Emotion API for facial recognition and
# Emotion detection. It is able to detect the 7 basic emotions on multiple 
# faces in pictures. These emotions include fear, contempt, sadness, happiness,
# surprise, neutral, and disgust. It uses cv2 to handle drawing the result on 
# picture and display.

from __future__ import print_function
import sys
import time 
import requests
import operator
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Microsoft Emotion API subscription key
_key = '2354b8a908bf4cb085eb64c242741852'

# URL to sent HTTP request to
_url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'

# Handle HTTP request & obtain result
def handleRequest(data, headers):
    retries = 0
    maxRetries = 5

    while True:
        response = requests.request('POST', _url, data = data, headers = headers)

        if response.status_code == 429: 

            print("Message: %s" % (response.json()['error']['message']))

            if retries <= maxRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print('Error: exhausted retries!')
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print("Error code: %d" % (response.status_code))
            print("Message: %s" % (response.json()['error']['message']))
        break
        
    return result

# Change color of font based on detected emotion
def getEmotionColor(emotion):
	if 'anger' in emotion:
		return (0, 0, 255)
	elif 'contempt' in emotion:
		return (0, 0, 128)
	elif 'disgust' in emotion:
		return (19, 69, 139)
	elif 'fear' in emotion:
		return (204, 50, 153)
	elif 'happiness' in emotion:
		return (0, 255, 0)
	elif 'neutral' in emotion:
		return (0, 255, 255)
	elif 'sadness' in emotion:
		return (255, 0, 0)
	elif 'surprise' in emotion:
		return (212, 255, 127)


# Display detected faces with corresponding detected emotions on image.
def handleDrawing(result, img):
    
    # Draw box around detected face.
    for currentFace in result:
        faceRectangle = currentFace['faceRectangle']
        cv2.rectangle(img,(faceRectangle['left'],faceRectangle['top']),
                           (faceRectangle['left']+faceRectangle['width'], faceRectangle['top'] + faceRectangle['height']),
                       color = (255, 255, 255), thickness = 2 )
    
    # Draw name of detected emotion.
    for currentFace in result:
        faceRectangle = currentFace['faceRectangle']
        currentEmotion = max(currentFace['scores'].items(), key=operator.itemgetter(1))[0]
        color = getEmotionColor(currentEmotion)
        textToWrite = "%s" % (currentEmotion)
        cv2.putText(img, textToWrite.upper(), (faceRectangle['left'],faceRectangle['top']-10), cv2.FONT_HERSHEY_PLAIN, 1.5, color, 2)

# Prompt user for file path of image.
path = raw_input("Please enter file path of image: ")

# Load image file into memory.
with open(path, 'rb') as file:
    data = file.read()

# Load header for request to be sent.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': _key,
}

# Send request
result = handleRequest(data, headers)

# Handle request result
if result is not None:
    # Convert string to an unsigned int array
    dataArray = np.fromstring(data, np.uint8)
    img = cv2.imdecode(dataArray, cv2.IMREAD_COLOR)
    handleDrawing(result, img)

    ig, ax = plt.subplots(figsize = (15, 20))
    # Resize options
    # cv2.namedWindow("Emotion Detection",cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Emotion Detection", 1000, 1000)
    cv2.imshow("Emotion Detection", img)
    cv2.waitKey(0)
    for currentFace in result:
		currentEmotion = max(currentFace['scores'].iteritems(), key = operator.itemgetter(1))[0]
		print("Emotion detected: ", currentEmotion)