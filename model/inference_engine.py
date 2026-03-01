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

    # model/inference_engine.py
    def run_counterfactual(self, evidence):
        # Ensure we never condition on the outcome node 'AxisVictory'
        evidence_clean = {k: v for k, v in (evidence or {}).items() if k != "AxisVictory"}
        result = self.infer.query(
            variables=['AxisVictory'],
            evidence=evidence_clean
        )
        return result.values[1]