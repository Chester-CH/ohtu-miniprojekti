from entities.reading_tip import ReadingTip

from repositories.tips_repository import (
    tips_repository as default_tips_repository
)


class ReadingTipService:

    def __init__(self, tips_repository=default_tips_repository):
        """Constructor, which launchs the service
        Args:
            tips_repository ([type], optional): [description]. Defaults to default_tips_repository.
        """
        self._tips_repository = tips_repository

    def create_reading_tip(self, title):
        """Create a new reading tip.

        Args:
            title: string, which describes the title

        Returns: return reading tip

        """
        if not title:
            return None

        if self._tips_repository.create_tip(title):
            return True
        return None

    def remove_reading_tip(self, tip):
        """Remove the selected reading tip

        Args:
            int: which is the id of the tip
        Return true/false
        """
        if not tip:
            return False

        if self._tips_repository.remove_tip(tip.tip_id):
            return True
        return False
        

    def get_all_tips(self):
        """Show all the existing tips by listing
        Args: String
        Returns: return list of tips
        """
        return self._tips_repository.get_tips()

reading_tip_service = ReadingTipService()
