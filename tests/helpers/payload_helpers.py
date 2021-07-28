VALID_PAYLOAD = {
    "name": "charizard",
    "is_legendary": False,
    "flavor_text_entries": [
        {
            "flavor_text": "It was created by\na scientist after\nyears of horrific\fgene splicing and\nDNA engineering\nexperiments.",
            "language": {"name": "en", "url": "testing"},
            "version": {"name": "red", "url": "testing"},
        }
    ],
    "habitat": {
        "name": "mountain",
        "url": "test",
    },
}


INVALID_DESCRIPTION_PAYLOAD = {
    "name": "charizard",
    "is_legendary": False,
    "flavor_text_entries": [
        {
            "flavor_text": "Mewtwo est un Pokémon créé par manipulation génétique.\nCependant, bien que les connaissances scientifiques des\nhumains aient réussi à créer son corps, elles n’ont pas pu\ndoter Mewtwo d’un cœur sensible.",
            "language": {"name": "fr", "url": "testing"},
            "version": {"name": "red", "url": "testing"},
        }
    ],
    "habitat": {
        "name": "mountain",
        "url": "test",
    },
}


INVALID_HABITAT_PAYLOAD = {
    "name": "charizard",
    "is_legendary": False,
    "flavor_text_entries": [
        {
            "flavor_text": "It was created by\na scientist after\nyears of horrific\fgene splicing and\nDNA engineering\nexperiments.",
            "language": {"name": "en", "url": "testing"},
            "version": {"name": "red", "url": "testing"},
        }
    ],
    "habitat": None,
}


TRANSLATOR_SUCCESS = {
    "success": {"total": 1},
    "contents": {
        "translated": "Lost a planet,  master obiwan has.",
        "text": "Master Obiwan has lost a planet.",
        "translation": "yoda",
    },
}


TRANSLATOR_RATE_LIMIT_EXCEEDED = {
    "error": {
        "code": 429,
        "message": "Too Many Requests: Rate limit of 5 requests per hour exceeded. Please wait for 59 minutes and 59 seconds.",
    }
}
