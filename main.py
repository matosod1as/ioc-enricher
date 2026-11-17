import sys
from dotenv import load_dotenv
from detect import detectar_tipo
from abuseipdb import consultar_ip

load_dotenv()

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <ioc>")
        return

    ioc = sys.argv[1]
    tipo = detectar_tipo(ioc)
    print(f"IOC: {ioc} | tipo: {tipo}")

    if tipo == "ip":
        resultado = consultar_ip(ioc)
        print(resultado)
    else:
        print("Por enquanto só sei consultar IPs.")

if __name__ == "__main__":
    main()