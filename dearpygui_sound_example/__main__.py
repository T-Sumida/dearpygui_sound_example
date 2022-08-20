import dearpygui.dearpygui as dpg
import sounddevice as sd
from dearpygui_sound_example.mic import Mic
from math import sin, cos

print(sd.query_devices())

mic_obj = Mic()

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 4410):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))

def update_series():

    cosdatax = []
    cosdatay = []
    for i in range(0, 4410):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * i / 1000))
    mic_obj.start()

with dpg.window(label="Mic Input", tag="win"):
    dpg.add_button(label="Start Stream", callback=update_series)
    # create plot
    with dpg.plot(label="MIC", height=400, width=800):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="Time[sec]", tag="x_axis")
        dpg.set_axis_limits("x_axis", 0, 0.1)
        dpg.add_plot_axis(dpg.mvYAxis, label="Amp", tag="y_axis")
        dpg.set_axis_limits("y_axis", -1, 1)

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis", tag="series_tag")

dpg.create_viewport(title='Mic Streaming Example', width=1200, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
