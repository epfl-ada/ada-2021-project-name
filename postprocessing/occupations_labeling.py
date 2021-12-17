occ2synonyms = {
    "sport": [
        "sport", "archer", "player", 'football',
        "cricket", "rugby", 'basketball', "biathlon",
        "hockey", "fitness", "gymnastics", "baseball",
        "wrestling", "curling", "handball", "bobsledder",
        "badminton", "athlete", "runner", "tennis", "dancer",
        "skier", "skating", "golfer", "skier", "mountaineer",
        "surfer", "boxer", "sprinter", "skater", "aikidoka",
        "swimmer", "ufc light heavyweight championship",
        "ballerina", "ballet master", "bodybuilder", "bodybuilding",
        "boxing trainer", "brazilian jiu-jitsu practitioner",
        "formula one driver", "high jumper", "horse trainer",
        "judoka", "long jumper", "motocross rider", "netballer",
        "motorcycle development rider", "motorcycle rider",
        "motorcycle trials rider", "mountain biker", "race car driver",
        "racewalker", "racing automobile driver", "racing driver",
        "rhythmic gymnast", "sambo fighter", "shot putter",
        "show jumper", "skateboarder", "skeleton racer", "ski jumper",
        "skipper", "snowboarder", "stock car racing", "track cycling",
        "track cyclist", "trampoline gymnast", "wheelchair racer",
        "athletics competitor", "choreographer", "wrestler", "thrower",
        "trumpeter", "dressage rider", "jockey", "rower", "trumpeter",
        "competitive diver"
    ],
    "writer": [
        "poet", "essayist", "author", "autobiographer", "novelist",
        "playwright", "typographer", "columnist", "editor", "reporter",
        "writer", "columnist"
    ],
    "media": [
        "actor", "artist", "activist", "comedian", "composer", "motivational speaker",
        "podcaster", "presenter", "radio", "stunt performer", "painter", "blogger",
        "photographer", "singer", "musician", "drawer", "drummer", "cinematographer",
        "pianist"
    ],
    "programmer": [
        "programmer", "software developer", "software engineer", "engineer",
        "chief technology officer", "hacker"
    ],
    "politician": [
        "politician", "statesperson", "senator", "minister", "governor",
        "diplomat", "politics", "propagandist"
    ],
    "lawyer": [
        "lawyer", "jurist", "judge", "officer"
    ],
    "business": [
        "businessman", "administrator", "manager", "businessperson", "ceo",
        "director", "entrepreneur", "founder", "inventor", "investor", "judge",
        "lawyer", "owner", "chief operating officer", "chief executive officer",
        "cfo", "cpo", "chief product officer", "chief financial officer", "coo",
        "business", "entrepreneur"
    ],
    "economist": [
        "banker", "economist", "financier", "financist", "stockbroker", "trader"
    ],
    "science": [
        "chemist", "mathematician", "physicist", "scientist", "sociologist",
        "historian", "academic", "archeologist", 
    ],
    "crypto": [
        "cryptographer", "cryptologist"
    ],
}


def update_occupations(occupations_dict):
    for k, v in occupations_dict.items():
        for occ, syns in occ2synonyms.items():
            for syn in syns:
                if syn in v:
                    occupations_dict[k] = occ
        if "game" in v:
            occupations_dict[k] = "video-game"
        elif "chief executive officer" in v:
            occupations_dict[k] = "ceo"
    return occupations_dict


def upd_single_occ(x):
    for occ, syns in occ2synonyms.items():
        for syn in syns:
            if (x is not None) and (syn in x):
                return occ
    return x
