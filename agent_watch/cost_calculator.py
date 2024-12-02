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
        },
        "gpt-4": {
            "input": 3.00 / 1_000_000,
            "output": 6.00 / 1_000_000
        },
        "gpt-4o-audio-preview": {
            "input": 2.50 / 1_000_000,
            "output": 10.00 / 1_000_000
        },
        "o1-mini": {
            "input": 3.00 / 1_000_000,
            "output": 12.00 / 1_000_000
        },
        "o1-preview": {
            "input": 15.00 / 1_000_000,
            "output": 60.00 / 1_000_000
        },
        "chatgpt-4o-latest": {
            "input": 5.00 / 1_000_000,
            "output": 15.00 / 1_000_000
        },
        "gpt-4-turbo-preview": {
            "input": 10.00 / 1_000_000,
            "output": 30.00 / 1_000_000
        },
        "gpt-4-32k": {
            "input": 60.00 / 1_000_000,
            "output": 120.00 / 1_000_000
        },
        "gpt-4-turbo": {
            "input": 10.00 / 1_000_000,
            "output": 30.00 / 1_000_000
        },
        "gpt-4-vision-preview": {
            "input": 10.00 / 1_000_000,
            "output": 30.00 / 1_000_000
        },
        "gpt-3.5-turbo": {
            "input": 1.50 / 1_000_000,
            "output": 2.00 / 1_000_000
        },
        "gpt-3.5-turbo-16k": {
            "input": 3.00 / 1_000_000,
            "output": 4.00 / 1_000_000
        },
        "claude-instant-1.2": {
            "input": 0.163 / 1_000_000,
            "output": 0.551 / 1_000_000
        },
        "claude-2": {
            "input": 8.00 / 1_000_000,
            "output": 24.00 / 1_000_000
        },
        "claude-2.1": {
            "input": 8.00 / 1_000_000,
            "output": 24.00 / 1_000_000
        },
            "claude-3-haiku-20240307": {
            "input": 0.25 / 1_000_000,
            "output": 1.25 / 1_000_000
        },
        "claude-3-5-haiku-20241022": {
            "input": 1.00 / 1_000_000,
            "output": 5.00 / 1_000_000
        },
        "claude-3-opus-20240229": {
            "input": 15.00 / 1_000_000,
            "output": 75.00 / 1_000_000
        },
        "claude-3-sonnet-20240229": {
            "input": 3.00 / 1_000_000,
            "output": 15.00 / 1_000_000
        },
        "claude-3-5-sonnet-20240620": {
            "input": 3.00 / 1_000_000,
            "output": 15.00 / 1_000_000
        },
        "claude-3-5-sonnet-20241022": {
            "input": 3.00 / 1_000_000,
            "output": 15.00 / 1_000_000
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
