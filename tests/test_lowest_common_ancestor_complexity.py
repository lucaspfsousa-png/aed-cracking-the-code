from time import sleep

import big_o

from challenges.lowest_common_ancestor import (
    lowest_common_ancestor,
)

from tests.complexities import (
    NOTATIONS,
    ComplexityInferenceData,
    infer_complexity,
    measure_execution_times,
)

from tests.generators import (
    generate_balanced_bst,
)


def lca_wrapper(data):
    root, value1, value2 = data

    return lowest_common_ancestor(
        root,
        value1,
        value2,
    )


def test_evaluate_time_lca():
    highest_acceptable_complexity = (
        big_o.complexities.Linear
    )

    for _ in range(3):

        data = ComplexityInferenceData(
            analyzed_function=lca_wrapper,
            generation_function=generate_balanced_bst,
            order_of_magnitude=5,
            initial_order=2,
            base_of_magnitude=3,
            execution_quantity=10,
            times_to_repeat=3,
        )

        results = measure_execution_times(data)

        observed_complexity = infer_complexity(
            results.registered_sizes,
            results.registered_times,
        )

        if (
            observed_complexity
            <= highest_acceptable_complexity
        ):
            break

        sleep(3)

    else:
        assert False, (
            "Seu algoritmo parece ser "
            f"{NOTATIONS[observed_complexity.__class__]}"
            ", mas deveria ser no máximo "
            f"{NOTATIONS[highest_acceptable_complexity]}"
        )
