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
  retrieved_at: datetime
  source_metadata: {}
  provenance_ref: optional-ref
```

Conceptual contract only. Replaces the former Sabueso Evidence concept.
