import os
import requests

BASE = "https://www.virustotal.com/api/v3"

CAMINHOS = {
    "ip": "ip_addresses",
    "dominio": "domains",
    "md5": "files",
    "sha1": "files",
    "sha256": "files",
}


def consultar_vt(valor, tipo):
    chave = os.getenv("VIRUSTOTAL_KEY")
    if not chave:
        raise RuntimeError("Defina VIRUSTOTAL_KEY no arquivo .env")

    if tipo not in CAMINHOS:
        return None

    url = f"{BASE}/{CAMINHOS[tipo]}/{valor}"

    resposta = requests.get(url, headers={"x-apikey": chave}, timeout=15)

    if resposta.status_code == 404:
        return {"fonte": "VirusTotal", "veredito": "desconhecido"}

    resposta.raise_for_status()

    atributos = resposta.json()["data"]["attributes"]
    votos = atributos["last_analysis_stats"]
    total = sum(votos.values())

    return {
        "fonte": "VirusTotal",
        "maliciosos": votos["malicious"],
        "suspeitos": votos["suspicious"],
        "total": total,
        "reputacao": atributos.get("reputation"),
        "veredito": classificar_vt(votos["malicious"], votos["suspicious"], total),
    }


def classificar_vt(maliciosos, suspeitos, total):
    if total == 0:
        return "desconhecido"

    if maliciosos >= total * 0.1:
        return "malicioso"
    elif maliciosos >= total * 0.03 or suspeitos >= total * 0.03:
        return "suspeito"
    else:
        return "limpo"
