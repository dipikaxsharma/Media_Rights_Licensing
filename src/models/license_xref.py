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
