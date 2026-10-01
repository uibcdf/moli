# Sabueso SourceAssertion conceptual schema

```yaml
source_assertion:
  id: stable-id
  subject_ref: stable-ref
  field_path: string
  asserted_value: any
  normalized_value: any
  source:
    type: database|literature|patent|curated|other
    name: string
    record_id: string
    version: optional
  acquisition:
    method: database|curation|rule_extraction|model_extraction
    tool: optional
    version: optional
    configuration: optional
    origin: optional
    validated_by: optional
  retrieved_at: datetime
  source_metadata: {}
  provenance_ref: optional-ref
```

Conceptual contract only. Replaces the former Sabueso Evidence concept.

`source` identifies where the statement comes from; `acquisition.method` records
how Sabueso or its user obtained that statement. A database record whose provider
says it was text-mined remains `method: database`; `origin` may record the
provider's stated route, such as `text_mining`. Do not infer the provider's
upstream method from the way Sabueso retrieved the record.

New SourceAssertions record `acquisition`. For `rule_extraction` and
`model_extraction`, `tool` and `version` identify the extraction process;
`configuration` records available settings. `validated_by` records a human
confirmation of an extraction when one occurred; it does not replace the
extraction method. Extraction must capture a statement present in a source,
not a model-generated interpretation presented as if the source stated it.

For historical assertions without `acquisition`, readers report
`not_recorded` rather than guessing `database`, `curation`, or another route.
The legacy `source.type: curated` likewise does not prove an acquisition
method. Acquisition provenance describes entry into Sabueso; it does not
grade truth or turn a SourceAssertion into Nextia Evidence. Sabueso owns the
concrete schema and migration of stored Cards.
