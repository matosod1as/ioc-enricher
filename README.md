# IOC Enricher
IOC (Indicador de Comprometimento) é um rastro deixado por um ataque, como o IP de origem, um domínio de phishing ou o hash de um arquivo malicioso.

Ferramenta de linha de comando em Python que recebe um IOC (IP, domínio ou hash), identifica o tipo automaticamente, consulta fontes de threat intelligence e devolve um veredito: limpo, suspeito ou malicioso.

## Por que criei

Quando aparece um IP suspeito num log, o analista precisa consultar várias fontes manualmente. Esta ferramenta faz isso de uma vez.

## Como usar
Crie uma conta gratuita na AbuseIPDB e gere sua chave de API no painel da conta.

​```bash
pip install -r requirements.txt
# crie um arquivo .env com: ABUSEIPDB_KEY=sua_chave
python main.py 8.8.8.8
​```

## Exemplo de saída
​```
IOC: 8.8.8.8 | tipo: ip
{'fonte': 'AbuseIPDB', 'score': 0, 'denuncias': 197, 'pais': 'US', 'provedor': 'Google LLC', 'tor': False, 'tipo_uso': 'Content Delivery Network', 'ultima_denuncia': '2026-11-17T00:00:48+00:00', 'veredito': 'limpo'}
​```

## Como o veredito é decidido
O veredito usa o score de confiança de abuso da AbuseIPDB (0 a 100), e não o
número bruto de denúncias — denúncias podem ser falsas (o 8.8.8.8 acima tem quase
200 e é legítimo), enquanto o score já pondera a confiabilidade de quem denunciou.

| Score  | Veredito  | Motivo                                              |
|--------|-----------|-----------------------------------------------------|
| 75–100 | malicioso | alta confiança de abuso                             |
| 25–74  | suspeito  | sinais relevantes, mas pode ser falso positivo      |
| 0–24   | limpo     | sem evidência suficiente de abuso                   |

## Próximos passos
- [ ] Integração com VirusTotal (domínios e hashes)
- [ ] Relatório em Markdown
