from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5000
    PERCENT_ENGAGEMENT_RATE = 1.2

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return True if engagement_rate >= self.required_engagement * HighBudgetCampaign.PERCENT_ENGAGEMENT_RATE else False
