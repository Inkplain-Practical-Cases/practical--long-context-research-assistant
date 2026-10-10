# Long-Context Research Assistant

Junior FDE educational implementation with six cumulative STEP branches for a bounded multi-document research pipeline. Uses offline lexical passage retrieval, per-user/session in-process history, context budgeting and source-cited extractive answers.

## Branches
- STEP 1: [Research intake](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-01-research-intake)
- STEP 2: [Bounded context window and token budgeting](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-02-bounded-context-window-and-token-budgeti)
- STEP 3: [Retrieve evidence with stable citations](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-03-retrieve-evidence-with-stable-citations)
- STEP 4: [Store scoped multi-turn research history](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-04-store-scoped-multi-turn-research-history)
- STEP 5: [Generate extractive cited research answers](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-05-generate-extractive-cited-research-answe)
- STEP 6: [Orchestrate bounded multi-document research](https://github.com/Inkplain-Practical-Cases/practical--long-context-research-assistant/tree/step-06-orchestrate-bounded-multi-document-resea)

Install via `python -m pip install -r requirements.txt`, test via `python -m pytest -q`. It is **not** a production long-context LLM or distributed session store; token budgeting uses word counts as a pedagogical estimate, not an actual tokenizer. Do not use real research secrets without access controls. The seven-branch GitHub Actions matrix verifies tests independently.
