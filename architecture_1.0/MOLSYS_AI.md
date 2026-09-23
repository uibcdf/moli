# MolSys-AI — MolSysSuite Specialist Agent

MolSys-AI is the **specialist agent for MolSysSuite**. It is conceptually part of the MolSysSuite ecosystem and remains independent from MOLI Agent.

## Mission

MolSys-AI understands and operates MolSysSuite. Its specialized context may include documentation, API references, tutorials, examples, devguides, tool schemas, source/code context, and runtime information. A RAG system over these sources is a natural part of MolSys-AI.

## Roles

As a **software assistant**, MolSys-AI answers how-to questions about MolSysSuite components.

As a **specialist agent**, when authorized, it may plan and execute multi-step MolSysSuite operations, inspect outputs, recover from tool-level errors, and report results.

## Boundary with MOLI Agent

MolSys-AI specializes in **operating molecular-modeling software**. MOLI Agent specializes in **reasoning across the scientific investigation**.

MOLI may delegate modeling tasks to MolSys-AI, but MolSys-AI is not mandatory: MOLI, Praxis Protocols, DiscoveryEngine, or expert users may access MolSysSuite APIs directly.

MolSys-AI may report modeling outputs and observations, but project-level Evidence, Hypotheses, Strategies, and Decisions are represented and owned by Nextia. Human scientists and/or MOLI Agent may create, interpret, or propose them under the project's authority model.

> **MolSys-AI knows how to use MolSysSuite. MOLI reasons about why, when, and what for.**
