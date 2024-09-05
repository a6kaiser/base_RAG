***RETRIEVAL AUGMENTED GENERATION***
by Alexandre Kaiser

Retrieval Augmented Generation (RAG) is a term that unifies all the efforts to (i) retrieve relevant passages from a database and (ii) generate relevant text from the retrieved information. The term originates from the paper https://arxiv.org/abs/2005.11401 which made use of pre-trained language models to retrieve and generate text from a query. Importantly in practice, the code attempts to stay agnostic to the language model, which allows for parallel work to be done on improving the language model.



**Retrieval**

**Augmented Generation**

**Real uses (by popularity)**
- improve upon semantic search within collections of proprietary information
-

**Practical Uses**
- Generate a wiki on a given text
    - input: body of text
    - retrieve: all semantic information
    - generate: a structured wiki
- Generate a conceptual taxonomy of a given text
    - input: body of text
    - retrieve: all semantic information
    - generate: conceptual taxonomy
- Take high concept command and identify the sequence of primitive tasks from set of instructions
    - input: command
    - retrieve: correct command recipe
- Identify sarcasm
    - input: text
    - retrieve: 
- Identify logical inconsistencies: this would be super important in the process of large developments because there may have been one team that made a particular decision due to one observation that a different team didnt know about when they tried to modify something else.



**Limitations and concerns**
The first clear limitation is the capability of the language model being used. However, since it's development is independent RAG we don't need to concern ourselves with it.

Data privacy: with many of the market uses cases relating to private information, there remain significant privacy concerns.

Chatbot
