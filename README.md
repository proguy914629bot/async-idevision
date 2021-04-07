# async-idevision
An Async Wrapper written in python for the IDevision API.

## How to Install:
```sh
pip install git+https://github.com/proguy914629bot/async-idevision/
```

## Guide:
```py
from idevision import IDevision

idevision = IDevision(token="<Token Goes Here>") #Token is not needed. But an error would be raised when you are trying to access an endpoint that requires a token.

#Example for RTFM:
rtfm = await idevision.rtfm(query="Bot", uri="https://discordpy.readthedocs.io/en/latest", ...)
rtfm.nodes # {"Node Name": "URL of the documentation", ...}
rtfm.status # 200
rtfm.query_time # "1.0"

#Example for RTFS:
rtfs = await idevision.rtfs(query="Bot", library="discord.py", ...)
rtfs.nodes # {"Node Name": "URL/Source"},
rtfs.status # 200
rtfs.query_time # "1.0"
```

## For more info, Please read the Documentation.
------------------------------------------------------------------------------------------------------------------------------------------
| IDevision                                | async-idevision                                                                             |
------------------------------------------------------------------------------------------------------------------------------------------
| [Click Here](https://idevision.net/docs) | [Click Here](https://github.com/proguy914629bot/async-idevision/blob/main/DOCUMENTATION.md) |
------------------------------------------------------------------------------------------------------------------------------------------
