from manim import *
import numpy as np

config.background_color = "#211B15"


class QuantumTunnel(Scene):
    def construct(self):
        coral, cyan, text, muted = "#E08A63", "#5FB6C4", "#F2EAE0", "#A89A88"
        title = Text("A wave meets a barrier", font="Montserrat", weight=BOLD,
                     font_size=40, color=text).to_edge(UP, buff=.35)
        axis = Line(LEFT * 6.3, RIGHT * 6.3, color="#4A3D30").shift(DOWN * .4)
        barrier = Rectangle(width=1.5, height=4.2, color=coral,
                            fill_color=coral, fill_opacity=.16).shift(RIGHT * .45 + DOWN * .4)
        label = Text("BARRIER", font="Open Sans", font_size=20, color=coral).next_to(barrier, UP, buff=.12)
        self.center = ValueTracker(-4.4)
        packet = always_redraw(lambda: FunctionGraph(
            lambda x: 1.0 * np.exp(-((x - self.center.get_value()) / 1.25) ** 2)
            * np.sin(8 * (x - self.center.get_value())),
            x_range=[-6.3, min(-.3, self.center.get_value() + 2.4)], color=cyan,
            stroke_width=4).shift(DOWN * .4))
        transmitted = FunctionGraph(
            lambda x: .28 * np.exp(-((x - 2.1) / 1.2) ** 2) * np.sin(8 * (x - 2.1)),
            x_range=[1.2, 5.2], color=cyan, stroke_width=4).shift(DOWN * .4)
        chance = Text("small probability beyond", font="Open Sans", font_size=24,
                      color=muted).next_to(transmitted, DOWN, buff=.55)
        self.play(FadeIn(title), Create(axis), FadeIn(barrier), FadeIn(label), run_time=1)
        self.add(packet)
        self.play(self.center.animate.set_value(-1.0), run_time=2.3, rate_func=linear)
        self.play(FadeIn(transmitted, shift=RIGHT * .25), FadeIn(chance), run_time=1.2)
        self.play(Indicate(transmitted, color=coral, scale_factor=1.08), run_time=1.2)
        self.wait(1.0)
