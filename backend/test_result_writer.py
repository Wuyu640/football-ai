from backend.evaluation.result_writer import ResultWriter

writer = ResultWriter()

path = writer.save(

    "test",

    {

        "accuracy": 0.72,

        "matches": 380

    }

)

print(path)