from collections import defaultdict, Counter

def filter_irrelevant(x):
    return (" a bit " not in x) and \
        (" little bit " not in x) and \
        (" least bit concerned " not in x) and \
        (" every bit confident " not in x) and \
        (" the least bit coincidental " not in x) and \
        ("bitching " not in x) and \
        ("bitching " not in x) and \
        (" bitching" not in x) and \
        ("bitchin " not in x) and \
        ("bitchin " not in x) and \
        (" bitchin" not in x) and \
        (" cryptus " not in x) and \
        (" cryptus" not in x) and \
        ("cryptus " not in x) and \
        (" cryptic " not in x) and \
        (" cryptic" not in x) and \
        ("cryptic " not in x) and \
        (" cryptum " not in x) and \
        (" cryptum" not in x) and \
        ("cryptum " not in x) and \
        (" cryptex " not in x) and \
        (" cryptex" not in x) and \
        ("cryptex " not in x) and \
        (" cryptoriana " not in x) and \
        (" cryptoriana" not in x) and \
        ("cryptoriana " not in x) and \
        (" cryptonazi " not in x) and \
        (" cryptonazi" not in x) and \
        ("cryptonazi " not in x) and \
        (" crypto-nazi " not in x) and \
        (" crypto-nazi" not in x) and \
        ("crypto-nazi " not in x) and \
        (" crypto nazi " not in x) and \
        (" crypto nazi" not in x) and \
        ("crypto nazi " not in x) and \
        (" cryptozoology " not in x) and \
        (" cryptozoology" not in x) and \
        ("cryptozoology " not in x) and \
        (" cryptozoologi " not in x) and \
        (" cryptozoologi" not in x) and \
        ("cryptozoologi " not in x) and \
        (" cryptochrome " not in x) and \
        (" cryptochrome" not in x) and \
        ("cryptochrome " not in x) and \
        (" bitbucket " not in x) and \
        (" bitbucket" not in x) and \
        ("bitbucket " not in x) and \
        (" bitwarden " not in x) and \
        (" bitwarden" not in x) and \
        ("bitwarden " not in x)


def select_occupation(x, occupations_dict, prefered_occs):
    output = []
    for elem in x:
        if elem is not None:
            output += list(occupations_dict[e] for e in elem)
    output = [o for o in output if o != "cryptozoologist"]
    result = [item for item, c in Counter(output).most_common()]
    if not output:
        return None
    else:
        for o in output:
            if "crypto" in o:
                return o

        if len(output) > 1:
            for n in prefered_occs:
                if n in output:
                    return n

        first = output[0].strip()
        if first in ["sport", "writer", "media"]:
            if len(output) > 1:
                return output[1]
        else:
            return output[0]
