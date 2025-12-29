def final_arbitration(history):
    """
    Produces an arbitration prompt based on the full negotiation history.
    The LLM decides the most balanced, enforceable final clause.
    """

    history_text = ""

    for h in history:
        history_text += f"""
Round {h['round']}:
Supplier proposal:
{h['supplier']}

Buyer counter:
{h['buyer']}
"""

    arbiter_prompt = f"""
You are a neutral legal ARBITER.

Below is the full negotiation history between Supplier and Buyer:
{history_text}

Your task:
1. Identify where each side overreached
2. Select or synthesise the most balanced drafting
3. Produce ONE final, clean contract clause
4. Ensure internal consistency and legal enforceability
5. Prefer market-standard and precedent-aligned drafting

Return ONLY the final clause text.
"""

    return arbiter_prompt
