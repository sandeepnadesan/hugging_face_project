from main import app
from main.api import controller


# Mount routes
app.add_url_rule(
    '/emotion-prediction/', view_func=controller.predict, methods=['GET','POST'])
app.add_url_rule(
    '/text-generation/', view_func=controller.generate, methods=['GET','POST'])
app.add_url_rule(
    '/word_translation/', view_func=controller.translate, methods=['GET','POST'])