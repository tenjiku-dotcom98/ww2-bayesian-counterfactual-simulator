class WW2GameEngine:

    def __init__(self, role):
        self.role = role
        self.engine = WW2InferenceEngine()
        self.evidence = {}
        self.turn = 1

    def player_decision(self, node, value):
        self.evidence[node] = value
        self.resolve_world()

    def resolve_world(self):
        posterior = self.engine.infer.query(
            variables=self.engine.model.nodes(),
            evidence=self.evidence
        )

        for node in posterior.variables:
            if node not in self.evidence:
                prob = posterior[node].values[1]
                if prob > 0.6:
                    self.evidence[node] = 1