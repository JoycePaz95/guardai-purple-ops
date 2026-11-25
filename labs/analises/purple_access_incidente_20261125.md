Análise Purple Team — access_incidente.log

Data/hora da análise: 2026-11-25T14:10:41Z (UTC)
Escopo: cópia preservada labs/evidencias_preservadas/COPIA_access_incidente.log.
Fonte consultada: access log estático de 8 linhas. Nenhum host ou sistema ativo foi acessado.

Fase 1 — Trava e ordem de volatilidade (RFC 3227)
- Trava aplicada: não isolar host, bloquear contas, reiniciar sistemas, encerrar processos ou alterar regras de rede nesta análise.
- A evidência disponível é um log persistente. Não há coleta documentada de registradores/cache, RAM, conexões, rotas/ARP, processos, temporários ou swap.
- Como não há acesso/coleta de estado volátil, o estado atual do host e a ordem temporal dos eventos voláteis são inconclusivos por ausência de artefato comprovável. Não executei contenção.
- A ordem RFC 3227 para eventual resposta ativa permanece: registradores/cache; RAM e estado de rede/processos; temporários/swap; disco/logs; logs remotos/backups.

Fase 2 — Preservação e cadeia de custódia (ISO/IEC 27037)
- Registro existente: labs/evidencias_preservadas/cadeia_custodia_access_incidente.json.
- Aquisição registrada: 2026-11-25T14:04:24Z; perito informado no registro: Joyce Paz.
- SHA-256 registrado e recalculado para a cópia: 4b943ee7208f3fdff7f01aee1714029f7ead79865da1080d46178f0750b08e10.
- O hash da cópia coincide com o SHA-256 original registrado; tamanho observado: 901 bytes. A cópia foi lida sem alteração.
- Ressalva de preservação: a cópia está com modo reportado pelo ambiente como 0666 (gravável). Não alterei permissões/metadados durante esta análise. O fluxo de aquisição não garante write-blocking/atributo somente leitura; registrar essa limitação e proteger a mídia/origem por controle externo antes de análise adicional.
- O registro anterior de custódia foi mantido em labs/evidencias_preservadas/cadeia_custodia_access_incidente_20261125T135003Z.json.

Fase 3 — Análise cruzada DFIR + Red Team
Todos os horários abaixo estão em UTC conforme o offset +0000 dos registros. IPs, métodos, caminhos, user-agents, status e bytes são fatos observados no log; não provam execução no servidor nem conteúdo da resposta.
- 13:10:02 e 13:10:15 — 192.168.1.45 solicitou /index.html e /produtos?id=10; ambos responderam HTTP 200.
- 13:14:22 — 45.33.32.156 solicitou /admin/login.php com user-agent Gobuster/3.6; HTTP 404. Compatível com varredura por lista de caminhos, MITRE ATT&CK T1595.003 (Wordlist Scanning); o log não estabelece autoria ou intenção.
- 13:14:25 — mesmo IP solicitou /upload.php com o mesmo user-agent; HTTP 200. Indica resposta do endpoint, não prova que upload ocorreu.
- 13:15:10 — requisição GET a /produtos com payload URL-encoded contendo UNION SELECT user,password FROM users; HTTP 200 e 8490 bytes enviados. Compatível com tentativa de explorar aplicação pública, T1190 (Exploit Public-Facing Application). Não é possível confirmar injeção, extração ou exposição de credenciais a partir do access log.
- 13:16:40 — POST a /upload.php por 45.33.32.156, user-agent curl/8.5.0; HTTP 200 e 512 bytes. O corpo enviado e o estado do arquivo não estão disponíveis.
- 13:17:05 — GET a /uploads/shell.php?cmd=id;whoami;cat%20/etc/passwd; HTTP 200 e 1420 bytes. O caminho/parâmetro são compatíveis com tentativa de usar um web shell (T1505.003) e comandos de shell Unix (T1059.004). O status/bytes não comprovam que o arquivo existia, que comandos executaram, ou que /etc/passwd foi retornado.
- 13:18:12 — 192.168.1.48 solicitou /contato; HTTP 200. O artefato não permite relacionar essa requisição às anteriores.
- Conclusão DFIR: há requisições suspeitas sucessivas originadas de 45.33.32.156, incluindo varredura, payload compatível com SQLi, POST de upload e acesso a caminho semelhante a web shell. Comprometimento, execução, exfiltração, persistência e impacto permanecem não confirmados. Fato inconclusivo por ausência de artefatos de aplicação, payloads, resposta, sistema de arquivos, processo e rede.

Fase 4 — Detecção e blindagem (Blue Team)
- Regras entregues em sigma_web_suspicious_access.yml e kql_web_suspicious_access.kql nesta pasta. Sigma considera o evento completo no campo message; KQL usa WebAccess_CL/RawData como nomes de exemplo, que devem ser mapeados à ingestão real.
- S.A.F.E.:
  Superfície: inventariar /produtos, /upload.php e /uploads; identificar exposição pública e fluxos de upload.
  Ameaça: monitorar varredura de caminhos, SQLi e requisições com parâmetros de comando.
  Falha: revisar consultas SQL parametrizadas, autenticação/autorização e validação de upload; verificar se uploads ficam fora da raiz web e sem permissão de execução.
  Escudo: configurar detecção/WAF para padrões de SQLi e uploads suspeitos; restringir execução de scripts no diretório de upload; aplicar menor privilégio e registrar requisições/correlação com logs de aplicação e host.
- Não aplicar bloqueios/isolar sistemas até a coleta volátil necessária e autorização conforme trava forense. Correlacionar primeiro com logs de aplicação, eventos de arquivo/processo, EDR e tráfego para confirmar ou refutar execução.

Limitações
- knowledge/tools-cheatsheet.md foi lido e está vazio (0 bytes); não forneceu comandos ou orientações adicionais.
- Não foram consultados código da aplicação, logs de erro/auditoria, conteúdo HTTP, filesystem, RAM, EDR ou firewall. Nenhuma conclusão além dos campos observados no log é afirmada.
