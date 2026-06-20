# agents/history_agent.py

from loaders.history_loader import get_history


def analyze_history(user_id):

    history = get_history(user_id)

    risk_flags = []

    if not history:
        return {
            "risk_flags": ["none"]
        }

    if history[
        "rejected_claim"
    ] >= 3:

        risk_flags.append(
            "user_history_risk"
        )

    if history[
        "manual_review_claim"
    ] >= 3:

        risk_flags.append(
            "manual_review_required"
        )

    if len(risk_flags) == 0:
        risk_flags.append("none")

    return {

        "risk_flags": risk_flags,

        "history_summary":
            history.get(
                "history_summary",
                ""
            )
    }