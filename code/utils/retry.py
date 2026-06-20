# utils/retry.py

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential


retry_llm = retry(

    stop=stop_after_attempt(3),

    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10
    ),

    reraise=True
)