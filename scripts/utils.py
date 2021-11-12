import networkx
from networkx.algorithms.components.connected import connected_components
from fuzzywuzzy import fuzz
from collections import defaultdict, Counter

"""
Usefull utils functions for both analysis notebook and downloading scripts
"""

def iterator_from_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line

def to_graph(cliques):
    G = networkx.Graph()
    for cli in cliques:
        G.add_nodes_from(cli)
        G.add_edges_from(to_edges(cli))
    return G

def to_edges(l):
    it = iter(l)
    last = next(it)

    for current in it:
        yield last, current
        last = current
    
def drop_similar(occupations_dict):
    occ_lst = list(set(occupations_dict.keys()))

    G = networkx.Graph()
    G.add_nodes_from(occ_lst)

    edges = []
    for o_i in occ_lst:
        for o_j in occ_lst:
            if fuzz.partial_ratio(occupations_dict[o_i], occupations_dict[o_j]) > 90:
                edges.append((o_i, o_j))
    G.add_edges_from(edges)
    cliques = list(networkx.find_cliques(G))
    G_ = to_graph(cliques)

    simmilar_occupasions = list(connected_components(G_))
    id2name = {}

    for elem in simmilar_occupasions:
        if len(elem) > 1:
            lst = list(elem)
            words = sum([occupations_dict[e].split(" ") for e in lst], [])
            name = Counter(words).most_common()[0][0]
            for e in lst:
                occupations_dict[e] = name
    return occupations_dict

def filter_rare_occupations(x, occ_freq):
    ids = defaultdict(list)
    for i, occ_ids in enumerate(x["occupation_ids"]):
        ids[i] = []
        if occ_ids is not None:
            for j, occs in enumerate(occ_ids):
                if (occs is not None) and (occ_freq[occs] > 1):
                    ids[i].append(j)
    for i, elem in ids.items():
        if elem:
            x["occupation_ids"][i] = [e for j, e in enumerate(x["occupation_ids"][i]) if j in elem]
    return x

def filter_outlier_wikidata(x):
    if len(x["gender"]) > 1:
        new_genders = []
        new_citizenship = []
        new_birth = []
        new_occupations = []
        
        gender_counter, citizenship_counter = Counter(x["gender"]), Counter(x["citizenship_id"])
        frequent_gender, _ = gender_counter.most_common()[0]
        if (frequent_gender == None) and len(gender_counter.most_common()) > 1:
            frequent_gender, _ = gender_counter.most_common()[1]
        
        frequent_citizenship, _ = citizenship_counter.most_common()[0]
        if (frequent_citizenship == None) and len(citizenship_counter.most_common()) > 1:
            frequent_citizenship, _ = citizenship_counter.most_common()[1]
        
        for i, (g, c) in enumerate(zip(x["gender"], x["citizenship_id"])):
            if (g == frequent_gender) and \
               (c == frequent_citizenship) and \
               ((x["birth"][i] is not None) and (int(x["birth"][i][1:5]) >= 1900)):
                new_genders.append(g)
                new_citizenship.append(c)
                new_birth.append(x["birth"][i][1:11])
                new_occupations.append(x["occupation_ids"][i])
        x["birth"], x["occupation_ids"], x["gender"], x["citizenship_id"] = new_birth, new_occupations, new_genders, new_citizenship
    return x

def update_occupations(occupations_dict):
    sport_words = [
        "sport", "archer", "player", 'football', 
        "cricket", "rugby", 'basketball', "biathlon", 
        "hockey", "fitness", "gymnastics", "baseball",
        "wrestling", "curling", "handball", "bobsledder",
        "badminton", "athlete", "runner", "tennis", "dancer",
        "skier", "skating", "golfer", "skier", "mountaineer", 
        "surfer", "boxer", "sprinter", "skater", "aikidoka",
        "swimmer", "ufc light heavyweight championship"
    ]

    for k, v in occupations_dict.items():
        for sport_word in sport_words:
            if sport_word in v:
                occupations_dict[k] = "sport"
        if "game" in v:
            occupations_dict[k] = "video-game"
        elif "artist" in v:
            occupations_dict[k] = "artist"
        elif "actor" in v:
            occupations_dict[k] = "actor"
        elif "chief executive officer" in v:
            occupations_dict[k] = "executive-director"
        elif "chief creative officer" in v:
            occupations_dict[k] = "creative-director"
        elif "chief technology officer" in v:
            occupations_dict[k] = "technology-director"
        elif "chief operating officer" in v:
            occupations_dict[k] = "operating-director"
    return occupations_dict
            