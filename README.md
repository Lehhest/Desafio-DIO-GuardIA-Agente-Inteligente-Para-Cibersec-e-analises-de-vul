# Desafio-DIO-GuardIA-Agente-Inteligente-Para-Cibersec-e-analises-de-vul

# 🤖 DIO Agent - Especialização em Cibersegurança

Este repositório contém uma evolução do **DIO Agent**, transformando o assistente de estudos genérico em um **Mentor de Cibersegurança especializado em Application Security (AppSec) e Defesa**. 

A especialização foi implementada seguindo a arquitetura nativa do projeto base, utilizando arquivos de configuração abertos em Markdown lidos pelo harness de execução.

---

## 🎯 Por que esta especialização foi criada?
Em cenários de segurança da informação, respostas rápidas ou scripts automatizados sem a devida contextualização do ambiente podem expor infraestruturas a riscos ainda maiores. 

Esta especialização foi criada para que o agente atue como um **Engenheiro de Segurança Defensiva Sênior**. Em vez de apenas entregar códigos corrigidos ou comandos reativos, o agente obriga o desenvolvedor/analista a fornecer o contexto de rede, sistema operacional e privilégios. Com isso, ele realiza uma triagem estruturada baseada em risco real antes de guiar a mitigação.

---

## 🗂️ Arquivos Criados e Alterados

O projeto foi estendido através dos seguintes componentes:

*   **`skills/vulnerability-analysis/SKILL.md` (Criado):** Roteiro que define o comportamento investigativo do agente. Força as etapas de coleta de contexto, cálculo de risco (Severidade, Impacto e Probabilidade) e mapeamento com frameworks de mercado (MITRE ATT&CK / OWASP).
*   **`skills/vulnerability-analysis/README.md` (Criado):** Documentação em linguagem humana explicando o propósito e funcionamento da nova habilidade para outros desenvolvedores.
*   **`agent/knowledge/security-basics.md` (Criado):** Base de conhecimento teórico municiando o agente com conceitos cruciais como a Tríade CIA (Confidencialidade, Integridade e Disponibilidade), matriz de risco (Risco = Probabilidade × Impacto) e padrões de codificação segura.
*   **`agent/persona.md` (Modificado):** Inclusão de traços comportamentais específicos de AppSec, alterando o tom de voz do agente para analítico, cauteloso e estritamente defensivo quando provocado com falhas de segurança.
*   **`AGENTS.md` (Modificado):** Atualização da tabela global de habilidades (`## 🧩 Skills Disponíveis`) para registrar e indexar a nova skill `Análise de Vulnerabilidade` no ecossistema do agente.

---

## 🚀 Como Rodar o Agente no Harness

Esta evolução foi validada utilizando o harness **Hermes** através do terminal.

### Pré-requisitos
Certifique-se de ter o **Hermes** instalado globalmente ou configurado em seu ambiente de desenvolvimento conforme a documentação oficial.

### Passo a Passo para Execução:
1. Abra o seu terminal.
2. Navegue obrigatoriamente até a pasta raiz deste projeto (onde o arquivo `AGENTS.md` está localizado):
   ```bash
   cd /caminho/para/o/seu/repositorio/dio-agent
   ```
3. Inicie o harness digitando o comando correspondente do seu interpretador do Hermes:
   ```bash
   hermes
   ```
4. O harness lerá automaticamente o arquivo `AGENTS.md` e carregará a nova persona e skill de segurança de forma transparente.

---

## 🔬 Validação Prática (Caso de Teste: SQL Injection)

Para validar a nova habilidade, foi criado um script de laboratório chamado `app.py` utilizando Flask, contendo uma vulnerabilidade crítica de concatenação direta de strings em uma consulta SQL (`SQL Injection`).

### Fluxo de Validação Executado:
1. **Varredura Inicial:** O código do `app.py` foi apresentado ao agente.
2. **Postura Investigativa:** Respeitando a nova skill, o agente não entregou o código corrigido de imediato; ele solicitou o contexto do ambiente (se o banco rodava como root, se estava exposto para a internet, etc.).
3. **Análise de Risco Estruturada:** Após o envio do contexto, o agente gerou um relatório classificando a falha como **Crítica**, mapeando o impacto na **Confidencialidade/Integridade** (Tríade CIA) e associando a técnica ao **OWASP Top 10** e **MITRE ATT&CK**.
4. **Mitigação Defensiva:** O agente orientou detalhadamente a substituição da concatenação por consultas parametrizadas (`Prepared Statements`), validando o fechamento da vulnerabilidade após a correção.

---

## 🛠️ Melhoria Escolhida para Evolução
Para este desafio, a melhoria implementada focou na **Padronização Estrita de Outputs Baseados em Risco**. A inteligência do agente foi calibrada para que qualquer triagem de vulnerabilidade adote uma matriz fixa dividida em três dimensões claras: **Severidade, Impacto e Probabilidade**. Isso aproxima o uso do agente de ferramentas reais de mercado e de relatórios de auditoria profissionais, facilitando a comparação de múltiplos incidentes dentro de um fluxo contínuo de DevSecOps.
