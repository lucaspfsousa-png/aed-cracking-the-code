from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    if root is None:
        return -1

    if root.value == value1 or root.value == value2:
        return root.value

    left_lca = lowest_common_ancestor(root.left, value1, value2)
    right_lca = lowest_common_ancestor(root.right, value1, value2)

    if left_lca != -1 and right_lca != -1:
        return root.value

    return left_lca if left_lca != -1 else right_lca