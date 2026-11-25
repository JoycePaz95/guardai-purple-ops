import hashlib
import shutil
import sys
import json
from datetime import datetime, timezone
from pathlib import Path

def calcular_sha256(caminho: Path) -> str:
    sha256 = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            sha256.update(bloco)
    return sha256.hexdigest()

def preservar_evidencia(arquivo_origem: str, perito: str = "Joyce Paz"):
    origem = Path(arquivo_origem)
    if not origem.exists():
        print(f"[ERRO] Arquivo nao encontrado: {origem}")
        return

    timestamp_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    hash_original = calcular_sha256(origem)

    dir_trabalho = origem.parent / "evidencias_preservadas"
    dir_trabalho.mkdir(exist_ok=True)

    destino = dir_trabalho / f"COPIA_{origem.name}"
    shutil.copy2(origem, destino)
    hash_copia = calcular_sha256(destino)

    if hash_original != hash_copia:
        print("[CRITICO] Falha na verificacao de integridade da copia!")
        return

    registro = {
        "norma": "ISO/IEC 27037",
        "timestamp_aquisicao_utc": timestamp_utc,
        "perito_responsavel": perito,
        "arquivo_original": str(origem.resolve()),
        "copia_trabalho": str(destino.resolve()),
        "sha256_original": hash_original,
        "sha256_copia": hash_copia,
        "integridade_verificada": True
    }

    log_custodia = dir_trabalho / f"cadeia_custodia_{origem.stem}.json"
    with open(log_custodia, "w", encoding="utf-8") as f:
        json.dump(registro, f, indent=4, ensure_ascii=False)

    print(f"[OK] Evidencia preservada com sucesso (ISO/IEC 27037)!")
    print(f"     UTC:    {timestamp_utc}")
    print(f"     SHA256: {hash_original}")
    print(f"     Log:    {log_custodia}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python labs/custodia.py <caminho_do_arquivo>")
    else:
        preservar_evidencia(sys.argv[1])
