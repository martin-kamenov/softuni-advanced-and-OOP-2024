from typing import List
from project.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_SKILLS = [
        "sing high pitch notes",
        "sing low pitch notes"
    ]

    @property
    def available_skills(self) -> List[str]:
        return self.AVAILABLE_SKILLS