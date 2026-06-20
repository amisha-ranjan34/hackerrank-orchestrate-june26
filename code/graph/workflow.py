# graph/workflow.py

from langgraph.graph import StateGraph
from graph.state import ClaimState

from graph.nodes import (

    claim_parser_node,
    image_node,
    evidence_node,
    history_node,
    consensus_node,
    formatter_node

)

builder = StateGraph(ClaimState)

# Nodes

builder.add_node(
    "claim_parser",
    claim_parser_node
)

builder.add_node(
    "image_analyzer",
    image_node
)

builder.add_node(
    "evidence_checker",
    evidence_node
)

builder.add_node(
    "history_agent",
    history_node
)

builder.add_node(
    "consensus_agent",
    consensus_node
)

builder.add_node(
    "formatter",
    formatter_node
)

# Flow

builder.set_entry_point(
    "claim_parser"
)

builder.add_edge(
    "claim_parser",
    "image_analyzer"
)

builder.add_edge(
    "image_analyzer",
    "evidence_checker"
)

builder.add_edge(
    "evidence_checker",
    "history_agent"
)

builder.add_edge(
    "history_agent",
    "consensus_agent"
)

builder.add_edge(
    "consensus_agent",
    "formatter"
)

graph = builder.compile()