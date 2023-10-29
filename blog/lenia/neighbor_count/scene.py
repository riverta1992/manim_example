from manim import *

class SquareExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        vg = VGroup()
        n = 3
        vg += Square(side_length=1.0,color=BLACK).shift(UP+LEFT).set_fill(BLACK, opacity=1.0)
        vg += Square(side_length=1.0,color=BLACK).shift(UP)
        vg += Square(side_length=1.0,color=BLACK).shift(UP+RIGHT)
        vg += Square(side_length=1.0,color=BLACK).shift(LEFT)
        center = Square(side_length=1.0,color=BLACK)
        vg += center
        vg += Square(side_length=1.0,color=BLACK).shift(RIGHT).set_fill(BLACK, opacity=1.0)
        vg += Square(side_length=1.0,color=BLACK).shift(DOWN+LEFT)
        vg += Square(side_length=1.0,color=BLACK).shift(DOWN).set_fill(BLACK, opacity=1.0)
        vg += Square(side_length=1.0,color=BLACK).shift(DOWN+RIGHT)

        red_center = Square(side_length=1.0,color=BLACK).set_fill(RED, opacity=1.0)
        
        self.add(vg)
        self.play(ReplacementTransform(center,red_center))
        self.wait(1)
        vg.remove(center)
        factor = 2
        self.play(ScaleInPlace(vg, factor))

        self.play(FadeIn(Text("1").shift(factor*(UP+LEFT)), shift=DOWN))
        self.play(FadeIn(Text("2").shift(factor*RIGHT), shift=DOWN))
        self.play(FadeIn(Text("3").shift(factor*DOWN), shift=DOWN))
        '''
        for i in range(n):
            for j in range(n):
                if i==0 and j==0:
                    s = Square(side_length=1.0).shift(UP+LEFT)
                    s.set_fill(RED,opacity=0.5)
                    vg += s
                else:
                    if j==0:
                        s = Square(side_length=1.0).next_to(vg[(i-1)*n], direction=DOWN)
                        vg += s
                    else:
                        s = Square(side_length=1.0).next_to(vg[-1], direction=RIGHT)
                        vg += s
        '''
