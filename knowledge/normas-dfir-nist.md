# Normas Internacionais de DFIR e Resposta a Incidentes

Este documento define os padrões obrigatórios que o **Perito Forense (DFIR)** e o **Orquestrador Purple Team** devem aplicar em qualquer investigação ou laboratório.

## 1. Ordem de Volatilidade: RFC 3227
Ao responder a um incidente em um sistema ativo, a coleta **deve** ocorrer estritamente do dado mais volátil para o menos volátil:

1. **Registradores, cache de CPU e memória de vídeo.**
2. **Tabelas de roteamento, cache ARP, tabela de processos, estatísticas do kernel e memória RAM.**
3. **Sistemas de arquivos temporários (`/tmp`, `/var/tmp`, swap).**
4. **Discos rígidos, sistemas de arquivos persistentes e logs locais (`/var/log`).**
5. **Logs remotos (SIEM/Syslog) e topologia física/lógica da rede.**
6. **Mídias de backup e arquivamento.**

> **Trava Operacional:** O Blue Team está proibido de isolar a interface de rede bruscamente (se houver sessão C2 ativa a ser capturada na RAM) ou reiniciar o host antes da conclusão das etapas 1 a 3.

## 2. Aquisição e Preservação: ISO/IEC 27037
Toda evidência digital só possui valor probatório se atender a quatro pilares:

* **Auditabilidade:** Outro perito deve conseguir avaliar cada passo executado.
* **Repetibilidade:** O mesmo procedimento aplicado sobre a mesma evidência deve gerar exatamente o mesmo resultado.
* **Reprodutibilidade:** O resultado deve ser consistente mesmo usando ferramentas diferentes e validadas.
* **Justificabilidade:** Cada ação tomada deve ter motivação técnica clara (ex: por que coletar a RAM antes do disco).

### Regras de Cadeia de Custódia
1. **Operação em Somente Leitura:** Nunca analisar a evidência original; trabalhar exclusivamente sobre uma cópia bit a bit.
2. **Integridade Criptográfica:** Gerar hash **SHA-256** no momento exato da coleta e revalidar a cada transferência.
3. **Padronização Temporal:** Registrar todos os eventos, logs e metadados (MACB: Modified, Accessed, Created, Born) em horário **UTC (ISO 8601)**.

## 3. Ciclo de Resposta a Incidentes: NIST SP 800-61
1. **Preparação:** Hardening, telemetria ativa, sincronização NTP (UTC) e playbooks definidos.
2. **Detecção e Análise:** Triagem de alertas, validação de IoCs, reconstrução de timeline e escopo do impacto.
3. **Contenção, Erradicação e Recuperação:**
   - *Contenção:* Isolamento de rede/conta (somente após coleta volátil).
   - *Erradicação:* Remoção de artefatos maliciosos, webshells, persistência (cron, serviços) e aplicação de patches.
   - *Recuperação:* Restauração controlada de serviços e monitoramento intensivo pós-incidente.
4. **Atividade Pós-Incidente (Lições Aprendidas):** Atualização de regras SIEM/EDR, ajuste de políticas e emissão de relatório final.
