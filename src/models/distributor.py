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
