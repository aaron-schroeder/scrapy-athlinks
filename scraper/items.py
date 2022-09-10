"""Define here the models for your scraped items

See documentation in:
https://docs.scrapy.org/en/latest/topics/items.html
"""

from scrapy import Item, Field


class AthleteItem(Item):
  name = Field()  # str
  split_data = Field()  # list(AthleteSplitItem)


class AthleteSplitItem(Item):
  # Split data collected in selenium package: 
  #   "split", "Overall", "Gender", "Division", "Pace", "Time"
  # I really only care about the split time, everything else is of
  # dubious value to me.
  name = Field()  # str
  time_ms = Field()  # int
  # Optional (not sure if this matters)
  number = Field()  # int
  time_with_penalties_ms = Field()  # int
  distance_m = Field()  # int


class RaceItem(Item):
  """Unsure if this is needed, or something else like MetaDataItem
  
  Thinking the entire file represents the race, no need to create
  a container for everything
  """
  name = Field()  # str
  # athletes = Field()  # list(AthleteItem)
  # divisions = Field() # list() -> consider
  event_id = Field()
  event_course_id = Field()
  date_utc_ms = Field()  # is this typically done?
  distance_m = Field()
  split_info = Field()  # list
  # Other stuff too, see sample_race_meta_response

