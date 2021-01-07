import matplotlib.pyplot as plt
from backend.demo import config as c
from bokeh.palettes import Viridis
from bokeh.io import output_file, save
from bokeh.plotting import figure
from bokeh.layouts import row


palette = Viridis[3]


def temperature_plot():
    plot = figure(plot_width=500, plot_height=500, x_axis_label="Czas regulacji [s]",
                  y_axis_label="Temperatura wody [*C]", title="Temperatura wody w funkcji czasu")
    plot.line(range(0, int(c.get_simulation_cycles()) + 1), c.temperature_list, color=palette[0], legend_label="Tw(n)")
    return plot


def control_quantity_plot():
    plot = figure(plot_width=500, plot_height=500, x_axis_label="Czas regulacji [s]",
                  y_axis_label="Wielkość sterująca", title="Wielkość sterująca w funkcji czasu")
    plot.line(range(0, int(c.get_simulation_cycles())), c.get_control_quantity_list(), color=palette[1], legend_label="U(n)")
    return plot


def error_plot():
    plot = figure(plot_width=500, plot_height=500, x_axis_label="Czas regulacji [s]",
                  y_axis_label="Uchyb regulacji", title="Uchyb regulacji w funkcji czasu")
    plot.line(range(0, int(c.get_simulation_cycles())), c.get_control_error_list(), color=palette[0], legend_label="e(n)")
    return plot


def generate_plots():
    plots = row(temperature_plot(), control_quantity_plot(), error_plot())
    output_file("./web/templates/plots.html")
    save(plots, "./web/templates/plots.html")
