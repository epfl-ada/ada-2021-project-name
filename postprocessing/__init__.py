from .occupations_labeling import update_occupations, upd_single_occ
from .filter import filter_irrelevant, select_occupation
from .merge_occupations import (
    to_edges,
    to_graph,
    iterator_from_file,
    drop_similar,
    filter_outlier_wikidata,
    filter_rare_occupations
)

prefered_occs = [
    "programmer",
    "politician",
    "lawyer",
    "business",
    "economist",
    "science",
    "crypto"
]