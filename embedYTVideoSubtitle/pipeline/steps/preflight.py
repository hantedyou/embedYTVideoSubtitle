
from embedYTVideoSubtitle.pipeline.steps.step import Step
from embedYTVideoSubtitle import utils

class Preflight(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        print("Preflight process")
        utils.create_folders()