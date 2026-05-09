import time


class RetryEngine:

    def __init__(self, max_retries=2, delay=1):
        self.max_retries = max_retries
        self.delay = delay

    def run_with_retry(self, func, *args, **kwargs):

        last_error = None

        for attempt in range(1, self.max_retries + 1):

            try:
                print(f"\n[RetryEngine] Attempt {attempt} running {func.__name__}")

                result = func(*args, **kwargs)

                print(f"[RetryEngine] Success on attempt {attempt}")

                return result

            except Exception as e:

                print(f"[RetryEngine] Error on attempt {attempt}: {e}")

                last_error = e

                time.sleep(self.delay)

        # If all retries fail
        return {
            "status": "failed",
            "error": str(last_error),
            "message": "All retry attempts failed"
        }