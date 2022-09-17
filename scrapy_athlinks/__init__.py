from scrapy_athlinks.spiders.race import RaceSpider
from scrapy_athlinks.items import RaceItem, AthleteItem, AthleteSplitItem


__version__ = '0.0.1'


# Use __all__ to let type checkers know what is part of the public API.
# The public API is determined based on the documentation.
__all__ = [ 
  'AthleteItem',
  'AthleteSplitItem',
  'RaceItem',
  'RaceSpider',
  'items',
  'spiders'
]