# graph/nodes.py

from agents.claim_parser import parse_claim
from agents.image_analyzer import analyze_images
from agents.evidence_agent import evaluate_evidence
from agents.history_agent import analyze_history
from agents.consensus_agent import consensus_decision
from agents.formatter_agent import format_output


def claim_parser_node(state):

    state["parsed_claim"] = parse_claim(
        state["user_claim"]
    )

    return state


def image_node(state):

    state["image_analysis"] = analyze_images(
        state["image_paths"],
        state["claim_object"],
        state["parsed_claim"]
    )

    return state


def evidence_node(state):

    state["evidence_result"] = evaluate_evidence(
        state["claim_object"],
        state["parsed_claim"]["issue_type"],
        state["image_analysis"]
    )

    return state


def history_node(state):

    state["history_result"] = analyze_history(
        state["user_id"]
    )

    return state


def consensus_node(state):

    state["final_decision"] = consensus_decision(

        parsed_claim=state["parsed_claim"],

        image_analysis=state["image_analysis"],

        evidence_result=state["evidence_result"],

        history_result=state["history_result"]

    )

    return state


def formatter_node(state):

    row = {

        "user_id": state["user_id"],

        "image_paths": ";".join(
            state["image_paths"]
        ),

        "user_claim": state["user_claim"],

        "claim_object": state["claim_object"]
    }

    state["output_row"] = format_output(

        row,

        state["final_decision"]

    )

    return state