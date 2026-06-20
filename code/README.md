# Multi-Modal Damage Claim Review

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
```

---

## Dataset Structure

```
dataset/

claims.csv

sample_claims.csv

user_history.csv

evidence_requirements.csv

images/
    sample/
    test/
```

---

## Run

```bash
python main.py
```

---

## Output

Results are saved to:

```
outputs/output.csv
```

---

## Evaluation

```bash
python evaluation/evaluate.py
```

---

## Models Used

### Claim Parser

Groq Llama 3.3 70B

---

### Image Analysis

GPT-4.1-mini Vision

---

### Consensus Agent

Groq Llama 3.3 70B

---

## Workflow

```
Claim Parser
↓
Image Analyzer
↓
Evidence Agent
↓
History Agent
↓
Consensus Agent
↓
Formatter Agent
↓
output.csv
```

---

## Design Principles

- Images are primary evidence.
- User history contributes risk only.
- Structured outputs with Pydantic.
- LangGraph orchestration.
- Retry logic.
- Logging.
- Evaluation support.