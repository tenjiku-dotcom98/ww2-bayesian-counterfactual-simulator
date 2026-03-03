from pgmpy.factors.discrete import TabularCPD


def get_cpds():

    # ----------------------------
    # Root Nodes (No Parents)
    # ----------------------------

    cpd_poland = TabularCPD(
        variable="PolandInvaded",
        variable_card=2,
        values=[[0.3], [0.7]]
    )

    cpd_barbarossa = TabularCPD(
        variable="BarbarossaLaunched",
        variable_card=2,
        values=[[0.4], [0.6]]
    )

    cpd_pearl = TabularCPD(
        variable="PearlHarbor",
        variable_card=2,
        values=[[0.5], [0.5]]
    )

    cpd_usjoins = TabularCPD(
        variable="USJoins",
        variable_card=2,
        values=[[0.3], [0.7]]
    )

    cpd_north_africa = TabularCPD(
        variable="NorthAfricaCampaignSuccess",
        variable_card=2,
        values=[[0.5], [0.5]]
    )

    # ----------------------------
    # FranceFalls | PolandInvaded
    # ----------------------------

    cpd_france = TabularCPD(
        variable="FranceFalls",
        variable_card=2,
        values=[
            [0.8, 0.2],
            [0.2, 0.8]
        ],
        evidence=["PolandInvaded"],
        evidence_card=[2]
    )

    # ----------------------------
    # BritainResists | FranceFalls
    # ----------------------------

    cpd_britain = TabularCPD(
        variable="BritainResists",
        variable_card=2,
        values=[
            [0.3, 0.7],
            [0.7, 0.3]
        ],
        evidence=["FranceFalls"],
        evidence_card=[2]
    )

    # ----------------------------
    # LendLeaseActive | USJoins
    # ----------------------------

    cpd_lendlease = TabularCPD(
        variable="LendLeaseActive",
        variable_card=2,
        values=[
            [0.7, 0.2],
            [0.3, 0.8]
        ],
        evidence=["USJoins"],
        evidence_card=[2]
    )

    # ----------------------------
    # IndustrialAdvantageAllies | USJoins
    # ----------------------------

    cpd_industry = TabularCPD(
        variable="IndustrialAdvantageAllies",
        variable_card=2,
        values=[
            [0.6, 0.2],
            [0.4, 0.8]
        ],
        evidence=["USJoins"],
        evidence_card=[2]
    )

    # ----------------------------
    # PacificNavalSuperiority | PearlHarbor
    # ----------------------------

    cpd_pacific = TabularCPD(
        variable="PacificNavalSuperiority",
        variable_card=2,
        values=[
            [0.4, 0.7],
            [0.6, 0.3]
        ],
        evidence=["PearlHarbor"],
        evidence_card=[2]
    )

    # ----------------------------
    # GermanOilCrisis | BarbarossaLaunched, NorthAfricaCampaignSuccess
    # ----------------------------

    cpd_oil = TabularCPD(
        variable="GermanOilCrisis",
        variable_card=2,
        values=[
            [0.7, 0.5, 0.4, 0.2],
            [0.3, 0.5, 0.6, 0.8]
        ],
        evidence=["BarbarossaLaunched", "NorthAfricaCampaignSuccess"],
        evidence_card=[2, 2]
    )

    # ----------------------------
    # DDaySuccess | IndustrialAdvantageAllies
    # ----------------------------

    cpd_dday = TabularCPD(
        variable="DDaySuccess",
        variable_card=2,
        values=[
            [0.6, 0.3],
            [0.4, 0.7]
        ],
        evidence=["IndustrialAdvantageAllies"],
        evidence_card=[2]
    )

    # ----------------------------
    # USSRSurvives | LendLeaseActive
    # ----------------------------

    cpd_ussr = TabularCPD(
        variable="USSRSurvives",
        variable_card=2,
        values=[
            [0.6, 0.2],
            [0.4, 0.8]
        ],
        evidence=["LendLeaseActive"],
        evidence_card=[2]
    )

    # ----------------------------
    # AxisVictory | BritainResists, GermanOilCrisis,
    #                PacificNavalSuperiority, DDaySuccess, USSRSurvives
    # ----------------------------

    cpd_axis = TabularCPD(
        variable="AxisVictory",
        variable_card=2,
        values=[
            [0.6] * 32,
            [0.4] * 32
        ],
        evidence=[
            "BritainResists",
            "GermanOilCrisis",
            "PacificNavalSuperiority",
            "DDaySuccess",
            "USSRSurvives"
        ],
        evidence_card=[2, 2, 2, 2, 2]
    )

    return [
        cpd_poland,
        cpd_barbarossa,
        cpd_pearl,
        cpd_usjoins,
        cpd_north_africa,
        cpd_france,
        cpd_britain,
        cpd_lendlease,
        cpd_industry,
        cpd_pacific,
        cpd_oil,
        cpd_dday,
        cpd_ussr,
        cpd_axis
    ]