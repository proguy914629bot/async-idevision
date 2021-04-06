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

class IDevision:
  def __init__(self, token : str):
    self.token = token
    Token = token
    
  class rtfs:
    async def __init__(self, query : str, library : str, *, format : str = "links"):
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
    def nodes(self):
      return self.js["nodes"]
    
    @property
    def query_time(self):
      return self.js["query_time"]
    
  
