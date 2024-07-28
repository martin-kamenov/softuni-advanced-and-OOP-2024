from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer

class PremiumInfluencer(BaseInfluencer):

    PAYMENT_PERCENTAGE = 0.85

    def calculate_payment(self, campaign: LowBudgetCampaign or HighBudgetCampaign) -> float:
        payment = campaign.budget * PremiumInfluencer.PAYMENT_PERCENTAGE

        return payment

    def reached_followers(self, campaign_type: str) -> int:

        if campaign_type == 'HighBudgetCampaign':
            followers = self.followers * self.engagement_rate * 1.5
            return int(followers)

        elif campaign_type == 'LowBudgetCampaign':
            followers = self.followers * self.engagement_rate * 0.8
            return int(followers)

