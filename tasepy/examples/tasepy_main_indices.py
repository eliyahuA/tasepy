"""
Get 3 main indeces of Tel Aviv stock exhange
"""
from tasepy import quick_client
from dotenv import load_dotenv
from os.path import realpath, dirname, exists
from sys import argv
from json import loads, load
from typing import Tuple
from pydantic import RootModel
from rich import print as rprint
from loguru import logger

class DataTuple(RootModel[Tuple[float, float, str]]):
    """
    A Pydantic model for a tuple containing two floats.
    The root value is accessed via the `root` attribute.
    """
    pass

def get_index_last_rate(client: quick_client, index_id: int) -> DataTuple:
    last_rate=loads(client.indices_online.get_last_rate(index_id).model_dump_json())
    raw_data = (last_rate["getIndexTradingDataIntraDay"]["lastIndexRate"], last_rate["getIndexTradingDataIntraDay"]["change"], last_rate["getIndexTradingDataIntraDay"]["lastSaleTime"])
    return DataTuple.model_validate(raw_data)

def main(json_dir: str = ".") -> int:
    env_file= dirname(realpath(argv[0])) + "/.env"
    if exists(env_file):
        load_dotenv(env_file)
    client = quick_client()
    indices=client.indices_basic.get_indices_list()
    indices_json=loads(indices.model_dump_json())
    
    # Main indices
    selected_indices_json = json_dir + "/selected_indices.json"
    if not exists(selected_indices_json):
       selected_indices_json  = dirname(realpath(argv[0])) + "/../tasepy/examples/selected_indices.json"
    with open(selected_indices_json) as input_json:
        selected_indices = load(input_json)
    # Build reverse mapping for O(1) lookup
    name_to_key = {name: int(key) for key, name in selected_indices.items()}
    # Initialize with None for clearer error handling
    selected_id = [None, None, None]
    # Build index table and find selected ids 
    index_table=dict()
    for idx in indices_json["indicesList"]["result"]:
        index_name = idx["indexName"]
        # Fill index_table and assign selected ids
        if index_name in name_to_key:
            index_id = idx["indexId"]
            index_table[index_id] = index_name
            selected_id[name_to_key[index_name]] = index_id
    
    rprint(f"[bold]{'שם'}      {'אחרון'}     {'שינוי'}  {'זמן המכירה האחרונה'}")
    for idx in (selected_id):
        if idx:
            try:
                last_rate, change, last_trade = get_index_last_rate(client, idx).root
                change_string = f"{change:.2f} " if change >=0 else f"{-change:.2f}-"
                change_pretty = "[green]" + change_string + "[/green]" if change >= 0 else "[red]" + change_string + "[/red]"
                rprint(f"     {index_table[idx]}   {last_rate:.2f}    {change_pretty}       [magenta]{last_trade}[/magenta]")
            except Exception as e:
                logger.error(f"Online indices are not available now. Please, try again later")
                return 1
    return 0
if __name__ == "__main__":
    print(main(json_dir=dirname(realpath(argv[0]))))

