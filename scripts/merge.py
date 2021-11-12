from argparse import ArgumentParser

from tqdm import tqdm
from wikidata.client import Client
import json
from utils import iterator_from_file
from urllib.error import HTTPError

"""
Joining additional information from Wikidata
"""

id2gender = {
    "Q6581097": "male",
    "Q6581072": "female"
}


def _extract(e):
    if "mainsnak" in e:
        if "datavalue" in e["mainsnak"]:
            if "value" in e["mainsnak"]["datavalue"]:
                return e["mainsnak"]["datavalue"]["value"]
    return None


def get_birth(e):
    if "P569" in e:
        birth = _extract(e["P569"][0])
        if birth is not None:
            return birth["time"] if "time" in birth else None
    return None


def get_citizenship(e):
    if "P27" in e:
        citizenship_id = _extract(e["P27"][0])
        if citizenship_id is not None:
            return citizenship_id["id"] if "id" in citizenship_id else None
    return None


def get_gender(e):
    if "P21" in e:
        gender_id = _extract(e["P21"][0])
        if gender_id is not None:
            if "id" in gender_id:
                gender_id = gender_id["id"]
                if gender_id in id2gender:
                    return id2gender[gender_id]
    return None


def get_occupations(e):
    occupation_ids = []
    if "P106" in e:
        for j in range(len(e["P106"])):
            occupation_id = _extract(e["P106"][j])
            occupation_id = occupation_id["id"] if "id" in occupation_id else None
            occupation_ids.append(occupation_id)

            if j > 4:
                break
    return occupation_ids if occupation_ids else None


def join_wikidata(row, client):
    row["gender"], row["birth"], row["occupation_ids"], row["citizenship_id"] = [], [], [], []

    for i, id_ in enumerate(row["id"]):
        try:
            entity = client.get(id_, load=True).data["claims"]
        except HTTPError:
            continue

        birth = get_birth(entity)
        gender = get_gender(entity)
        citizenship_id = get_citizenship(entity)
        occupation_ids = get_occupations(entity)

        row["gender"].append(gender)
        row["birth"].append(birth)
        row["occupation_ids"].append(occupation_ids)
        row["citizenship_id"].append(citizenship_id)

        if i > 4:
            break

    return row


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    c = Client()

    it = map(json.loads, list(iterator_from_file(args.file)))
    merged = map(lambda row_: join_wikidata(row_, client=c), it)

    name, ext = args.file.split(".")
    name, _ = name.rsplit("-", maxsplit=1)
    output_file = f"{name}-merged.{ext}"

    with open(output_file, "a") as file:
        for row in tqdm(merged):
            json.dump(row, file)
            file.write("\n")
