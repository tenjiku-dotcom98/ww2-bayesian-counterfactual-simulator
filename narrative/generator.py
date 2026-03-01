# narrative/generator.py

def generate_narrative(result):

    baseline = result["baseline"]
    counter = result["counterfactual"]
    delta = result["delta"]

    direction = "increases" if delta > 0 else "decreases"

    return f"""
Baseline Axis Victory Probability: {baseline:.3f}

Under this counterfactual scenario, the probability of Axis victory
{direction} to {counter:.3f}.

This represents a shift of {abs(delta):.3f}, indicating the causal
importance of the altered decision within the modeled network.
"""