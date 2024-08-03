from typing import List
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    INFLUENCERS_TYPE = {
        'PremiumInfluencer': PremiumInfluencer,
        'StandardInfluencer': StandardInfluencer
    }
    CAMPAIGN_TYPES = {
        'HighBudgetCampaign': HighBudgetCampaign,
        'LowBudgetCampaign': LowBudgetCampaign
    }


    def __init__(self):
        self.influencers: List[PremiumInfluencer or StandardInfluencer] = []
        self.campaigns: List[HighBudgetCampaign or LowBudgetCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:
        if influencer_type not in InfluencerManagerApp.INFLUENCERS_TYPE:
            return f"{influencer_type} is not an allowed influencer type."

        if self._get_influencer(username):
            return f"{username} is already registered."

        influencer = InfluencerManagerApp.INFLUENCERS_TYPE[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:
        if campaign_type not in InfluencerManagerApp.CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        if self._get_campaign(campaign_id):
            return f"Campaign ID {campaign_id} has already been created."

        campaign = InfluencerManagerApp.CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:
        influencer = self._get_influencer(influencer_username)
        campaign = self._get_campaign(campaign_id)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)

            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self) -> dict:
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                total_followers = influencer.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + total_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str) -> str:
        influencer = self._get_influencer(username)

        if len(influencer.campaigns_participated) < 1:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self) -> str:
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = f"$$ Campaign Statistics $$\n"
        result += '\n'.join(f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
                            f"Total budget: ${c.budget:.2f}, Total reached followers: "
                            f"{self.calculate_total_reached_followers().get(c, 0)}" for c in sorted_campaigns)

        return result

    def _get_influencer(self, username):
        return next(filter(lambda x: x.username == username, self.influencers), None)

    def _get_campaign(self, campaign_id):
        return next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns), None)
