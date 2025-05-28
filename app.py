from flask import Flask, render_template, request, redirect, url_for #modules de Flask
import os
from motifs import dessiner  # importe la fonction dessiner de motifs.py

app = Flask(__name__) #création de l'application

IMAGE_FOLDER = 'librairie/images' 
os.makedirs(IMAGE_FOLDER, exist_ok=True)    #endroit où sont stockées les images 

