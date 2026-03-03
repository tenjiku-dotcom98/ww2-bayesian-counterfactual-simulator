# utils/config.py

NODES = [
    "PolandInvaded",
    "FranceFalls",
    "BritainResists",
    "BarbarossaLaunched",
    "GermanOilCrisis",
    "PearlHarbor",
    "PacificNavalSuperiority",
    "USJoins",
    "LendLeaseActive",
    "IndustrialAdvantageAllies",
    "NorthAfricaCampaignSuccess",
    "DDaySuccess",
    "USSRSurvives",
    "AxisVictory"
]


SCENARIOS = {

    "No Barbarossa": {
        "BarbarossaLaunched": 0
    },

    "No Pearl Harbor": {
        "PearlHarbor": 0
    },

    "Axis Oil Stability": {
        "GermanOilCrisis": 0
    },

    "Allied Industrial Surge": {
        "IndustrialAdvantageAllies": 1
    },

    "US Neutral": {
        "USJoins": 0
    },

    "Axis Best Case": {
        "PolandInvaded": 1,
        "FranceFalls": 1,
        "BarbarossaLaunched": 1,
        "GermanOilCrisis": 0,
        "PacificNavalSuperiority": 1,
        "USJoins": 0,
        "DDaySuccess": 0,
        "USSRSurvives": 0
    },

    "Allied Best Case": {
        "USJoins": 1,
        "LendLeaseActive": 1,
        "IndustrialAdvantageAllies": 1,
        "DDaySuccess": 1,
        "USSRSurvives": 1,
        "GermanOilCrisis": 1
    }
}