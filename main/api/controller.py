from flask import Flask, request, render_template
from main.helpers.text_generation import generate_text
from main.helpers.emotions import classifier, emotion_mapping
from main.helpers.translation import translation_pipeline,home
from app import app


def predict():
    if request.method == 'POST':
        user_input = request.form['user_input']
        model_output = classifier(user_input)
        predicted_emotion = model_output[0]['label']
        mapped_sentiment = emotion_mapping.get(predicted_emotion, "unknown")
        return render_template('prediction_output.html', user_input=user_input, predicted_emotion=predicted_emotion, mapped_sentiment=mapped_sentiment)
    return render_template('prediction.html')

def generate():
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_text = generate_text(prompt)
        return render_template('generation_output.html', prompt=prompt, generated_text=generated_text)

    return render_template('generation.html')

def translate():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = translation_pipeline(input_text, max_length=50)[0]["translation_text"]
        return render_template("translation_out.html", input_text=input_text, output_text=output_text)
    return render_template("translation.html", input_text="", output_text="")


