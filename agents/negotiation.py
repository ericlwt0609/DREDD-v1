def run_multi_round_negotiation(
    initial_clause: str,
    buyer_objectives: str,
    supplier_objectives: str,
    llm_call,
    rounds: int = 3,
):
    """
    Runs a multi-round adversarial negotiation between Supplier and Buyer.

    Returns:
        history: list of dicts with keys:
            round, supplier, buyer
    """

    history = []
    current_clause = initial_clause

    for r in range(1, rounds + 1):

        supplier_prompt = f"""
You are the SUPPLIER in a contract negotiation.

Your objectives (must not be violated):
{supplier_objectives}

Current clause:
{current_clause}

Task:
- Propose revised drafting favourable to the Supplier
- Justify changes briefly
- Do NOT concede beyond your objectives
"""

        supplier_response = llm_call(supplier_prompt)

        buyer_prompt = f"""
You are the BUYER in a contract negotiation.

Your objectives (must not be violated):
{buyer_objectives}

Supplier has proposed the following revision:
{supplier_response}

Task:
- Counter-propose drafting favourable to the Buyer
- Identify risks in Supplier's proposal
- Do NOT concede beyond your objectives
"""

        buyer_response = llm_call(buyer_prompt)

        history.append(
            {
                "round": r,
                "supplier": supplier_response,
                "buyer": buyer_response,
            }
        )

        # Buyer proposal becomes the working clause for next round
        current_clause = buyer_response

    return history
