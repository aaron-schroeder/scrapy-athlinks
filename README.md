# athlinks-scraper-scrapy: web scraper for race results hosted on Athlinks

[![License](https://img.shields.io/github/license/aaron-schroeder/athlinks-scraper-scrapy)](LICENSE)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)


## Dependencies

[Scrapy](https://scrapy.org/) is required.

## Included spiders

### [Race results spider](scraper/spiders/race.py)

This spider collects every athlete's split times from a chosen race on Athlinks,
along with some metadata about the race itself.

<!--## Documentation

The official documentation is hosted on readthedocs.io: https://athlinks-scraper-scrapy.readthedocs.io/en/stable. -->

## Usage

### Command line

Create and activate a python virtual environment of your choice,
then from the command line:

```sh
git clone https://github.com/aaron-schroeder/athlinks-scraper-scrapy
cd athlinks-scraper-scrapy
pip install -r requirements.txt
scrapy crawl race -a url=https://www.athlinks.com/event/33913/results/Event/1018673
```

### In a python script

Scrapy also supports running the scraper from a script.
[An example is included in this repo](scrapy_script.py).

## Testing

```
make tests
```

## License

[![License](https://img.shields.io/github/license/aaron-schroeder/athlinks-scraper-scrapy)](LICENSE)

This project is licensed under the MIT License. See
[LICENSE](LICENSE) file for details.

## Contact

You can get in touch with me at the following places:

- Website: [trailzealot.com](https://trailzealot.com)
- LinkedIn: [linkedin.com/in/aarondschroeder](https://www.linkedin.com/in/aarondschroeder/)
- GitHub: [github.com/aaron-schroeder](https://github.com/aaron-schroeder)