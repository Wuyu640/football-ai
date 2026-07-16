from backend.dataset.dataset_builder import DatasetBuilder
from backend.export.csv_exporter import CSVExporter

builder = DatasetBuilder()
exporter = CSVExporter()

dataset = builder.build_season()

exporter.export(
    dataset,
    "backend/data/datasets/PD_2025.csv"
)

print()

print("Dataset exportado correctamente.")