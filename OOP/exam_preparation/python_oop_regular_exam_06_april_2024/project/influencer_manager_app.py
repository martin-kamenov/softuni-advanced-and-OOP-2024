from typing import List
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer


class InfluencerManagerApp:

    INFLUENCERS_TYPES = {'StandardInfluencer': StandardInfluencer, 'PremiumInfluencer': PremiumInfluencer}
    CAMPAIGNS_TYPES = {'LowBudgetCampaign': LowBudgetCampaign, 'HighBudgetCampaign': HighBudgetCampaign}

    def __init__(self):
        self.influencers: List[StandardInfluencer or PremiumInfluencer] = []
        self.campaigns: List[LowBudgetCampaign or HighBudgetCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:
        if influencer_type not in self.INFLUENCERS_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self._get_influencer(username)
        if influencer is not None:
            return f"{username} is already registered."

        new_influencer = self.INFLUENCERS_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:
        if campaign_type not in self.CAMPAIGNS_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self._get_campaign(campaign_id)
        if campaign is not None:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.CAMPAIGNS_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:
        influencer = self._get_influencer(influencer_username)
        campaign = self._get_campaign(campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        influencer_payment = influencer.calculate_payment(campaign)

        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' has successfully participated "
                    f"in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self) -> dict:
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + reached_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str) -> str:
        influencer = self._get_influencer(username)

        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()

        sorted_campaign = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        campaign_stats = [
            f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
            f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers.get(campaign, 0)}"
            for campaign in sorted_campaign
        ]

        return f"$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)

    def _get_influencer(self, username: str):
        influencer = next((i for i in self.influencers if i.username == username), None)

        return influencer

    def _get_campaign(self, campaign_id):
        campaign = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)

        return campaign