class LicenseXref:
    """
    I created this class to represent a single license relationship
    between one piece of content and one distributor.
    """

    def __init__(
        self,
        id: int,
        content_id: int,
        distributor_id: int,
        start_date: str | None = None,
        end_date: str | None = None,
        terms: str | None = None,
    ):
        # I added these fields so each license record knows:
        # - which content it belongs to
        # - which distributor holds the license
        # - when the license starts and ends
        # - any special contract terms

        self.id = id
        self.content_id = content_id
        self.distributor_id = distributor_id
        self.start_date = start_date
        self.end_date = end_date
        self.terms = terms
    # --------------------------------------------------------
    # String Helpers
    # I added these methods so I can easily print or inspect
    # a LicenseXref object when I'm debugging or reviewing data.
    # --------------------------------------------------------
    def __str__(self) -> str:
        return (
            f"License {self.id}: Content {self.content_id} -> "
            f"Distributor {self.distributor_id}"
        )

    def __repr__(self) -> str:
        return (
            f"LicenseXref(id={self.id!r}, content_id={self.content_id!r}, "
            f"distributor_id={self.distributor_id!r}, start_date={self.start_date!r}, "
            f"end_date={self.end_date!r}, terms={self.terms!r})"
        )
    # --------------------------------------------------------
    # Dictionary Conversion Helpers
    # I added these methods so I can easily convert the
    # LicenseXref object to a dictionary (for saving to SQLite)
    # and create a new LicenseXref object from a dictionary
    # (for loading data back out of SQLite).
    #
    # These methods will be called by the persistence layer:
    # - license_repo.py will use to_dict() before inserting
    # - db.py will fetch rows & turn them into dictionaries
    # - from_dict() will rebuild full objects for the service layer
    #
    # This keeps the data flow clean between all layers.
    # --------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this LicenseXref object into a clean dictionary."""
        return {
            "id": self.id,
            "content_id": self.content_id,
            "distributor_id": self.distributor_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "terms": self.terms
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Re-create a LicenseXref object from a dictionary."""
        return cls(
            id=data["id"],
            content_id=data["content_id"],
            distributor_id=data["distributor_id"],
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            terms=data.get("terms")
        )
