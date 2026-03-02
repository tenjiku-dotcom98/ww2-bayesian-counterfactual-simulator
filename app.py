import streamlit as st
from model.inference_engine import WW2InferenceEngine
from utils.config import NODES
from analysis.influence import compute_node_influence

st.set_page_config(layout="wide")

st.title("🧠 WWII Causal Intervention Lab")

# -----------------------------------
# Initialize Bayesian Engine
# -----------------------------------

engine = WW2InferenceEngine()

# -----------------------------------
# Sidebar - Interventions
# -----------------------------------

st.sidebar.header("⚙️ Interventions")

interventions = {}

for node in NODES:
    if node == "AxisVictory":
        continue

    choice = st.sidebar.radio(
        label=node,
        options=["No Intervention", "Force 0", "Force 1"],
        key=f"intervention_{node}"
    )

    if choice == "Force 0":
        interventions[node] = 0
    elif choice == "Force 1":
        interventions[node] = 1

# -----------------------------------
# Outcome Calculation
# -----------------------------------

baseline = engine.get_baseline()
counter = engine.run_counterfactual(interventions)
delta = counter - baseline

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Outcome")
    st.metric("Baseline Axis Victory", f"{baseline:.3f}")
    st.metric("Intervention Axis Victory", f"{counter:.3f}")
    st.metric("Δ Change", f"{delta:.3f}")

with col2:
    st.subheader("Active Interventions")
    if interventions:
        st.json(interventions)
    else:
        st.write("None")

# -----------------------------------
# Posterior Cascade View
# -----------------------------------

st.divider()
st.subheader("🔁 Posterior Cascade")

for node in NODES:
    if node == "AxisVictory":
        continue

    result = engine.infer.query(
        variables=[node],
        evidence=interventions
    )

    prob = result.values[1]
    st.write(f"{node}: {prob:.3f}")

# -----------------------------------
# Influence Ranking
# -----------------------------------

st.divider()
st.subheader("📈 Node Influence Ranking")

ranked, scores = compute_node_influence()

for node, value in ranked:
    st.write(f"{node}: {value:.4f}")