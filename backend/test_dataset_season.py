from backend.dataset.dataset_builder import DatasetBuilder

builder = DatasetBuilder()

dataset = builder.build_season()

print()

print("PARTIDOS:", len(dataset))

print()

print(dataset[0])