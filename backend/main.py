from fastapi import FastAPI

app = FastAPI(title="ScamShield AI")

SCAM_WORDS = ["won", "lottery", "urgent", "otp", "click here",
              "verify", "blocked", "prize", "kyc", "free gift"]
BAD_URL_HINTS = ["bit.ly", "tinyurl", ".xyz", ".top", "login-", "-verify"]

@app.get("/")
def home():
    return {"status": "ScamShield running"}

@app.post("/check-text")
def check_text(message: str):
    hits = [w for w in SCAM_WORDS if w in message.lower()]
    score = min(100, len(hits) * 25)
    return {"verdict": "Scam" if score >= 50 else "Safe",
            "risk_score": score, "triggers": hits}

@app.post("/check-url")
def check_url(url: str):
    hits = [h for h in BAD_URL_HINTS if h in url.lower()]
    if not url.startswith("https"):
        hits.append("no https")
    score = min(100, len(hits) * 35)
    return {"verdict": "Suspicious" if score >= 35 else "Looks OK",
            "risk_score": score, "triggers": hits}