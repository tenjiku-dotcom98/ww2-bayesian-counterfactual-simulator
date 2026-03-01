# test_scenarios.py

from simulation.scenario_runner import ScenarioRunner
from utils.config import SCENARIOS
from narrative.generator import generate_narrative

runner = ScenarioRunner()

print("=== SCENARIO TESTS ===\n")

for scenario_name in SCENARIOS.keys():
    result = runner.run(scenario_name)
    print(f"Scenario: {scenario_name}")
    print(result)
    print(generate_narrative(result))
    print("-" * 50)