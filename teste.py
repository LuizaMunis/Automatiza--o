import requests
from bs4 import BeautifulSoup

url = 'https://www.gov.br/mme/pt-br/arquivos?b_start=1&b_size=31000'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    pdf_links = [link['href'] for link in links if link['href'].endswith('s1.pdf/view') or link['href'].endswith('s2.pdf/view')]

    if pdf_links:
        for pdf_link in pdf_links:
            print(pdf_link)
    else:
        print("Nenhum arquivo PDF encontrado.")
else:
    print(f"Falha na requisição: {response.status_code}")
