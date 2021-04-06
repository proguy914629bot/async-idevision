import aiohttp

def find(predicate, seq):
  for element in seq:
    if predicate(element):
      return element
  return None

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
    
  
