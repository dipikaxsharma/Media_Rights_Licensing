class Distributor:
    def __init__(self, id: int, name: str, contact_email: str | None = None, region: str | None = None):
        self.id = id
        self.name = name
        self.contact_email = contact_email
        self.region = region
    def __str__(self) -> str:
        parts = [f"{self.id}: {self.name}"]
        if self.region:
            parts.append(f"[{self.region}]")
        return " ".join(parts)

    def __repr__(self) -> str:
        return (
            f"Distributor(id={self.id!r}, name={self.name!r}, "
            f"contact_email={self.contact_email!r}, region={self.region!r})"
        )
    # ---------------------------------------------
    # Serialization Helpers
    # I added these so I can easily convert a Distributor
    # object into a dictionary and back again.
    #
    # I’ll need this when saving/loading data through the
    # SQLite persistence layer, and it will also help later
    # when testing or printing data.
    # ---------------------------------------------
    def to_dict(self) -> dict:
        """Convert this Distributor into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "contact_email": self.contact_email,
            "region": self.region
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Re-create a Distributor object from a dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            contact_email=data.get("contact_email"),
            region=data.get("region")
        )
