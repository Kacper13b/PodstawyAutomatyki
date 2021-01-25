from flask import Flask, render_template, request
from backend.config import config
from backend.demo import demo, set_demo_config
from backend.plots import plot
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/simulation')
# def simulation_web_page():
#     return render_template('simulation.html', title='simulation', data=config)


@app.route('/simulation', methods=['POST', 'GET'])
def my_form_post():
    # config.set_temperature_goal(np.float32(request.form['temperature_goal']))
    # config.set_ambient_temperature(np.float32(request.form['ambient_temperature']))
    # config.set_time(np.float32(request.form['ambient_temperature']))
    # config.set_initial_temperature(np.float32(request.form['ambient_temperature']))
    # return render_template('simulation.html', title='simulation', data=config)
    set_demo_config()
    return render_template('simulation.html', title='simulation', data=config)



@app.route('/demo', methods=['POST', 'GET'])
def demo_web():
    set_demo_config()
    demo()
    fig = make_subplots(rows=2, cols=3)

    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.temperature_list,
                             mode='lines',
                             name='Temperatura', line=dict(color="orange", width=2)),row=1, col=1)

    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.delivered_heat_list,
                             mode='lines',
                             name='Dostarczone ciepło', line=dict(color="red", width=2)), row=1, col=2)

    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.control_error_list,
                             mode='lines',
                             name='Uchyb', line=dict(color="blue", width=2)), row=1, col=3)
    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.control_quantity_list,
                             mode='lines',
                             name='Control Quantity', line=dict(color="green", width=2)), row=2, col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.heat_loss_list,
                             mode='lines',
                             name='Strata ciepła', line=dict(color="black", width=2)), row=2, col=2)
    fig.update_layout(
        title_text=str("Wykres")
    )
    fig.write_html("web/templates/plots.html")
    return render_template("plots.html")




if __name__ == '__main__':
    set_demo_config()
    demo()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(config.get_simulation_cycles())], y=config.temperature_list,
                             mode='lines',
                             name='Temperatura', line=dict(color="orange", width=2)))
    fig.update_layout(
        title_text=str("Temperatura"), hovermode="x unified", xaxis_title="Czas", yaxis_title="Temperatura"
    )
    fig.write_html("web/templates/plots.html")
    app.run(debug=True)

