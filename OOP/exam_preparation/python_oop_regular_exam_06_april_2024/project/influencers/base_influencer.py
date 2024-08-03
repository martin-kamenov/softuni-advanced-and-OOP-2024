from abc import ABC, abstractmethod
from typing import List
from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):

    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List[BaseCampaign] = []

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        if value.strip() == '':
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self) -> int:
        return self.__followers

    @followers.setter
    def followers(self, value: int):
        if not value >= 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value
        
    @property
    def engagement_rate(self) -> float:
        return self.__engagement_rate
    
    @engagement_rate.setter
    def engagement_rate(self, value: float):
        if not (0.0 <= value <= 5.0):
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @property
    @abstractmethod
    def initial_payment_percentage(self):
        ...

    def calculate_payment(self, campaign: BaseCampaign) -> int:
        return campaign.budget * self.initial_payment_percentage

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        ...

    def display_campaigns_participated(self) -> str:
        if len(self.campaigns_participated) > 0:
            result = f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:\n"
            result += '\n'.join(f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, "
                                f"Reached followers: {self.reached_followers(type(campaign).__name__)}"
                                for campaign in self.campaigns_participated)
            return result

        return f"{self.username} has not participated in any campaigns."
