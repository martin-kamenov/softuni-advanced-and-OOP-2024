from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85

    @property
    def initial_payment_percentage(self) -> float:
        return self.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str) -> float:
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)

        if campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)