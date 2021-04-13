import argparse
import os
from metrics import metrics


if __name__ == '__main__':
    ## Info & args
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--seed", type=int, default=None, help=\
        "Optional random number seed value to make toolbox deterministic.")
    parser.add_argument("--predictions", type=str, default='/home/ubuntu/google-landmark/landmark-retrieval/baseline/inference_results/16250/prediction.csv')
    parser.add_argument("--groundtruth", type=str, default='/home/ubuntu/google-landmark/retrieval_solution_v2.1.csv')

    args = parser.parse_args()

    metrics(args.groundtruth, args.predictions)