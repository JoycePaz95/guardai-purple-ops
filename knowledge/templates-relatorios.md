# Templates de Relatórios: GuardAI Purple Ops

O Orquestrador deve utilizar estritamente um destes três formatos quando o usuário solicitar o comando `/laudo`.

## 1. Laudo Técnico Pericial (`/laudo juridico`)
*Público: Jurídico, Compliance, Auditoria Externa e Autoridades.*
*Tom: Impessoal, estritamente factual, sem suposições, baseado apenas em artefatos com hash verificado.*

```markdown
# LAUDO TÉCNICO PERICIAL DE INCIDENTE CIBERNÉTICO
**Protocolo/Caso:** [ID] | **Data de Emissão (UTC):** [YYYY-MM-DDTHH:MM:SSZ]
**Normas Aplicadas:** ISO/IEC 27037:2012 e RFC 3227

## 1. Objetivo da Perícia
Descrever o escopo exato da análise solicitada.

## 2. Identificação e Cadeia de Custódia das Evidências

| Artefato | Caminho Original | Hash SHA-256 | Data/Hora Aquisição (UTC) |
| :--- | :--- | :--- | :--- |
| [Nome] | [Path] | `[Hash completo]` | [Timestamp UTC] |

## 3. Metodologia e Ferramentas Utilizadas
Listar ferramentas e comandos exatos executados sobre as cópias de trabalho (garantindo repetibilidade).

## 4. Cronologia dos Fatos Comprovados (Timeline UTC)
- **[Timestamp UTC]:** Fato comprovado pelo artefato X (linha/offset Y).
*(Nota: Eventos sem lastro técnico direto devem ser marcados como "Inconclusivo por ausência de artefato").*

## 5. Indicadores de Comprometimento (IoCs) Identificados
- **Endereços IP:** ...
- **Hashes de Arquivos:** ...
- **URIs / Comandos:** ...

## 6. Conclusão Pericial
Síntese objetiva dos fatos tecnicamente comprovados.
```

## 2. Relatório Técnico de Operações (`/laudo tecnico`)
*Público: Equipes de SOC, AppSec, Infraestrutura e Engenharia.*
*Tom: Direto, acionável, focado em TTPs, detecção e remediação.*

```markdown
# RELATÓRIO TÉCNICO PURPLE TEAM: ANÁLISE E REMEDIAÇÃO
**Severidade:** [Crítica / Alta / Média / Baixa] | **Frameworks:** MITRE ATT&CK / OWASP

## 1. Resumo da Vetorização (Visão Red Team)
- **Vulnerabilidade Explorada:** [Descrição + CWE]
- **Mapeamento MITRE ATT&CK:** [Tática -> Técnica (ID)]
- **Caminho de Exploração:** Passo a passo resumido do vetor de entrada.

## 2. Artefatos e Causa Raiz (Visão DFIR)
- **Causa Raiz:** [Ex: Falta de sanitização / Permissão excessiva]
- **Evidências-Chave:** Trechos de log ou memória que confirmam a ação.

## 3. Plano de Contenção e Blindagem (Visão Blue Team - Método S.A.F.E.)
- **Ação Imediata (Contenção):** [Bloqueio de IP, revogação de token, patch emergencial]
- **Correção Definitiva (Escudo):** [Código corrigido ou comando de hardening]
- **Regra de Detecção (Sigma / KQL):** [Bloco de código da regra criada]
```

## 3. Sumário Executivo (`/laudo executivo`)
*Público: Diretoria (C-Level), Gestores de Negócio e Comitê de Crise.*
*Tom: Estratégico, sem jargão técnico excessivo, focado em impacto ao negócio, risco e investimento.*

```markdown
# SUMÁRIO EXECUTIVO: AVALIAÇÃO DE RISCO E INCIDENTE
**Nível de Risco ao Negócio:** [Crítico / Alto / Moderado / Baixo]

## 1. O que aconteceu (Visão Geral)
Explicação clara em 3 linhas sobre o incidente ou vulnerabilidade testada e quais ativos de negócio foram envolvidos.

## 2. Impacto Operacional e Regulatório
- **Confidencialidade / Dados (LGPD):** Houve exposição ou risco de vazamento de dados sensíveis?
- **Disponibilidade:** Houve interrupção de serviço crítico?
- **Integridade:** Algum registro ou sistema foi alterado indevidamente?

## 3. Ações Já Tomadas e Próximos Passos
- **Contenção:** O que já foi isolado/corrigido.
- **Prevenção Estrutural:** Recomendações de processo, arquitetura ou governança para evitar recorrência.
```
