# model/inference_engine.py

from pgmpy.inference import VariableElimination
from .structure import build_structure
from .cpds import get_cpds

class WW2InferenceEngine:

    def __init__(self):
        self.model = build_structure()
        self.model.add_cpds(*get_cpds())
        self.model.check_model()
        self.infer = VariableElimination(self.model)

    def get_baseline(self):
        result = self.infer.query(variables=['AxisVictory'])
        # AxisVictory = 1 (win) is index 1
        return result.values[1]

    def run_counterfactual(self, evidence):
        result = self.infer.query(
            variables=['AxisVictory'],
            evidence=evidence
        )
        return result.values[1]