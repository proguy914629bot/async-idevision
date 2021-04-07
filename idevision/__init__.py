"""
MIT License

Copyright (c) 2021 proguy914629

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp

errorCodes = {
  "503": "Service Unavailable",
  "500": "Internal Server Error",
  "200": "Ok.",
  "400": "Bad Request.",
  "401": "Bad Authorization/Unauthorized.",
  "404": "Not found.",
  "403": "Banned.",
  "429": "Ratelimited.",
  "201": "Ok.",
  "204": "Ok."
}

def find(predicate, seq):
  for element in seq:
    if predicate(element):
      return element
  return None

__version__ = "0.9.3"

baseURL = "https://idevision.net"
Token = ""

class IDevisionException(Exception):
  """A Global Exception for the IDevision API."""
  def __init__(self, *args, **kwargs):
    return super().__init__(*args, **kwargs)

class BadAuthorization(IDevisionException):
  """An Exception when you are trying to access an API with bad authorization (No Token, Token Invalid, etc). This is a subclass of idevision.IDevisionException"""
  def __init__(self, endpoint):
    if len(Token) == 0:
      return super().__init__("A token is required to access the {} endpoint.")
    else:
      return super().__init__("You have passed an invalid token. Your current passed token is {}. You will not be able to access any other required token endpoints such as CDN and OCR if you do not change the current token passed.")
  
class Ratelimit(IDevisionException):
  """An Exception when you are Ratelimited. This is a subclass of idevision.IDevisionException"""
  def __init__(self):
    return super().__init__("You are currently ratelimited from IDevision API. You have recieved a 429 error code. Please follow the Ratelimit rules of IDevision from now on or you might get banned.")
  
class Banned(Ratelimit):
  """An Exception when you are Banned from the API. This is a subclass of idevision.Ratelimit."""
  def __init__(self):
    return super().__init__("You are banned from IDevision API. You have recieved a 403 error code.")
  
class BadRequest(IDevisionException):
  """An Exception when the API has raised a Bad Request. This is a subclass of idevision.IDevisionException"""
  
class BadArgument(IDevisionException):
  """An Exception when there is a bad argument to a parameter. This is a subclass of idevision.IDevisionException"""
  def __init__(self, argument, expectedVal, inputVal):
    return super().__init__(
      "A bad argument was raised in parameter {}. Expected value {} but got {} instead.".format(
        str(argument), str(expectedVal), str(inputVal)
      )
    )

class IDevision:
  def __init__(self, token : str = ""):
    """
    Async IDevision API Class.
    
    Parameters
    -----------
    token: :class:`str`
        The token for your IDevision API to access specific Endpoints.
    """
    self.token = token
    self.documentation = "https://idevision.net/docs"
    self.docs = "https://idevision.net/docs"
    self.baseURL = basseURL
    Token = token
    self.error_codes = errorCodes
    
  def documentation(self):
    def idevision():
      return "https://idevision.net/docs"
    def async_idevison():
      return "https://github.com/proguy914629bot/async-idevision/blob/main/DOCUMENTATION.md"
    
  class rtfs:
    async def __init__(self, query : str, library : str, *, format : str = "links"):
      """
      |coro|
      
      A helper for the RTFS API.
      
      Parameters
      -----------
      query: :class:`str`
          The query of the RTFS that you want to search for.
      library: :class:`str`
          The library that you need to search for.
      format: :class:`str`
          The format of the RTFS. Either `soruce` or `links`. Defaults to `links`.
      """
      lib = find(lambda m: library.lower() in m.lower(), ["discord.py", "twitchio", "wavelink", "aiohttp"])
      if not lib:
        raise BadArgument('library', 'discord.py/twitchio/wavelink/aiohttp', str(library))
      library = lib
      fr = find(lambda m: format.lower() in m.lower(), ["links", "source"])
      if not fr:
        raise BadArgument('format', 'links/source', str(format))
      format = fr
      params = {
        "query": query,
        "library": library,
        "format": format
      }
      async with aiohttp.ClientSession() as sess:
        async with sess.get(f"{baseURL}/api/public/rtfs", params=params) as resp:
          self = resp
          r = resp
      await sess.close()
      self.query = query
      self.format = format
      self.params = params
      self.library = library
      self.js = await r.json()
          
    @property
    def nodes(self) -> dict:
      """
      Returns a dict of the node name and URL/Source. 
      The dict will be in the format {"Node Name": "URL/Source of Documentation."}
      """
      return self.js["nodes"]
    
    @property
    def query_time(self) -> str:
      '''
      Returns a string of the query time. E.g "1.0".
      '''
      return self.js["query_time"]
  
  class rtfm:
    async def __init__(self, query : str, uri : str, *, show_labels : bool = True, label_labels = False):
      """
      |coro|
      
      A helper for the RTFM API.
      
      Parameters
      -----------
      query: :class:`str`
        The query of the RTFM that you want to search for.
      uri: :class:`str`
        The URL/URI of the documentation. This can be any sphinx generated documentation. Ex. https://discordpy.readthedocs.io/en/latest.
      show_labels: :class:`bool`
        Configures the labels. When False, labels will not be returned in the results. Defaults to True.
      label_labels: :class:`bool`
        When True, labels will have label: prepended to them. Does nothing when show-labels is False. Defaults to False
      """
      params = {
        "query": query,
        "location": uri,
        "show-labels": show_labels,
        "label-labels": label_labels
      }
      async with aiohttp.ClientSession() as sess:
        async with sess.get(f"{baseURL}/api/public/rtfm", params=params) as resp:
          self = resp
          r = resp
      await sess.close()
      self.query = query
      self.show_labels = show_labels
      self.params = params
      self.uri = uri
      self.label_labels = label_labels
      self.js = await r.json()
      
    @property
    def nodes(self) -> dict:
      """
      Returns a dict of the node name and URL/Source. 
      The dict will be in the format {"Node Name": "URL/Source of Documentation."}
      """
      return self.js["nodes"]
    
    @property
    def query_time(self) -> str:
      '''
      Returns a string of the query time. E.g "1.0".
      '''
      return self.js["query_time"]
      
