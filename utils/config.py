# utils/config.py

NODES = [
    "PolandInvaded",
    "BritainResists",
    "BarbarossaLaunched",
    "PearlHarbor",
    "USJoins",
    "DDaySuccess",
    "USSRSurvives",
    "AxisVictory"
]

SCENARIOS = {
    "No Barbarossa": {"BarbarossaLaunched": 0},
    "No Pearl Harbor": {"PearlHarbor": 0},
    "D-Day Fails": {"DDaySuccess": 0},
    "US Never Joins": {"USJoins": 0}
}