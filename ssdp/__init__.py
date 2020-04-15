"""Python library for Simple Service Discovery Protocol (SSDP)."""

import ssdp.entity as entity
import ssdp.network as network
import ssdp.asyncio as asyncio

from ssdp.entity import *
from ssdp.asyncio import *

__all__ = entity.__all__ + asyncio.__all__
