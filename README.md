# emotion_detection
Detecting Emotion Using Facial Expressions in Images

## Abstract
Implementing an emotion detection system that senses emotion via facial expression has become a much easier task over the past several years. This is because of the development and progress of affective computing APIs over the past several years. I wanted to try such an implementation for my final project because the topic of computing with affect interests me as an emerging research area and I simply love to code. The system that I created can predict, with a fair amount of accuracy, a person’s emotional state based of their facial expression in pictures. It is written using Python and uses a few APIs to accomplish emotion prediction as well as displaying the results. No empirical research was done, but I ran several tests which I will show the results of later. I tested my program using pictures found on google image search of faces with labeled emotional states and pictures of myself.

## Introduction
This project was initiated by simply exploring what was out there in terms of APIs and tools for affective computing. After determining what sort of tools that I had at my disposal I decided that it would be challenging, but also rewarding to develop a program centered around emotion prediction through facial expression recognition. Development of programs such as this are important because there are numerous applications and benefit future study of this topic.

## Background Information
The task of emotion prediction via facial expressions in pictures involves finding the state of semantic primitives or features of a detected face (i.e. wrinkled forehead, pursed lips, raised cheeks, etc) and using a classification algorithm to force a decision for a predicted emotion. For this program, I used categorical representation of emotion. This representation only includes the seven basic emotions. These emotions are understood to be cross-culturally and universally communicated with distinct facial expressions.

## Methodology
My first steps with this project involved understanding what tools were available to try and gauge what was actually feasible for the scope of this class. I explored a few options for emotion detection APIs and considered their strengths and limitations. I settled on Microsoft’s Emotion API and decided to develop an application that can predict emotion of facial expressions found in images.
I chose to use Microsoft’s Emotion API for number of reasons. First, I already had the credentials to use this API for free through my Microsoft Azure account. Also, this API supports facial recognition as well as emotion detection of facial expressions in an image, which is perfect for my usage. I’m using the categorical representation of emotion for this project as the Emotion API can detect anger, contempt, disgust, fear, happiness, neutral, sadness, and surprise. These basic emotions can be accurately detected with facial expression. The categorical representation works best for my implementation as it is much simpler to model than using dimensional or componential representations. 

