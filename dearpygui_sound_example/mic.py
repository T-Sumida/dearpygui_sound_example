import sounddevice as sd
import dearpygui.dearpygui as dpg
import numpy as np
import sys

class Mic(object):
    def __init__(self) -> None:
        self.stream = sd.InputStream(
            device=1, channels=max([i+1 for i in range(2)]),
            samplerate=44100,
            blocksize=4410,
            callback=self.audio_callback
        )
        # self.stream.start()
        self.tag = "series_tag"

    def start(self):
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        # Fancy indexing with mapping creates a (necessary!) copy:
        # q.put(indata[::10, :])
        try:
            # print(indata.shape)
            x = np.arange(indata.shape[0], dtype=np.float32) / 44100.
            # print(x.shape, indata[:, 0].shape)
            dpg.set_value('series_tag', [list(x), list(indata[:, 0])])
            dpg.set_item_label('series_tag', "4- Anker PowerCast M300")
        except Exception as e:
            print(e)
            pass
        # dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")
