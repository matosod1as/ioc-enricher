import ipaddress
import re

HEX = re.compile(r"^[0-9a-fA-F]+$")
DOMINIO = re.compile(r"^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$")

def detectar_tipo(valor):
    valor = valor.strip()

    try:
        ipaddress.ip_address(valor)
        return "ip"
    except ValueError:
        pass

    if valor.startswith(("http://", "https://")):
        return "url"

    if HEX.match(valor) and len(valor) in (32, 40, 64):
        return {32: "md5", 40: "sha1", 64: "sha256"}[len(valor)]

    if DOMINIO.match(valor):
        return "dominio"

    return "desconhecido"