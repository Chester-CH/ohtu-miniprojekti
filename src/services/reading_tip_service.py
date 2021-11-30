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
        reading_tip = ReadingTip(title=title)
        if reading_tip:
            self._tips_repository.create_tip(reading_tip.title)
            return reading_tip


reading_tip_service = ReadingTipService()
