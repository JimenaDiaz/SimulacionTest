from redis import Redis
from os import getenv   

redis = Redis(
  host= 'us1-dynamic-urchin-37514.upstash.io',
  port= '37514',
  password= '50e04b3d55a24c62b566537e6abe4467', ssl=True)

