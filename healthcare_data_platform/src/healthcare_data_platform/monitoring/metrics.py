class MetricsCollector:

    def __init__(self):

        self.records_read = 0

        self.records_written = 0

    def collect(self):

        return {

            "records_read": self.records_read,

            "records_written": self.records_written

        }