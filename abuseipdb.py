import os
import requests

URL = "https://api.abuseipdb.com/api/v2/check"


def consultar_ip(ip):
    chave = os.getenv("ABUSEIPDB_KEY")
    if not chave:
        raise RuntimeError("Defina ABUSEIPDB_KEY no arquivo .env")

    resposta = requests.get(
        URL,
        headers={"Key": chave, "Accept": "application/json"},
        params={"ipAddress": ip, "maxAgeInDays": 90},
        timeout=10,
    )
    resposta.raise_for_status()

    dados = resposta.json()["data"]

    return {
        "fonte": "AbuseIPDB",
        "score": dados["abuseConfidenceScore"],
        "denuncias": dados["totalReports"],
        "pais": dados.get("countryCode"),
        "provedor": dados.get("isp"),
        "tor": dados.get("isTor", False),
        "tipo_uso": dados.get("usageType"),
        "ultima_denuncia": dados.get("lastReportedAt"),
        "veredito": classificar(dados["abuseConfidenceScore"]),
    }


# Limites baseados no score da AbuseIPDB (0–100).
# 75+: a própria plataforma trata como alta confiança de abuso.
# 25+: denúncias relevantes, mas que podem ser falso positivo — vale revisar.
def classificar(score):
    if score >= 75:
        return "malicioso"
    elif score >= 25:
        return "suspeito"
    else:
        return "limpo"
