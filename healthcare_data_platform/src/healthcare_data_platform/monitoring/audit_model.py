from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AuditRecord:

    pipeline_name: str
    dataset_name: str
    source_path: str
    target_table: str

    batch_id: str

    status: str
    
    records_read: Optional[int]
    records_written: Optional[int]

    started_at: datetime
    completed_at: datetime

    duration_seconds: float

    created_by: str
    created_at: datetime