# Operational Analysis

## Model Calls

For each claim:

1 GPT Vision call

1 Groq claim parser call

1 Groq consensus call

Total:

3 model calls per claim

---

## Token Usage

Average input tokens:

1200

Average output tokens:

200

---

## Image Processing

1-3 images per claim

All images processed locally before model calls.

---

## Estimated Cost

Assumptions:

GPT-4.1-mini Vision

Groq Llama 3.3 70B

Approximate cost:

$0.001 per claim

---

## Runtime

Average:

5 seconds per claim

100 claims:

≈8 minutes sequential

≈2 minutes batched

---

## Rate Limits

Retries implemented using tenacity.

Caching prevents duplicate requests.

Parallel execution through LangGraph reduces latency.

---

## Strategies

Batching

Caching

Exponential backoff

JSON validation

Structured outputs using Pydantic

Conservative decision logic

Images treated as primary evidence.