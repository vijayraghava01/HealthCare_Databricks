class HealthcareDataPlatformException(Exception):
    """Base exception for the healthcare data platform."""


class BronzePipelineException(
    HealthcareDataPlatformException
):
    """Bronze ingestion failure."""


class ValidationException(
    HealthcareDataPlatformException
):
    """Data validation failure."""


class MetadataException(
    HealthcareDataPlatformException
):
    """Metadata processing failure."""


class WriterException(
    HealthcareDataPlatformException
):
    """Bronze writer failure."""


class AuditException(
    HealthcareDataPlatformException
):
    """Audit framework failure."""