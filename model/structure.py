# model/structure.py

from pgmpy.models import DiscreteBayesianNetwork

def build_structure():
    model = DiscreteBayesianNetwork([
        ('PolandInvaded', 'BritainResists'),
        ('BritainResists', 'BarbarossaLaunched'),
        ('BarbarossaLaunched', 'USSRSurvives'),
        ('PearlHarbor', 'USJoins'),
        ('USJoins', 'DDaySuccess'),
        ('BarbarossaLaunched', 'AxisVictory'),
        ('DDaySuccess', 'AxisVictory'),
        ('USSRSurvives', 'AxisVictory')
    ])

    return model