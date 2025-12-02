class Content:
    def __init__(
        self,
        id: int,
        title: str,
        genre: str | None = None,
        content_type: str | None = None,
        release_year: int | None = None,
        notes: str | None = None,
    ):
        self.id = id
        self.title = title
        self.genre = genre
        self.content_type = content_type
        self.release_year = release_year
        self.notes = notes

    def __str__(self) -> str:
        parts = [f"{self.id}: {self.title}"]
        if self.genre:
            parts.append(f"[{self.genre}]")
        if self.release_year:
            parts.append(f"({self.release_year})")
        return " ".join(parts)

    def __repr__(self) -> str:
        return (
            f"Content(id={self.id!r}, title={self.title!r}, "
            f"genre={self.genre!r}, content_type={self.content_type!r}, "
            f"release_year={self.release_year!r}, notes={self.notes!r})"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "content_type": self.content_type,
            "release_year": self.release_year,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            title=data["title"],
            genre=data.get("genre"),
            content_type=data.get("content_type"),
            release_year=data.get("release_year"),
            notes=data.get("notes"),
        )
