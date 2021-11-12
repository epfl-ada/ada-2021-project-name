from argparse import ArgumentParser

from tqdm import tqdm
from wikidata.client import Client
import json
from utils import iterator_from_file
from urllib.error import HTTPError

"""
Building vocabularies. Since requests to WikiData client requires a lot of time 
"""

def dump_vocab(path, ids):
    id2obj = {}
    for id_ in tqdm(ids):
        try:
            id2obj[id_] = str(client.get(id_, load=True).label)
        except HTTPError:
            continue

    with open(path, "a") as file:
        json.dump(id2obj, file)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    client = Client()

    it = map(json.loads, list(iterator_from_file(args.file)))
    occupations, countries = set(), set()
    for row in tqdm(it):
        for o_ids in row["occupation_ids"]:
            if o_ids is not None:
                occupations.update(o_ids)
        for c_ids in row["citizenship_id"]:
            if c_ids is not None:
                countries.update([c_ids, ])

    dump_vocab("data/occupations_vocab.json", occupations)
    dump_vocab("data/countries_vocab.json", countries)
