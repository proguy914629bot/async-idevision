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

def find(predicate, seq):
  for element in seq:
    if predicate(element):
      return element
  return None

__version__ = "0.9.1"

baseURL = "https://idevision.net"
Token = ""

class IDevisionException(Exception):
  """A Global Exception for the IDevision API."""

class BadAuthorization(IDevisionException):
  """An Exception when you are trying to access an API with bad authorization (No Token, Token Invalid, etc). This is a subclass of idevision.IDevisionException"""
  
class Ratelimit(IDevisionException):
  """An Exception when you are Ratelimited. This is a subclass of idevision.IDevisionException"""
  
class Banned(Ratelimit):
  """An Exception when you are Banned from the API. This is a subclass of idevision.Ratelimit."""
  
class BadRequest(IDevisionException):
  """An Exception when the API has a Bad Request. This is a subclass of idevision.IDevisionException"""
  
class MissingRequiredArgument(IDevisionException):
  """An Exception when a """

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
    
  class rtfs:
    async def __init__(self, query : str, library : str, *, format : str = "links"):
      """
      |coro|
      
      A helper for the RTFS API.
      """
      library = find(lambda m: library.lower() in m.lower(), ["discord.py", "twitchio", "wavelink", "aiohttp"])
      format = find(lambda m: format.lower() in m.lower(), ["links", "source"])
      params = {
        "query": query,
        "library": library,
        "format": format
      }
      async with aiohttp.ClientSession() as sess:
        async with sess.get(f"{baseURL}/api/public/rtfs", params=params) as resp:
          self = resp
          r = resp
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
  
  #class rtfm:
    #async def __init__(self, query : str)
