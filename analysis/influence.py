# analysis/influence.py

from model.inference_engine import WW2InferenceEngine
from utils.config import NODES

def compute_node_influence():

    engine = WW2InferenceEngine()
    baseline = engine.get_baseline()

    influence_scores = {}

    for node in NODES:
        if node == "AxisVictory":
            continue

        cf_zero = engine.run_counterfactual({node: 0})
        cf_one = engine.run_counterfactual({node: 1})

        impact_zero = abs(cf_zero - baseline)
        impact_one = abs(cf_one - baseline)

        influence_scores[node] = float(max(impact_zero, impact_one))

    ranked = sorted(
        influence_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked, influence_scores