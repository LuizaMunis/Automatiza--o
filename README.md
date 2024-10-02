# Automatização de Geração de PDFs - Ministério de Minas e Energia

Bem-vindo ao repositório de automatização de geração de PDFs! Este projeto utiliza a biblioteca FPDF para criar documentos PDF personalizados contendo links para redirecionar do o portal do MME para o site do Diário Oficial da União..

## Descrição do Projeto

Este projeto gera 30 documentos PDF, cada um contendo uma imagem e um link que direciona para uma página do governo. A automatização é útil para facilitar a criação de documentos oficiais e informativos.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FPDF**: Biblioteca para geração de arquivos PDF.

## Como Funciona

O código cria uma nova instância do PDF para cada iteração, adiciona uma imagem, um texto e um link específico. O link é gerado dinamicamente com base na data, resultando em 30 PDFs, um para cada dia do mês de setembro de 2018.
