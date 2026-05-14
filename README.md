# 📊 Sistema de Gerenciamento de Cadastros

Este é um sistema CRUD de gerenciamento de cadastros robusto baseado em terminal, desenvolvido em Python. O projeto foi estruturado seguindo boas práticas de desenvolvimento, utilizando conceitos de modularização clean, persistência de dados em banco de dados relacional (SQLite) e automação de relatórios.

> 🚀 **Nota de evolução:** Este projeto representa um marco importante na minha jornada como desenvolvedor, consolidando meus conhecimentos em arquitetura de software, manipulação de banco de dados, tratamento de exceções e empacotamento de software nativo.

---

## 🛠️ Funcionalidades

O sistema conta com um menu interativo e dinâmico, com limpeza automática de tela a cada ação e validação estrita de dados:

1. **Listar Cadastros:** Consulta e exibe em formato legível todos os registros salvos.
2. **Pesquisar Cadastro:** Filtra e localiza registros específicos na base de dados.
3. **Novo Cadastro:** Adiciona novos registros com validação de tipo de dado na entrada.
4. **Atualizar Cadastro:** Permite editar informações de cadastros já existentes.
5. **Deletar Cadastro:** Remove de forma definitiva registros selecionados.
6. **Exportar para Excel:** Gera automaticamente um relatório estruturado em planilha `.xlsx`.
7. **Encerrar Programa:** Finaliza a aplicação de forma segura e limpa.

---

💻 Tecnologias e Conceitos Aplicados
Python 3: Linguagem base para toda a arquitetura de software.

- SQLite3: Banco de dados relacional leve para persistência real e segura dos dados.
  
- Limpeza Dinâmica de Terminal: Uso da biblioteca nativa os para alternar comandos de limpeza automática (cls/clear) dependendo do sistema operacional do usuário.

- Tratamento de Exceções: Validação de entradas para evitar crash do sistema por erros de digitação do usuário.

- Manipulação de Cores ANSI: Feedback visual com destaque para erros em vermelho no terminal.

---

## 📂 Estrutura Modular do Projeto

A lógica da aplicação foi inteligentemente dividida em um pacote local chamado `lib`, garantindo que cada arquivo tenha uma única responsabilidade:

```text
PROJETO_CADASTRO/
├── lib/
│   ├── __init__.py
│   ├── banco.py          # Gerenciamento do SQLite (tabelas e conexões) e exportação Excel
│   ├── interface.py      # Renderização visual dos menus e layouts do terminal
│   ├── menus.py          # Orquestração das ações e telas de cada funcionalidade
│   └── validar.py        # Tratamento de erros e travas de digitação inválida (ex: validar_int)
├── dados.db              # Banco de dados SQLite de produção
├── main.py               # Ponto de entrada e loop principal do software
└── README.md             # Documentação do projeto
```

---

🚀 Como Executar o Projeto
Você pode rodar esta aplicação diretamente pelo código-fonte ou baixando a versão compilada para o seu sistema operacional.

Opção 1: Executando o Código-Fonte (Para Desenvolvedores)
Certifique-se de ter o Python 3 instalado em sua máquina.
Execute o bash

Clone o repositório:
```bash
git clone [https://github.com/ston01/python-crud-system.git](https://github.com/ston01/python-crud-system.git)
```
Acesse o diretório do projeto:
```bash
cd PROJETO_CADASTRO
python -m pip install openpyxl
```
Inicie o programa:
```bash
python main.py
```

Opção 2: Executando como Aplicativo Nativo (.exe)
Se você deseja apenas testar ou utilizar o software no Windows sem precisar instalar o Python:

1. Acesse a aba Releases deste repositório.

2. Baixe o pacote compactado (.zip) contendo o executável.

3. Extraia o conteúdo e certifique-se de que o arquivo dados.db está localizado na mesma pasta que o main.exe.

4, Dê um duplo clique em main.exe para rodar.

---

🧠 Aprendizados Relevantes

Modularização Avançada: Entendimento prático de como separar códigos extensos em arquivos menores e reutilizáveis via pacotes (import).

Experiência do Usuário (UX/UI no Terminal): Aprendi a controlar o fluxo de telas limpando buffers antigos e usando cores de alerta para guiar o usuário.

Deploy e Distribuição: Utilização do PyInstaller para transformar scripts Python em executáveis prontos para uso em ambiente de produção do cliente final.

---

👤 Autor

Desenvolvido com dedicação por Emanuel
GitHub: @ston01
