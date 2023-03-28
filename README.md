# Pokemon.py

Pokemon.py is an API wrapper for PokéAPI written in Python.

## Sample

```python
from api import Client
import asyncio

async def main():
    async with Client() as client:
        berry = await client.get_berry(1)
        berry_firmness = await berry.firmness.fetch()

    print(berry) # <Berry>: {'id': ..., }
    print(berry_firmness) # <BerryFirmness>: {'id': ...}


asyncio.run(main())
```

You can also use this function as follows

```python
async def main():
   client = Client()

   berry = await client.get_berry(1)
   berry_firmness = await berry.firmness.fetch()

   await client.close()
```

If you want to get the original resources, try the following:
```python
# in main
async with Client() as client:
    """all resource-classes have `to_dict()` method"""
   berry = (await client.get_berry(1)).to_dict()

print(berry) # {'name': 'cheri', 'id': 1, ...}
```
