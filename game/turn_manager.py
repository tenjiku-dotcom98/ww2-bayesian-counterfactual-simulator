import random
from model.inference_engine import WW2InferenceEngine
from game.world_state import WorldState
from game.roles import ROLES


class TurnManager:

    def __init__(self, role):
        self.world = WorldState(role)
        self.engine = WW2InferenceEngine()

    def get_available_player_decisions(self):
        allowed = ROLES[self.world.role]
        return [
            node for node in allowed
            if node not in self.world.evidence
        ]

    def player_move(self, node, value):
        self.world.apply_decision(node, value, actor="Player")
        self.resolve_ai_moves()
        self.world.next_turn()

    def resolve_ai_moves(self):

        for node in self.engine.model.nodes():

            # ❌ Never resolve final outcome
            if node == "AxisVictory":
                continue

            # Skip already decided nodes
            if node in self.world.evidence:
                continue

            # Skip player-controlled nodes
            if node in ROLES[self.world.role]:
                continue

            result = self.engine.infer.query(
                variables=[node],
                evidence=self.world.evidence
            )

            prob = result.values[1]

            outcome = 1 if random.random() < prob else 0

        self.world.apply_decision(node, outcome, actor="AI")
    def get_axis_victory_probability(self):
        prob = self.engine.run_counterfactual(self.world.evidence)
        return float(prob)

    def get_world_state(self):
        return {
            "turn": self.world.turn,
            "evidence": self.world.evidence,
            "history": self.world.history
        }