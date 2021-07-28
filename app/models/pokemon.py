class Pokemon:
    name: str
    version: str
    description: str
    habitat: str
    is_legendary: bool

    def __init__(self, data, version="red"):
        self.name = data["name"]
        self.version = version
        self.description = Pokemon.english_descriptions(
            data["flavor_text_entries"], self.version
        )
        self.habitat = Pokemon.assign_habitat(data["habitat"])
        self.is_legendary = data["is_legendary"]

    @staticmethod
    def english_descriptions(descriptions, version):
        for d in descriptions:
            if d["language"]["name"] == "en" and d["version"]["name"] == version:
                return d["flavor_text"].replace("\n", " ").replace("\f", " ")
        return "Unknown"

    @staticmethod
    def assign_habitat(habitat):
        if habitat:
            return habitat["name"]
        return "Unknown"

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_description(self):
        return self.description

    def get_habitat(self):
        return self.habitat

    def get_is_legendary(self):
        return self.is_legendary
