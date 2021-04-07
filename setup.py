import setuptools
from idevision import __version__ as version

with open("README.md", "r", encoding="utf-8") as fp:
  long_desc = fp.read()
  
setuptools.setup(
  name = "idevision",
  version = version,
  author = "proguy914629",
  description = "An async wrapper for the IDevision API",
  long_description = long_desc,
  long_description_content_type = "text/markdown",
  url = "https://github.com/proguy914629bot/async-idevision",
  python_requires = ">=3.6",
  install_requires = ["aiohttp"]
)
