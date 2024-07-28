from project.campaigns.base_campaign import BaseCampaign

class LowBudgetCampaign(BaseCampaign):
    LOW_BUDGET_CAMPAIGN = 2500

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.LOW_BUDGET_CAMPAIGN, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= 0.9 * self.required_engagement

