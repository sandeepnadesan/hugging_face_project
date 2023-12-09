from flask import Flask, render_template, request
from transformers import pipeline



translation_pipeline = pipeline(task="translation", model="Helsinki-NLP/opus-mt-en-de")

def home():
    
    input_text = request.form["input_text"]
    output_text = translation_pipeline(input_text, max_length=50)[0]["translation_text"]

    return output_text