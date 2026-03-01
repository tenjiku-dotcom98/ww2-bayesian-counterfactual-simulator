from model.inference_engine import WW2InferenceEngine
from visualization.probability_plot import plot_probability_shift

engine = WW2InferenceEngine()

baseline = engine.get_baseline()
cf = engine.run_counterfactual({'BarbarossaLaunched': 0})

print("Baseline:", baseline)
print("Counterfactual:", cf)

fig = plot_probability_shift(baseline, cf)
fig.show()