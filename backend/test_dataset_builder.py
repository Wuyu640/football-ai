from pprint import pprint

from backend.dataset.dataset_builder import DatasetBuilder

builder = DatasetBuilder()

sample = builder.build_match(

    "FC Barcelona",

    "Real Madrid CF",

    "home"

)

pprint(sample)