import json
from argparse import ArgumentParser

from tqdm import tqdm
from string import punctuation
from fuzzywuzzy import fuzz


def transform_to_dict(line: str) -> dict:
    row = json.loads(line)
    del row["quoteID"]
    del row["urls"]
    del row["phase"]
    del row["probas"]

    row["q"] = row["quotation"]
    del row["quotation"]
    row["d"] = row["date"]
    del row["date"]
    row["id"] = row["qids"]
    del row["qids"]
    row["s"] = row["speaker"]
    del row["speaker"]
    row["o"] = row["numOccurrences"]
    del row["numOccurrences"]

    return row


def filter_empty(row: dict) -> bool:
    return (row["s"] != "None") and (row["id"])


def filter_punctuation(row: dict):
    row["q"] = ''.join(ch for ch in row["q"] if ch not in punctuation)
    return row


def lowercase_(row: dict):
    row["q"] = row["q"].lower()
    return row


def iterator_from_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line


def filter_tags(rows: dict, tags: list) -> bool:
    ratios = [fuzz.partial_ratio(rows["q"], tag) for tag in tags]
    return max(ratios) >= 85


def preprocess(it_):
    rows = map(transform_to_dict, it_)
    rows = filter(filter_empty, rows)
    rows = map(filter_punctuation, rows)
    rows = map(lowercase_, rows)

    tags = ["blockchain", "bitcoin", "cryptocoin", "crypto", "cryptocurrency", "cryptotrading"]
    rows = filter(lambda rows_: filter_tags(rows_, tags=tags), rows)
    return rows


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    name, ext = args.file.split(".")
    output_file = f"{name}-processed.{ext}"

    it = preprocess(iterator_from_file(args.file))
    with open(output_file, "a") as file:
        for row in tqdm(it):
            json.dump(row, file)
            file.write("\n")
