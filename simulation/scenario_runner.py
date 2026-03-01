# simulation/scenario_runner.py

from model.inference_engine import WW2InferenceEngine
from utils.config import SCENARIOS

class ScenarioRunner:

    def __init__(self):
        self.engine = WW2InferenceEngine()
        self.baseline = self.engine.get_baseline()

    def run(self, scenario_name):
        evidence = SCENARIOS[scenario_name]
        counterfactual = self.engine.run_counterfactual(evidence)

        return {
            "baseline": float(self.baseline),
            "counterfactual": float(counterfactual),
            "delta": float(counterfactual - self.baseline)
        }