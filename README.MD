# ✂️ Live Cutter


<img src="assets/qr_code_pix.png" alt="QR Code Pix" width="200">

> Apoio é opcional. Se este projeto foi útil para você, há formas de contribuir mais abaixo.

---

## O que é

O **Live Cutter** é um aplicativo local para criadores de conteúdo que precisam **marcar e cortar trechos de vídeos do YouTube** de forma simples e direta.

Ele roda **localmente no navegador**, utilizando **Flask** como backend e **HTML/JavaScript** no frontend.  
O projeto não hospeda conteúdo, não funciona como serviço online e não oferece processamento remoto.

---

## Visão geral de uso

1. Cole a URL de um vídeo do YouTube  
2. Carregue o vídeo no player  
3. Marque o tempo de início e fim do trecho  
4. As informações do corte são enviadas automaticamente e de forma individual para o backend  
5. O processamento ocorre localmente, conforme os cortes são registrados

> Este repositório documenta o **estado atual do projeto**. Algumas partes ainda estão em desenvolvimento.

> 🤫Meu agente não me permite informar que a interface virá provavelmente nas próximas duas atualizações🤫

---

## Leia na sua língua

| 🇧🇷 Português (principal) | 🌍 English (international) |
|--------------------------|-----------------------------|
| 📘 [README.pt-BR.md](README.pt-br.md) | 📘 [README.en.md](README.en.md) |
| [Introdução](README.pt-BR.md#introducao) | [Introduction](README.en.md#introduction) |
| [Funcionalidades](README.pt-BR.md#funcionalidades-estado-atual) | [Features](README.en.md#current-features) |
| [Limitações](README.pt-BR.md#limitacoes-e-postura-do-projeto) | [Limitations](README.en.md#limitations-and-project-stance) |
| [💡 Ideias em aberto](README.pt-BR.md#ideias-em-aberto) | [Open ideas](README.en.md#open-ideas) |
| [Apoio](README.pt-BR.md#apoio-ao-projeto) | [Support](README.en.md#support-the-project) |
| [Licença](README.pt-BR.md#licenca) | [License](README.en.md#license) |

---

## Apoio ao projeto

O Live Cutter é um projeto independente, desenvolvido de forma incremental.

- 🇧🇷 **Brasil:** [Apoia.se](https://apoia.se/ytclipper) — página oficial de apoio ao projeto  
- 🌍 **Internacional:** [Buy Me a Coffee](https://buymeacoffee.com/LeoPardo) — apoio consciente e voluntário  

O apoio é opcional e não está associado a promessas, contrapartidas ou garantias.

---

## Licença

Este projeto é distribuído sob a **licença MIT**.

Consulte o arquivo [`licence/LICENSE.txt`](licence/LICENSE.txt) para mais informações.

O projeto pode utilizar ferramentas de terceiros, cujas licenças são documentadas separadamente.
As licenças aplicáveis estão documentadas no diretório [`licence/Third_Party/`](licence/Third_Party/).

#### Nota para desenvolvedores:
Este repositório contém apenas o código-fonte.
Os binários necessários para execução (ex: yt-dlp) não são versionados e estão disponíveis apenas nos releases.