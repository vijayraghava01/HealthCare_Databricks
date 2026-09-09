from healthcare_data_platform.config.tables import (
    PIPELINE_AUDIT_TABLE
)


class AuditRepository:

    def __init__(self, spark):

        self.spark = spark
        
    def write(self, audit_record):

        data = [

            (
                audit_record.pipeline_name,
                audit_record.dataset_name,
                audit_record.source_path,
                audit_record.target_table,

                audit_record.batch_id,

                audit_record.status,

                audit_record.records_read,
                audit_record.records_written,

                audit_record.started_at,
                audit_record.completed_at,

                audit_record.duration_seconds,

                audit_record.created_by,
                audit_record.created_at,
            )

        ]

        columns = [

            "pipeline_name",
            "dataset_name",
            "source_path",
            "target_table",

            "batch_id",

            "status",

            "records_read",
            "records_written",

            "started_at",
            "completed_at",

            "duration_seconds",

            "created_by",
            "created_at"
        ]

        (
            self.spark
            .createDataFrame(data, columns)
            .write
            .mode("append")
            .format("delta")
            .saveAsTable(PIPELINE_AUDIT_TABLE)
        )