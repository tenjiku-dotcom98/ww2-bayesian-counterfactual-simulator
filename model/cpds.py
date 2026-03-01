# model/cpds.py

from pgmpy.factors.discrete import TabularCPD

def get_cpds():

    cpd_poland = TabularCPD('PolandInvaded', 2, [[0.1], [0.9]])

    cpd_pearl = TabularCPD('PearlHarbor', 2, [[0.3], [0.7]])

    cpd_britain = TabularCPD(
        'BritainResists', 2,
        [[0.2, 0.7],
         [0.8, 0.3]],
        evidence=['PolandInvaded'],
        evidence_card=[2]
    )

    cpd_barbarossa = TabularCPD(
        'BarbarossaLaunched', 2,
        [[0.3, 0.6],
         [0.7, 0.4]],
        evidence=['BritainResists'],
        evidence_card=[2]
    )

    cpd_ussr = TabularCPD(
        'USSRSurvives', 2,
        [[0.2, 0.8],
         [0.8, 0.2]],
        evidence=['BarbarossaLaunched'],
        evidence_card=[2]
    )

    cpd_us = TabularCPD(
        'USJoins', 2,
        [[0.4, 0.9],
         [0.6, 0.1]],
        evidence=['PearlHarbor'],
        evidence_card=[2]
    )

    cpd_dday = TabularCPD(
        'DDaySuccess', 2,
        [[0.5, 0.8],
         [0.5, 0.2]],
        evidence=['USJoins'],
        evidence_card=[2]
    )

    # AxisVictory has 3 parents → 8 combinations
    cpd_axis = TabularCPD(
        'AxisVictory', 2,
        [
            # Axis loses
            [0.95, 0.8, 0.7, 0.4, 0.6, 0.3, 0.2, 0.1],
            # Axis wins
            [0.05, 0.2, 0.3, 0.6, 0.4, 0.7, 0.8, 0.9]
        ],
        evidence=['BarbarossaLaunched', 'DDaySuccess', 'USSRSurvives'],
        evidence_card=[2, 2, 2]
    )

    return [
        cpd_poland,
        cpd_pearl,
        cpd_britain,
        cpd_barbarossa,
        cpd_ussr,
        cpd_us,
        cpd_dday,
        cpd_axis
    ]