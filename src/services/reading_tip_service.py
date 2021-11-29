from entities.reading_tip import ReadingTip
from repositories.tips_repository import (tips_repository as default_tips_repository)

def __init__(self, tips_repository=default_tips_repository     
    ):
    self._tips_repository = tips_repository

def create_reading_tip(content):    

    return self.tips_repository.create_tip(reading_tip.title)