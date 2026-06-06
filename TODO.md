# TODO

- [ ] Pin dependency versions to fix Groq/httpx incompatibility (TypeError: unexpected keyword argument 'proxies').
- [ ] Update requirements.txt with compatible `httpx`/`httpcore` versions for groq==0.9.0.
- [ ] Reinstall dependencies in venv2 (`pip install -r requirements.txt`).
- [ ] Run app and verify Groq client initializes without error.
- [ ] Smoke test `/summarize` with a sample document.

