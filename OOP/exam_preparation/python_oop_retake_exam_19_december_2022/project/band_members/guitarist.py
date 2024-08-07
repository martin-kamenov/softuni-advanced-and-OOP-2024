from typing import List
from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE_SKILLS = [
         "play metal",
         "play rock",
         "play jazz"
    ]

    @property
    def available_skills(self) -> List[str]:
        return self.AVAILABLE_SKILLS