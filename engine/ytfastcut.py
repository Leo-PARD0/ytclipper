#import os # nomear os arquivos
import subprocess # rodar os comandos do console
import shutil # mover arquivos
import time
from pathlib import Path

from core.app_path import get_clipper_root, get_data_root, get_essentials # função que descobre a pasta que está rodando o aplicativo

# ===== CONSTANTE DE clipper e ytdlp =====
cutter_dir = get_clipper_root()
essentials = get_essentials()
yt_dlp = essentials["yt-dlp.exe"]


# ===== Constantes de Pasta ===== 
data_root = get_data_root()
TMP_DIR = data_root / "tmp" / "fast"
CUT_DIR = data_root / "cut" / "fast"

def cortar_rapido(url, video_id, start, end):
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    CUT_DIR.mkdir(parents=True, exist_ok=True)

    clipe = f"*{start}-{end}"

    filename = f"{video_id}_{int(start)}_{int(end)}"
    
    output_path = TMP_DIR / filename

    comando = [str(yt_dlp), "--download-sections", clipe, "-o", str(output_path), url]
    '''comando = [
        "yt-dlp",
        "-f", "bv+ba/b", # Pega o melhor vídeo e áudio independente da extensão
        "--download-sections", clipe,
        "--merge-output-format", "mp4", # Se precisar juntar, faz em mp4
        "--remux-video", "mp4",         # Se já baixar pronto, converte para mp4
        "-o", output_path,
        url
    ]'''

    inicio_execucao = time.time()

    resultado = subprocess.run(comando)

    if resultado.returncode == 0:
        while True:
            exist_part = False
            arquivos_finais = []
            arquivos = TMP_DIR.iterdir()
            for i in arquivos:
                if i.is_file():
                    if i.stat().st_mtime > inicio_execucao:
                        if i.name.endswith(".part"):
                            exist_part = True
                        else:
                            if i.stat().st_size > 0:
                                arquivo_path = i
                                arquivos_finais.append(arquivo_path)
                            else:
                                raise RuntimeError("Tamanho do arquivo inválido")
                    else:
                        pass
                else:
                    pass
            if exist_part == False:
                if len(arquivos_finais) == 1:
                    corte_final = shutil.move(str(arquivos_finais[0]), str(CUT_DIR))
                else:
                    raise FileNotFoundError("Arquivo não encontrado")
                
                if Path(corte_final).exists():
                    return corte_final
            else:
                pass
    else:
        raise RuntimeError("yt-dlp não rodou")

                        
    
if __name__ == "__main__":
    url = input("Digite a URL do vídeo: ")
    video_id = input("Digite o video_id: ")
    start = float(input("Digite o tempo inicial (segundos): "))
    end = float(input("Digite o tempo final (segundos): "))

    cortar_rapido(url, video_id, start, end)

