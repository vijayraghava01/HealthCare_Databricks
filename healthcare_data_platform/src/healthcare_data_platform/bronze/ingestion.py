from healthcare_data_platform.monitoring.context import (
    PipelineContext,
)

from healthcare_data_platform.monitoring.application_logger import (
    logger,
)

from healthcare_data_platform.monitoring.audit_repository import (
    AuditRepository,
)

from healthcare_data_platform.monitoring.audit_logger import (
    AuditLogger,
)

from healthcare_data_platform.monitoring.metrics import (
    MetricsCollector,
)

from healthcare_data_platform.bronze.reader import (
    BronzeReader,
)

from healthcare_data_platform.bronze.metadata import (
    MetadataManager,
)

from healthcare_data_platform.bronze.validation import (
    ValidationManager,
)

from healthcare_data_platform.bronze.writer import (
    BronzeWriter,
)


class BronzeIngestion:

    def __init__(
        self,
        spark,
        config,
        created_by,
    ):

        self.spark = spark
        self.config = config
        self.created_by = created_by

    def run(self):

        context = PipelineContext.create(

            pipeline_name="bronze_ingestion",

            dataset_name=self.config["dataset_name"],

            source_path=self.config["source_path"],

            target_table=self.config["target_table"],

            created_by=self.created_by,
        )

        repository = AuditRepository(
            self.spark
        )

        audit = AuditLogger(
            context,
            repository,
        )

        metrics = MetricsCollector()

        try:

            logger.info(
                f"Starting ingestion: "
                f"{context.dataset_name}"
            )

            # =====================================
            # 1. READ
            # =====================================

            df = BronzeReader.read_stream(
                self.spark,
                self.config,
            )

            logger.info(
                f"Reader initialized: "
                f"{context.dataset_name}"
            )

            # =====================================
            # 2. METADATA
            # =====================================

            df = MetadataManager.add_metadata(
                df
            )

            # =====================================
            # 3. VALIDATION
            # =====================================

            ValidationManager.validate(
                df,
                self.config,
            )

            logger.info(
                f"Validation completed: "
                f"{context.dataset_name}"
            )

            # =====================================
            # 4. WRITE
            # =====================================

            query = BronzeWriter.write_stream(
                df,
                self.config,
            )

            logger.info(
                f"Streaming query started: "
                f"{context.dataset_name}"
            )

            # IMPORTANT:
            #
            # This is a streaming query.
            # We do NOT call df.count().
            #
            # We also do NOT mark the audit
            # as SUCCESS here because the query
            # has only been started.
            #
            # The execution-level audit will be
            # handled at the correct pipeline/job
            # boundary.

            return query

        except Exception:

            logger.exception(
                f"Pipeline failed: "
                f"{context.dataset_name}"
            )

            audit.complete(
                status="FAILED",
                records_read=metrics.records_read,
                records_written=metrics.records_written,
            )

            raise