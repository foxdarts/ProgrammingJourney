import requests
import pandas as pd
import openpyxl
import asyncio
import aiohttp

async def fetch_card_sets(session, card_name):
    """Fetches set information for a given card from Scryfall API asynchronously."""
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    async with session.get(url) as response:
        data = await response.json()

        if 'card' in data:
            card_sets = [set['set_name'] for set in data['card']['set_details']]
            return card_name, card_sets
        else:
            return card_name, []

async def main(filename):
    """Asynchronously fetches set information for cards from a file and creates an Excel sheet."""
    with open(filename, 'r') as f:
        card_list = [line.strip() for line in f]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for card in card_list:
            tasks.append(asyncio.create_task(fetch_card_sets(session, card)))

        results = await asyncio.gather(*tasks)

    # Create a DataFrame with card names as index and sets as values
    df = pd.DataFrame(results, columns=['Card Name', 'Sets'])
    df = df.set_index('Card Name')
    df = df.explode('Sets')
    df = df.pivot_table(index='Sets', columns='Card Name', aggfunc='size', fill_value=0)

    # Write the DataFrame to an Excel file
    df.to_excel('mtg_sets_pivot.xlsx')

# Example usage:
filename = 'price_list.txt'  # Replace with your file name
asyncio.run(main(filename))