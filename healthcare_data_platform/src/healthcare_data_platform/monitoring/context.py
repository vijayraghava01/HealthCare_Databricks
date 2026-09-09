from dataclasses import dataclass
from datetime import datetime, timezone
import uuid


@dataclass
class PipelineContext:

    pipeline_name: str
    dataset_name: str
    source_path: str
    target_table: str
    batch_id: str
    started_at: datetime
    created_by: str

    @classmethod
    def create(
        cls,
        pipeline_name: str,
        dataset_name: str,
        source_path: str,
        target_table: str,
        created_by: str
    ):

        return cls(
            pipeline_name=pipeline_name,
            dataset_name=dataset_name,
            source_path=source_path,
            target_table=target_table,
            batch_id=str(uuid.uuid4()),
            started_at=datetime.now(timezone.utc),
            created_by=created_by
        )