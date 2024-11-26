# agent_watch/cost_calculator.py

class CostCalculator:
    PRICING = {
        "gpt-4o": {
            "input": 2.50 / 1_000_000,
            "output": 10.00 / 1_000_000
        },
        "gpt-4o-mini": {
            "input": 0.150 / 1_000_000,
            "output": 0.600 / 1_000_000
        }
    }

    def __init__(self, model: str):
        if model not in self.PRICING:
            raise ValueError(f"Model {model} not supported.")
        self.model = model

    def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        input_cost = input_tokens * self.PRICING[self.model]["input"]
        output_cost = output_tokens * self.PRICING[self.model]["output"]
        total_cost = input_cost + output_cost
        return total_cost
