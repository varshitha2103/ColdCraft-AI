from ollama import Client

client = Client(host='http://localhost:11434')  # Default Ollama endpoint

def generate_email_variant(offer, lead_type, variation):
    prompt = f"""
    You are an expert B2B marketer. Write a cold email (version {variation}) for this:

    - Offer: {offer}
    - Lead Type: {lead_type}

    Keep it short, persuasive, and human-sounding. Avoid AI references or generic templates.
    """
    response = client.generate(model="mistral", prompt=prompt)
    return response['response']
