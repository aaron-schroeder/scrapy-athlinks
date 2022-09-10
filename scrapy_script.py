"""Run scrapy from a python script rather than command line.

Refs:
  https://doc.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
  https://stackoverflow.com/questions/53542201/when-scrapy-finishes-i-want-to-create-a-dataframe-from-all-data-crawled
  https://gitlab.com/gallaecio/versiontracker/blob/master/versiontracker/pipelines.py
  https://gitlab.com/gallaecio/versiontracker/blob/master/versiontracker/__init__.py#L212
 
"""
import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.race import RaceSpider


DIR_OUT = 'data'
RACE_URLS = {
  'horsetooth': 'https://www.athlinks.com/event/4984/results/Event/1017004/Course/2242309/Results',
  'leadville': 'https://www.athlinks.com/event/33913/results/Event/1018673/Course/2248652'
}


def scrape_athlete_results_jl(race_url):
  """Scrape a race's results and output as a jl file"""
  settings = get_project_settings()

  # https://docs.scrapy.org/en/latest/topics/feed-exports.html#storage-uri-parameters
  fname = os.path.join(DIR_OUT, '%(event_id)s_athletes.jl')

  # https://docs.scrapy.org/en/latest/topics/feed-exports.html#feeds
  settings['FEEDS'] = {
    fname: {
      'format':'jsonlines',
      'overwrite': True,

      # list of item classes to export. 
      # Falls back to FEED_EXPORT_FIELDS (default None)
      # (If undefined or empty, all items are exported.)
      'item_classes': ['scraper.items.AthleteItem'],
    }
  }

  process = CrawlerProcess(settings=settings)
  process.crawl(RaceSpider, race_url)
  process.start()


def scrape_athlete_results_json(race_url):
  """Scrape a race's results and output as a json file"""
  settings = get_project_settings()  
  settings['ITEM_PIPELINES'] = {
    'scraper.pipelines.SingleJsonWriterPipeline': 300,
  }
  settings['DIR_OUT'] = DIR_OUT
  process = CrawlerProcess(settings=settings)
  process.crawl(RaceSpider, race_url)
  process.start()


def scrape_athlete_results_json_simple(race_url):
  settings = get_project_settings()
  fname_json = os.path.join(DIR_OUT, '%(event_id)s.json')
  settings['FEEDS'] = {
    fname_json: {  # parameters
      'format':'json',

      # default False for local storage
      'overwrite': True,
    },
  }
  process = CrawlerProcess(settings=settings)
  process.crawl(RaceSpider, race_url)
  process.start()


if __name__ == '__main__':
  if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

  scrape = scrape_athlete_results_json
  # scrape = scrape_athlete_results_jl
  # scrape = scrape_athlete_results_json_simple

  # scrape(RACE_URLS['horsetooth'])
  scrape(RACE_URLS['leadville'])