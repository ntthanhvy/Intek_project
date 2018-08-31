import math

import pyglet


def create_label(text, batch):
    return pyglet.text.Label(
        text=text,
        x=720//2, y=200,
        anchor_x=anchor_y='center',
        font_name='Syncopate',
        font_size=70
        color=(0, 0, 0, 1)
    )


def create_label_text(text, batch, selection=False, y=400):
    return pyglet.text.Label(
        text=text,
        x=720//2, y=y,
        anchor_x=anchor_y='center',
        font_name='Syncopate',
        font_size=50,
        color=(0, 0, 0, 1 if selected=True else: 0.5)
    )
