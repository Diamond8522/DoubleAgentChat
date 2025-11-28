# --- Agent Response Function (UPDATED) ---
def generate_agent_response(persona_name, system_prompt, history):
    """Generates a response from a specific agent (Violet or Storm)."""
    
    # Compile the full message history, including the system prompt
    messages = [{"role": "system", "content": system_prompt}] + history

    # Set parameters to discourage repetition
    TEMP = 0.7  # Higher temperature (0.5 to 0.9) adds creativity/randomness
    # Groq's API uses 'frequency_penalty' instead of 'repetition_penalty' for this model
    FREQ_PENALTY = 0.5 # Positive values discourage repeating existing tokens
    
    try:
        completion = groq_client.chat.completions.create(
            model="mixtral-8x7b-32768", 
            messages=messages,
            temperature=TEMP, 
            frequency_penalty=FREQ_PENALTY # The fix for repeating sentences!
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"🚨 {persona_name} Agent Failure: Could not connect to Groq. Error: {e}"