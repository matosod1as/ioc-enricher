# IOC Enricher

A ferramente enriquece IOCs, detecta de que tipo de dado se trata e volta com as informações da fonte.

## Por que criei

Quando aparece um IP suspeito num log, o analista precisa consultar várias fontes manualmente. Esta ferramenta faz isso de uma vez.

## Como usar
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
O veredito foi baseado em marcadores que regem como ip limpo algo que tem entre 0 e 24 denúncias, 

## Próximos passos
- [ ] Integração com VirusTotal (domínios e hashes)
- [ ] Relatório em Markdown