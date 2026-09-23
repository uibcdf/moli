# MOLI — Scientific Communication

## Purpose

MOLI should help scientists not only perform and coordinate scientific work, but also **understand the state of a problem before acting and communicate what was learned after acting**.

Scientific communication is therefore a cross-platform capability built from the scientific state already owned by Sabueso, Praxis, Nextia, MolSysSuite, and their components.

This document records a long-term direction. It is not a frozen API, renderer specification, or commitment to implement automated report/video generation in the current MVPs.

## Ownership

Scientific Communication belongs to **MOLI** because no individual component owns enough of the scientific state to construct the complete narrative.

Conceptually:

    Sabueso ------ knowledge, literature, SourceAssertions,
       |           conflicts, unknowns
    Praxis ------- methods, Capabilities, Protocols
       |
    Nextia ------- Questions, Hypotheses, Observations,
       |           Evidence, decisions, conclusions
    MolSysSuite -- models, computations, Results, Artifacts
       |
    MolSysViewer - molecular views, scenes, visual explanations
       |
       +--------------------+
                            v
                           MOLI
                            |
                            v
                 Scientific Communication

Components remain owners of their scientific objects. MOLI composes them into communication artifacts without transferring semantic ownership.

## Scientific artifact before presentation format

A report should not primarily be an LLM-generated block of prose.

MOLI should first construct a **structured, traceable scientific communication artifact**. Presentation formats are renderings of that artifact.

    Scientific Context
            +
    Modeling state / Results
            +
    Discovery state
            |
            v
    structured communication artifact
            |
       +----+----+---------+-------+
       v         v         v       v
      PDF       HTML     Slides   Video

This separation allows the same scientific state to be communicated through different media without creating independent, potentially contradictory narratives.

## ProjectBriefing — before substantial work

A **ProjectBriefing** helps scientists study a target, hypothesis, system, or scientific problem before deciding what to do.

For a target such as TcTIM it might include:

- biological and disease context;
- molecular identity and relevant homologs;
- structures and conformational information;
- known ligands and inhibitors;
- relevant interactions and functional annotations;
- comparison with human or other selectivity-relevant homologs;
- relevant literature and SourceAssertions;
- modeling assets already available;
- known methodological capabilities;
- established facts;
- conflicts and uncertainty;
- explicit knowledge gaps;
- candidate scientific questions or hypotheses already present in Nextia;
- recommended source material for human study.

A briefing should distinguish clearly among established external knowledge, reproducibly derived knowledge, project-specific interpretation, and open questions.

Its purpose is not to decide what the scientists should investigate. It is to make the starting scientific state intelligible.

## ProgressBrief — during a project

A **ProgressBrief** is a compact representation of what has changed during an active DiscoveryProject.

It may summarize:

- active Questions and Hypotheses;
- work completed since the previous brief;
- Protocols or modeling operations executed;
- important Results and Observations;
- Evidence created or changed;
- hypotheses strengthened, weakened, rejected, or still unresolved;
- failed or uninformative approaches;
- unexpected observations;
- new knowledge gaps;
- decisions requiring human attention;
- immediate next scientific questions.

For example:

    TcTIM campaign — progress brief

    Active hypotheses:        3
    Weakened hypotheses:      2
    New observations:         1
    Compounds evaluated:     47

    Emerging finding:
        pocket P7 warrants further investigation

    Major unresolved question:
        selectivity relative to HsTIM

The exact format is not prescribed. The important property is that the summary derives from traceable project state rather than from conversational memory alone.

## ProjectReport — after a project, experiment, or campaign

A **ProjectReport** communicates what was done and learned.

It may include:

- original scientific question;
- initial knowledge state;
- hypotheses;
- rationale;
- systems and models;
- Protocols and methodological choices;
- computations or experiments performed;
- Results;
- Observations;
- Evidence;
- negative or failed approaches;
- unexpected findings;
- decisions and their rationale;
- conclusions and their confidence/limitations;
- unresolved questions;
- new hypotheses;
- knowledge suitable for controlled promotion through the LEARN loop;
- recommended next work.

Negative and inconclusive results are part of the scientific record. A ProjectReport should not rewrite a project as a sequence of successes.

## Traceability

Every substantive scientific statement should, where possible, be traceable to the objects that justify it.

Depending on the statement, this may lead to:

    SourceAssertion
    external source / literature location

    Observation
    Evidence
    Result
    Artifact

    Protocol / Capability

    molecular system / model
    calculation

    decision / hypothesis

A reader should be able to ask:

> **Why does MOLI say this?**

and inspect the relevant scientific path.

Generated narrative must not erase epistemic distinctions such as:

    SourceAssertion != Evidence != Provenance
    Result != Observation != Evidence
    asserted knowledge != derived knowledge

## Visual scientific communication

MolSysViewer and other MolSysSuite components may provide figures, molecular scenes, trajectories, annotations, plots, or other visual Artifacts.

For example, a TcTIM ProjectBriefing might use:

- a TcTIM structural overview;
- the dimer interface highlighted;
- TcTIM/HsTIM structural comparison;
- known ligand binding sites;
- TopoMT features;
- relevant residues or mutations.

The communication layer should reference the underlying scientific objects and scene definitions where feasible so that visual explanations remain reproducible rather than becoming disconnected screenshots.

## Video as a rendering

Video is a future rendering of the same structured scientific communication artifact, not a separate scientific truth.

Conceptually:

    ProjectBriefing / ProjectReport
              |
              v
          storyboard
              |
        +-----+------+
        v            v
     narrative     scenes
                     |
              MolSysViewer / figures
        +------------+
        v
    narrated video

A future renderer might coordinate molecular animations, figures, captions, narration, and references.

The scientific content should remain inspectable independently of the video.

## Audience profiles

The same scientific state may need different communication depth and vocabulary.

Potential profiles include:

- **scientist** — detailed methods, evidence, uncertainty, provenance;
- **collaborator** — sufficient technical context for joint work;
- **executive** — objectives, major findings, uncertainty, implications, decisions;
- **public** — accessible explanation without exposing restricted information.

An audience profile changes presentation and selection, not the underlying scientific record.

A communication profile must not manufacture stronger conclusions for a less technical audience.

## Confidentiality and disclosure

Communication artifacts must respect MOLI visibility and disclosure boundaries.

A public or collaborator-facing rendering must not expose private DiscoveryProjects, proprietary Protocols, restricted molecular Candidates, unpublished Evidence, credentials, or other protected information merely because those objects were available to the context assembler.

Semantic ownership, visibility, and publication status remain distinct.

## Reproducibility and snapshots

A briefing or report may need to represent the scientific state at a particular time.

Where relevant, it should retain references to:

- project/state version;
- Card or knowledge snapshots;
- SourceAssertions and source retrieval context;
- Protocol versions;
- model/software versions;
- Result and Artifact identities;
- communication-generation time;
- rendering profile/version.

This allows later readers to distinguish:

> what was known and concluded then

from:

> what MOLI knows now.

## Relationship to the MOLI learning loop

Scientific communication naturally appears at several points in the loop:

    KNOW -> MODEL -> DO -> DISCOVER -> LEARN -> KNOW
      |                                  |
      +-- ProjectBriefing                +-- ProjectReport
                   |
             ProgressBrief
              during work

The ProjectBriefing makes the starting knowledge state understandable.

ProgressBriefs make scientific change visible while work is active.

The ProjectReport makes the resulting scientific history and learning understandable.

None of these artifacts performs the LEARN promotion automatically. Communication and promotion remain separate operations.

## Structured artifacts, not new epistemic primitives

ProjectBriefing, ProgressBrief, and ProjectReport are **communication artifacts**.

They compose and reference existing MOLI objects; they do not replace or redefine them.

A ProjectReport does not become Evidence.

A sentence in a ProjectBriefing does not become a SourceAssertion.

A video does not become the authoritative scientific record.

The authoritative objects remain in their owning components.

## Possible future communication object

A future structured representation might conceptually contain:

    ScientificCommunicationArtifact

    kind:
        project_briefing
        progress_brief
        project_report

    focus:
        project / target / hypothesis / experiment

    audience_profile

    scientific_sections

    referenced_objects:
        Cards
        Decks
        SourceAssertions
        Capabilities
        Protocols
        Hypotheses
        Results
        Observations
        Evidence
        Artifacts

    visual_assets / scenes

    provenance / snapshot

    disclosure policy

The exact schema and API are intentionally left open.

## Design principle

> **MOLI should be able to explain the scientific state before work begins, communicate how that state changes while work proceeds, and preserve a traceable account of what was learned when the work ends.**

The same structured scientific account should be capable of supporting written dossiers, interactive reports, presentations, and eventually narrated scientific videos without sacrificing provenance, uncertainty, or epistemic boundaries.
