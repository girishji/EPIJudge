from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(
    final_score: int, individual_play_scores: List[int]
) -> int:
    # think of a x i, b x j...
    result = 0
    cumulative = {}
    for i, score in enumerate(individual_play_scores):
        cumulative[i] = []
        for j in range((final_score // score) + 1):
            cumulative[i].append(j * score)

    def solve(play_idx, score):
        nonlocal result, final_score, cumulative
        # print(play_idx, score)
        if score == final_score:
            result += 1
            return
        if score < final_score and play_idx < len(individual_play_scores):
            for sc in cumulative[play_idx]:
                # print("sc", sc)
                if score + sc > final_score:
                    break
                solve(play_idx + 1, score + sc)

    solve(0, 0)
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
