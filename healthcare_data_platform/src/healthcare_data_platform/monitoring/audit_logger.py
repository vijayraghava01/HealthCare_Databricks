from datetime import datetime, timezone
import uuid

from healthcare_data_platform.monitoring.audit_model import AuditRecord
from healthcare_data_platform.monitoring.audit_repository import AuditRepository


class AuditLogger:

    def __init__(
        self,
        pipeline_name,
        dataset_name,
        source_path,
        target_table,
        repository
    ):

        self.pipeline_name = pipeline_name
        self.dataset_name = dataset_name
        self.source_path = source_path
        self.target_table = target_table

        self.batch_id = str(uuid.uuid4())

        self.started_at = datetime.now(timezone.utc)

        self.repository = repository

    def success(
        self,
        records_read=0,
        records_written=0
    ):

        completed = datetime.now(timezone.utc)

        record = AuditRecord(

            pipeline_name=self.pipeline_name,

            dataset_name=self.dataset_name,

            source_path=self.source_path,

            target_table=self.target_table,

            batch_id=self.batch_id,

            status="SUCCESS",

            records_read=records_read,

            records_written=records_written,

            started_at=self.started_at,

            completed_at=completed,

            duration_seconds=(
                completed - self.started_at
            ).total_seconds(),

            created_by="databricks",

            created_at=completed
        )

        self.repository.save(record)

    def failure(
        self,
        records_read=0,
        records_written=0
    ):

        completed = datetime.now(timezone.utc)

        record = AuditRecord(

            pipeline_name=self.pipeline_name,

            dataset_name=self.dataset_name,

            source_path=self.source_path,

            target_table=self.target_table,

            batch_id=self.batch_id,

            status="FAILED",

            records_read=records_read,

            records_written=records_written,

            started_at=self.started_at,

            completed_at=completed,

            duration_seconds=(
                completed - self.started_at
            ).total_seconds(),

            created_by="databricks",

            created_at=completed
        )

        self.repository.save(record)