import sys
from pathlib import Path

def get_clipper_root():
    if getattr(sys, "frozen", False):
        base_path = sys.executable
        base_dir = Path(base_path).resolve().parent

        cutter_path = base_dir / "cutter"
    else:
        base_path = __file__
        base_dir = Path(base_path).resolve().parent

        cutter_path = base_dir.parent / "cutter"
    
    return cutter_path

def require_cutter():
    cutter = get_clipper_root()

    if not cutter.exists():
        raise FileNotFoundError("Pasta cutter apagada, descompacte o app de novo")
    
    return cutter

def get_essentials():
    cutter = require_cutter()

    essentials = {
        'yt-dlp.exe' : Path(cutter / 'essentials' / 'bin' / 'yt-dlp.exe'),
        'ffmpeg.exe' : Path(cutter / 'essentials' / 'bin' / 'ffmpeg.exe')
    }
    
    for nome, caminho in essentials.items():
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo essencial {nome} faltando!")
    
    return essentials


def get_data_root():
    cutter = require_cutter()

    data = cutter / "data"

    if not data.exists():
        data.mkdir(parents=True, exist_ok=True)
    
    pastas = {
        "cut": ["fast", "slow"],
        "tmp": ["fast", "slow"],
        "logs": None
    }

    for pasta_mae, conteudo in pastas.items():
        caminho_base = data / pasta_mae

        match conteudo:
            case list():
                for sub in conteudo:
                    (caminho_base / sub).mkdir(parents=True, exist_ok=True)
            
            case str():
                (caminho_base / conteudo).mkdir(parents=True, exist_ok=True)
            
            case None:
                caminho_base.mkdir(parents=True, exist_ok=True)
            
            case _:
                print(f"Formato desconhecido para {pasta_mae}")
    
    return data