# game/world_state.py

class WorldState:
    """
    Stores evolving game state:
    - Player role
    - Evidence (resolved decisions)
    - Turn number
    - History of moves
    """

    def __init__(self, role):
        self.role = role
        self.evidence = {}
        self.turn = 1
        self.history = []

    # game/world_state.py
    def apply_decision(self, node, value, actor="Player"):
        # Never allow the final outcome node to be set as an explicit decision.
        if node == "AxisVictory":
            return
        self.evidence[node] = value
        self.history.append({
            "turn": self.turn,
            "actor": actor,
            "node": node,
            "value": value
        })

    def next_turn(self):
        self.turn += 1