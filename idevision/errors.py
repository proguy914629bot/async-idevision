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

class IDevisionException(Exception):
  """A Global Exception for the IDevision API."""
  def __init__(self, *args, **kwargs):
    return super().__init__(*args, **kwargs)
  
class InternalServerError(IDevisionException):
  """An Exception when the IDevison API returns a 503 Status Code."""
  def __init__(self):
    super().__init__("API Returned a 500 Status Code.")

class BadAuthorization(IDevisionException):
  """An Exception when you are trying to access an API with bad authorization (No Token, Token Invalid, etc). This is a subclass of idevision.IDevisionException"""
  def __init__(self, endpoint = None):
    endpoint = endpoint or ""
    if len(Token) == 0:
      super().__init__("A token is required to access the %s endpoint." % endpoint)
    else:
      super().__init__("Invalid Token.")
  
class Ratelimit(IDevisionException):
  """An Exception when you are Ratelimited. This is a subclass of idevision.IDevisionException"""
  def __init__(self):
    super().__init__("You are currently ratelimited from IDevision API. You have recieved a 429 error code. Please follow the Ratelimit rules of IDevision from now on or you might get banned.")
  
class Banned(Ratelimit):
  """An Exception when you are Banned from the API. This is a subclass of idevision.Ratelimit."""
  def __init__(self):
    super().__init__("You are banned from IDevision API. You have recieved a 403 error code.")
  
class BadRequest(IDevisionException):
  """An Exception when the API has raised a Bad Request. This is a subclass of idevision.IDevisionException"""
  
class BadArgument(IDevisionException):
  """An Exception when there is a bad argument to a parameter. This is a subclass of idevision.IDevisionException"""
  def __init__(self, argument, expectedVal, inputVal):
    super().__init__(
      "A bad argument was raised in parameter %s. Expected value %u but got %s instead." % (argument, expectedVal, inputVal)
    )
  
class ServiceUnavailable(IDevisionException):
  """An Exception when the IDevison API returns a 503 Status Code."""
  def __init__(self):
    super().__init__("API Returned a 503 Status Code.")
    
class NotFound(IDevisionException):
    """An Exception when the IDevision API returns a 404 Status Code."""
    def __init__(self, url : str):
      super().__init__("URL %s Not Found. API Returned a 404 Status Code." % url)

errorCodes = {
  "503": ("Service Unavailable", ServiceUnavailable),
  "500": ("Internal Server Error", InternalServerError),
  "200": ("Ok.", None),
  "400": ("Bad Request.", BadRequest),
  "401": ("Bad Authorization/Unauthorized.", BadAuthorization),
  "404": ("Not found.", NotFound),
  "403": ("Banned.", Banned),
  "429": ("Ratelimited.", Ratelimit),
  "201": ("Ok.", None),
  "204": ("Ok.", None)
}
