# model/structure.py

from pgmpy.models import DiscreteBayesianNetwork

def build_structure():
    model = DiscreteBayesianNetwork([
        ("PolandInvaded", "FranceFalls"),
        ("FranceFalls", "BritainResists"),
        ("BritainResists", "AxisVictory"),

        ("BarbarossaLaunched", "GermanOilCrisis"),
        ("GermanOilCrisis", "AxisVictory"),

        ("PearlHarbor", "PacificNavalSuperiority"),
        ("PacificNavalSuperiority", "AxisVictory"),

        ("USJoins", "LendLeaseActive"),
        ("LendLeaseActive", "USSRSurvives"),

        ("USJoins", "IndustrialAdvantageAllies"),
        ("IndustrialAdvantageAllies", "DDaySuccess"),

        ("NorthAfricaCampaignSuccess", "GermanOilCrisis"),

        ("DDaySuccess", "AxisVictory"),
        ("USSRSurvives", "AxisVictory"),
    ])

    return model