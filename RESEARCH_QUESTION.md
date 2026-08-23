# Primary Research Question

Can principles derived from historical and modern attempts at universal representation support a useful model-independent semantic intermediate representation between human intent and AI computation?

## Operational Questions

1. What mechanisms recur across important historical systems of representation?
2. Which of those mechanisms have modern technical analogues?
3. What existing work already occupies this research space?
4. Can human intent be transformed into a more compact structured representation without material semantic loss?
5. Can such a representation improve token use, cost, latency, consistency, reasoning, or interoperability?
6. Can the same underlying representation work across multiple model families?
7. Does the representation generalize across substantially different task classes?
8. Does translation into and out of the representation introduce more cost or error than it saves?
9. Where does natural language outperform structured semantic representations?
10. Is there enough evidence after CE-01 to justify a larger research program?

## Working Architecture

Human Intent
    ↓
Natural Language
    ↓
Semantic Intermediate Representation
    ↓
Model / Tool Adapter
    ↓
LLM, Agent, Database, Simulator, or Program

## Central Falsifiable Hypothesis

For at least some broad classes of AI tasks, a model-independent semantic representation can communicate equivalent task intent more efficiently and/or reliably than conventional natural-language prompting after accounting for representation-conversion overhead.

## Null Hypothesis

After accounting for conversion, decoding, schema overhead, model adaptation, and performance loss, semantic intermediate representations provide no meaningful general advantage over strong natural-language prompting.
