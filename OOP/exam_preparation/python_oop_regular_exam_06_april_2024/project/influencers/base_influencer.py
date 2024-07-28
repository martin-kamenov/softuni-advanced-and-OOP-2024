from abc import ABC, abstractmethod
from typing import List

class BaseInfluencer(ABC):

    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        # if not value.strip():
        if value.strip() == '':
            raise ValueError("Username cannot be empty or consist only of whitespace!")

        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value: int):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")

        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement

    @engagement_rate.setter
    def engagement_rate(self, value: float):
        if not (0.0 <= value <= 5.0):
            raise ValueError("Engagement rate should be between 0 and 5.")

        self.__engagement = value

    @abstractmethod
    def calculate_payment(self, campaign):
        ...

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        ...

    # FLAG CHECK
    def display_campaigns_participated(self) -> str:
        if len(self.campaigns_participated) == 0:
            return f"{self.username} has not participated in any campaigns."

        result = [f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:"]

        for campaign in self.campaigns_participated:
            result.append(f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, "
                          f"Reached followers: {self.reached_followers(type(self).__name__)}")

        return '\n'.join(result)
