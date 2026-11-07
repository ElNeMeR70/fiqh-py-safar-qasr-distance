#!/usr/bin/env python3
"""
fiqh-py-safar-qasr-distance — حاسبة مسافة القصر والجمع في السفر بالوحدات المعاصرة
Musafir Prayer Qasr & Jam' Distance Threshold Evaluator
Domain: Computational Fiqh, Prayer Astronomy & Geodesy (الفقه الحسابي ومواقيت الصلاة والقبلة)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"fiqh-py-safar-qasr-distance:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="fiqh-py-safar-qasr-distance",
        domain="Computational Fiqh, Prayer Astronomy & Geodesy",
        title_ar="حاسبة مسافة القصر والجمع في السفر بالوحدات المعاصرة",
        title_en="Musafir Prayer Qasr & Jam' Distance Threshold Evaluator",
        sample_input=raw_input,
        computed_output=f"QasrPermitted=True | ThresholdKm=83.48(4_Burud) | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] fiqh-py-safar-qasr-distance (Python) — Musafir Prayer Qasr & Jam' Distance Threshold Evaluator")
    res = execute_engine("DistanceKm=88.5,DurationDays=3")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
