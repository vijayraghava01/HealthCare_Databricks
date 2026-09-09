from pyspark import pipelines as dp


@dp.temporary_view
def patient_cdc_source():

    return (
        spark.readStream  # type: ignore
        .table("workspace.dev.patient_cdc_source")
    )


dp.create_streaming_table(
    "patients_cdc_scd1"
)

dp.create_streaming_table(
    "patients_cdc_scd2"
)


dp.create_auto_cdc_flow(
    target="patients_cdc_scd1",
    source="patient_cdc_source",
    keys=["Patient_ID"],
    sequence_by="Event_Time",
    apply_as_deletes="Operation = 'DELETE'",
    except_column_list=[
        "CDC_Event_ID",
        "Operation"
    ],
    stored_as_scd_type=1
)


dp.create_auto_cdc_flow(
    target="patients_cdc_scd2",
    source="patient_cdc_source",
    keys=["Patient_ID"],
    sequence_by="Event_Time",
    ignore_null_updates=True,
    apply_as_deletes="Operation = 'DELETE'",
    except_column_list=[
        "CDC_Event_ID",
        "Operation"
    ],
    stored_as_scd_type=2
)
