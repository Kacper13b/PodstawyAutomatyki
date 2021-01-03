from flask import Flask, render_template, request
from backend.config import config
from backend.demo import demo, set_demo_config
import numpy as np

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/simulation')
def simulation_web_page():
    set_demo_config()
    return render_template('simulation.html', title='simulation', data=config)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')


@app.route('/simulation', methods=['POST'])
def my_form_post():
    config.set_temperature_goal(np.float32(request.form['temperature_goal']))
    config.set_ambient_temperature(np.float32(request.form['ambient_temperature']))
    config.set_time(np.float32(request.form['ambient_temperature']))
    config.set_initial_temperature(np.float32(request.form['ambient_temperature']))
    demo()
    # return render_template('simulation.html', title='simulation', data=config)
    return 'Działa'


if __name__ == '__main__':
    app.run(debug=True)
