WWII Causal Intervention Lab

A Bayesian counterfactual simulation platform modeling World War II as a probabilistic causal system.

This is not a game.
Not a history blog.
Not a rule engine.

It’s a structured causal inference lab.

What This Actually Does

WWII strategic decisions are modeled as a Bayesian Network.

Nodes include:

PolandInvaded

BritainResists

BarbarossaLaunched

PearlHarbor

USJoins

DDaySuccess

USSRSurvives

AxisVictory

Each node has probabilistic dependencies encoded through conditional probability tables.

You can intervene on any decision and compute:

P(AxisVictory | interventions)

Then observe how probabilities propagate across the entire system.

Core Capabilities
Multi-Node Interventions

Force multiple decisions simultaneously and measure structural impact.

Example:

BarbarossaLaunched = 0
DDaySuccess = 0

Watch how the entire network shifts.

Posterior Cascade Analysis

After intervention, the system recomputes the posterior probability of every unresolved node.

This exposes probabilistic propagation across the graph.

Node Influence Ranking

Quantifies structural importance of each decision node relative to the final outcome.

Answers questions like:

Which strategic decision structurally mattered most?

Causal DAG Visualization

Interactive graph of the full Bayesian structure.

Transparent.
Interpretable.
Not black-box ML.

Tech Stack

Python

pgmpy (DiscreteBayesianNetwork)

Streamlit

NetworkX

Plotly

Exact inference via Variable Elimination.

No heuristics.
No simulation shortcuts.

Why This Is Different

Most ML projects predict outcomes.

This one models causality.

Structured dependencies

Explicit interventions

Posterior reasoning

Sensitivity analysis

Transparent graphical model

It’s applied causal AI.

Run Locally

Clone the repo:

git clone https://github.com/YOUR_USERNAME/ww2-bayesian-counterfactual-simulator.git
cd ww2-bayesian-counterfactual-simulator

Create environment:

python -m venv venv
venv\Scripts\activate

Install:

pip install -r requirements.txt

Run:

streamlit run app.py
What This Demonstrates

Probabilistic graphical modeling

Counterfactual reasoning

Bayesian inference under intervention

Structural sensitivity analysis

Explainable AI systems

This is causal modeling applied to geopolitical decision systems.

Disclaimer

This is a simplified probabilistic abstraction of WWII strategic dynamics. It is built for structural reasoning experimentation, not historical completeness.