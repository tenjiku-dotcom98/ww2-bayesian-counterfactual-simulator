# test_influence.py

from analysis.influence import compute_node_influence

ranked, scores = compute_node_influence()

print("Influence Ranking:")
for node, value in ranked:
    print(f"{node}: {value:.4f}")