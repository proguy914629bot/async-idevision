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
  
class ServiceUnavailable(IDevisionException):
  """An Exception when the IDevison API returns a 503 Status Code."""
  def __init__(self):
    return super().__init__("API Returned a 503 Status Code.")
    
class NotFound(IDevisionException):
    """An Exception when the IDevision API returns a 404 Status Code."""
    def __init__(self):
      return super().__init__("API Returned a 404 Status Code.")
