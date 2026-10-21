# Fundamentos de Segurança da Informação (AppSec & Defesa)

## Tríade CIA
- **Confidencialidade**: Garantir que as informações só sejam acessadas por pessoas autorizadas.
- **Integridade**: Garantir que a informação não seja alterada de forma não autorizada ou maliciosa.
- **Disponibilidade**: Garantir que os sistemas e dados estejam acessíveis quando necessários.

## Gestão de Risco e Vulnerabilidades
- **Vulnerabilidade**: Uma fraqueza no software, hardware ou processo que pode ser explorada.
- **Ameaça**: Um agente ou evento com potencial de explorar uma vulnerabilidade.
- **Risco**: A relação entre a probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto gerado ($Risco = Probabilidade \times Impacto$).

## Severidade de Vulnerabilidades (Padrão CVSS simplificado)
- **Crítica**: Exploração remota simples, sem autenticação, com perda total de CIA (Ex: RCE, SQLi c/ privilégios de DBA).
- **Alta**: Exploração com pouca restrição ou vazamento direto de dados sensíveis.
- **Média**: Requer condições específicas ou autenticação prévia.
- **Baixa**: Baixo impacto local ou vazamento de informações irrelevantes (Ex: banners de versão).

## Boas Práticas de Codificação Segura (Secure Coding)
1. **Nunca confie no input do usuário**: Valide, filtre e sanitize todas as entradas.
2. **Consultas Parametrizadas**: Sempre utilize Prepared Statements para consultas em bancos de dados.
3. **Princípio do Menor Privilégio**: Aplicações devem rodar com o mínimo de permissões necessárias no sistema operacional e no banco.
