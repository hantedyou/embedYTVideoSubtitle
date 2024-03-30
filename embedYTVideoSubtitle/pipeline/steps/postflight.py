
from embedYTVideoSubtitle.pipeline.steps.step import Step

class Postflight(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        print("Postflight process")