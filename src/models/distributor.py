class Distributor:
    def __init__(self, id: int, name: str, contact_email: str | None = None, region: str | None = None):
        self.id = id
        self.name = name
        self.contact_email = contact_email
        self.region = region
