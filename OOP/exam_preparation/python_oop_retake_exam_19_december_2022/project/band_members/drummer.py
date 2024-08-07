from typing import List
from project.band_members.musician import Musician


class Drummer(Musician):
    AVAILABLE_SKILLS = [
         "play the drums with drumsticks",
         "play the drums with drum brushes",
         "read sheet music"
    ]

    @property
    def available_skills(self) -> List[str]:
        return self.AVAILABLE_SKILLS