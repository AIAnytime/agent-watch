# agent_watch/cost_calculator.py

class CostCalculator:
    # Define the cost per token in a constant
    COST_PER_TOKEN = 1_000_000

    # Base pricing template to avoid repetition
    BASE_PRICING = {
        "gpt-4o": (2.50, 10.00),
        "gpt-4o-mini": (0.150, 0.600),
        "gpt-4": (3.00, 6.00),
        "gpt-4o-audio-preview": (2.50, 10.00),
        "o1-mini": (3.00, 12.00),
        "o1-preview": (15.00, 60.00),
        "chatgpt-4o-latest": (5.00, 15.00),
        "gpt-4-turbo-preview": (10.00, 30.00),
        "gpt-4-32k": (60.00, 120.00),
        "gpt-4-turbo": (10.00, 30.00),
        "gpt-4-vision-preview": (10.00, 30.00),
        "gpt-3.5-turbo": (1.50, 2.00),
        "gpt-3.5-turbo-16k": (3.00, 4.00),
        "claude-instant-1.2": (0.163, 0.551),
        "claude-2": (8.00, 24.00),
        "claude-2.1": (8.00, 24.00),
        "claude-3-haiku-20240307": (0.25, 1.25),
        "claude-3-5-haiku-20241022": (1.00, 5.00),
        "claude-3-opus-20240229": (15.00, 75.00),
        "claude-3-sonnet-20240229": (3.00, 15.00),
        "claude-3-5-sonnet-20240620": (3.00, 15.00),
        "claude-3-5-sonnet-20241022": (3.00, 15.00),
        "gemini-pro": (0.5, 0.5),
        "gemini-1.0-pro": (0.5, 0.5),
        "gemini-1.5-pro": (1.25, 5.00),
        "gemini-1.5-flash": (0.075, 0.30),
    }

    def __init__(self, model: str):
        if model not in self.BASE_PRICING:
            raise ValueError(f"Model {model} not supported.")
        self.model = model

    def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        # Retrieve the base pricing for the selected model
        input_rate, output_rate = self.BASE_PRICING[self.model]

        # Calculate the costs using the cost per token
        input_cost = input_tokens * (input_rate / self.COST_PER_TOKEN)
        output_cost = output_tokens * (output_rate / self.COST_PER_TOKEN)

        # Return the total cost
        return input_cost + output_cost
