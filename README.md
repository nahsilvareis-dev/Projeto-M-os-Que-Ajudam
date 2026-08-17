# 🤝 Mãos que Ajudam — Gestão de Doações

> Aplicação web desenvolvida em Flask para centralizar, gerenciar e divulgar campanhas de arrecadação comunitárias.

---

## 📌 Status do Projeto

* **Fase Atual:** `MVP (Produto Mínimo Viável) Funcional`
* **Descrição do Estado Atual:** A versão atual conta com a estrutura Front-end (HTML5/CSS3) integrada ao servidor Back-end (Python/Flask), permitindo navegação entre rotas, exibição de campanhas e manipulação inicial do fluxo de doações.

---

## 🎯 Objetivo do Projeto

O **Mãos que Ajudam** resolve a falta de visibilidade enfrentada por pequenas instituições comunitárias através de três pilares:

* **Centralização:** Ponto único de acesso para registro de campanhas.
* **Transparência:** Exibição clara do progresso das arrecadações para os doadores.
* **Acessibilidade:** Interface simples e otimizada para navegação rápida.

---

## 🛠️ Tecnologias Utilizadas

### **Implementadas no MVP Atual:**
| Camada | Tecnologia | Função Principal |
| :--- | :--- | :--- |
| **Back-end** | Python 3.x | Regras de negócio e processamento local |
| **Framework** | Flask | Roteamento HTTP, renderização de templates e controle de requisições (`GET`/`POST`) |
| **Templates** | Jinja2 | Renderização dinâmica de dados |
| **Front-end** | HTML5 / CSS3 | Estruturação e estilização visual das interfaces |
| **Persistência** | CSV / Arquivo Local | Armazenamento inicial de registros de doações |
| **Versionamento** | Git / GitHub | Controle de versão e documentação pública |

### **Planejadas para Próximas Versões:**
* **Banco de Dados Relacional:** Migração para SQLite / PostgreSQL via SQLAlchemy.
* **Autenticação:** Sistema de login e cadastro de administradores/doadores com Flask-Login.

---

## 🚀 Próximos Passos & Roadmap

- [x] Criação das telas e layout responsivo (HTML/CSS)
- [x] Configuração da estrutura de rotas e rotinas no Flask
- [x] Processamento de formulários via requisições HTTP (`POST`)
- [ ] Integração com Banco de Dados Relacional (PostgreSQL)
- [ ] Implementação de Painel Administrativo para cadastro de novas campanhas

---

## 📚 Aprendizados e Resultados

* **Arquitetura Web:** Domínio do ciclo de requisição/resposta (`GET`/`POST`) e roteamento dinâmico.
* **Estruturação de Código:** Organização do padrão Flask em diretórios distintos (`/templates`, `/static`, `/data`).
* **Boas Práticas de Engenharia:** Versionamento semântico de commits e documentação técnica padronizada.
