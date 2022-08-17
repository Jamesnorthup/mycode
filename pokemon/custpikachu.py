#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse
import pandas as pd
import requests
items=requests.get("http://pokeapi.co/api/v2/item/?limit=1000").json()

df= pd.DataFrame(items)
print(df.tail())





