GRAPH_WITHOUT_CYCLE = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
}


GRAPH_WITH_CYCLE = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}


GRAPH_WITH_SELF_LOOP = {
    "A": ["A"],
}


DISCONNECTED_GRAPH = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": [],
}


DISCONNECTED_GRAPH_WITH_CYCLE = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": ["C"],
}
