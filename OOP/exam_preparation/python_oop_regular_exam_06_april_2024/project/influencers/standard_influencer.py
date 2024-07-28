from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer

class StandardInfluencer(BaseInfluencer):

    PAYMENT_PERCENTAGE = 0.45

    def calculate_payment(self, campaign: LowBudgetCampaign or HighBudgetCampaign) -> float:
        payment = campaign.budget * StandardInfluencer.PAYMENT_PERCENTAGE

        return payment

    def reached_followers(self, campaign_type: str):

        if campaign_type == "HighBudgetCampaign":
            followers = self.followers * self.engagement_rate * 1.2
            return int(followers)

        elif campaign_type == "LowBudgetCampaign":
            followers = self.followers * self.engagement_rate * 0.9
            return int(followers)
