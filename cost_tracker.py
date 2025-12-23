# cost_tracker.py

MODEL_PRICING = {
    "gpt-4": {
        "input": 0.03 / 1000,
        "output": 0.06 / 1000
    }
}

def calculate_cost(model, input_tokens, output_tokens):
    price = MODEL_PRICING.get(model)
    if not price:
        return 0.0

    return round(
        input_tokens * price["input"] +
        output_tokens * price["output"],
        6
    )
