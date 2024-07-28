from project.campaigns.base_campaign import BaseCampaign

class HighBudgetCampaign(BaseCampaign):
    HIGH_BUDGET_CAMPAIGN = 5000

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.HIGH_BUDGET_CAMPAIGN, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= 1.2 * self.required_engagement

