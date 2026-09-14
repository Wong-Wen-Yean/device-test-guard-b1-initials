# Deliberately unsafe review sample. Never use a real credential.
API_TOKEN = "DEMO_TOKEN_DO_NOT_USE"

def authorization_header() -> dict[str, str]:
    return {"Authorization": f"Bearer {API_TOKEN}"}
