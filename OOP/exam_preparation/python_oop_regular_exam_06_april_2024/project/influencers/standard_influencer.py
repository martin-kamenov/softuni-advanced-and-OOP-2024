from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.45

    @property
    def initial_payment_percentage(self) -> float:
        return self.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str) -> float:
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)

        if campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.9)