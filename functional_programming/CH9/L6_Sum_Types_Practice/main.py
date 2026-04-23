from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return prepare(data)
        case CSVExportStatus.PROCESSING:
            return process(data)
        case CSVExportStatus.SUCCESS:
            return handle_success(data)
        case CSVExportStatus.FAILURE:
            return handle_failure(data)
        case _:
            raise Exception("unknown export status")


def prepare(data):
    processed_data = list(map(lambda lst: list(map(lambda s: str(s), lst)), data))
    return "Pending...", processed_data


def process(prepared_data):
    processed_data = "\n".join(map(lambda lst: ",".join(lst), prepared_data))
    return "Processing...", processed_data


def handle_success(processed_data):
    return "Success!", processed_data


def handle_failure(data):
    _, processed_data = process(prepare(data)[1])
    return "Unknown error, retrying...", processed_data

