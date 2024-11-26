# agent_watch/utils.py

def calculate_carbon_emissions(total_tokens: int, model: str) -> float:
    # Placeholder for actual carbon calculation
    # This can be replaced with a real formula or API call
    emissions_per_token = {
        "gpt-4o": 0.0001,      # kg CO2 per token
        "gpt-4o-mini": 0.00005
    }
    return total_tokens * emissions_per_token.get(model, 0)
