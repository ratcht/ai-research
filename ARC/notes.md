- Start off by getting a model to interpret the environment. Pick up patterns explicitly.

Three Stage Pipeline:

Ideal solution should: create a DSL library on-the-fly:

- Create operations that it can perform based on the task at hand. Use previously created operations.
- DreamCoder
- Look into program synthesis

- LLMs (o1-preview) can reason relatively well on text-based patterns. Maybe change the way the patterns are formatted, look into better prompting, and FSL.

1. Pre-process the grid into a manner that encodes as much information as possible
2. Extract Pattern (Potentially by using LLMs)
3. Apply