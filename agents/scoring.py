def score_negotiation(history, buyer_objectives: str):
    """
    Scores the negotiation outcome from the Buyer's perspective.

    Returns:
        score (int 0–100)
        reasons (list of strings)
    """

    score = 100
    reasons = []

    buyer_objectives_lower = buyer_objectives.lower()

    for h in history:
        buyer_text = h["buyer"].lower()

        if "unlimited liability" not in buyer_text and "cap" in buyer_objectives_lower:
            score -= 10
            reasons.append(
                f"Round {h['round']}: Buyer did not clearly preserve liability cap."
            )

        if "sole remedy" in buyer_text:
            score -= 5
            reasons.append(
                f"Round {h['round']}: Buyer may have accepted restrictive remedy language."
            )

        if "as is" in buyer_text:
            score -= 5
            reasons.append(
                f"Round {h['round']}: Buyer accepted 'as is' risk allocation."
            )

    # Clamp score
    score = max(0, min(score, 100))

    if score >= 85:
        reasons.insert(0, "Overall outcome strongly aligns with Buyer objectives.")
    elif score >= 65:
        reasons.insert(0, "Outcome is mixed; some Buyer concessions identified.")
    else:
        reasons.insert(0, "Outcome materially compromises Buyer objectives.")

    return score, reasons
