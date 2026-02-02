document.addEventListener("DOMContentLoaded", function() {
    // ===== Variáveis globais =====
    const form = document.getElementById("cut-form");
    const startBtn = document.getElementById("start");
    const endBtn = document.getElementById("end");
    let player = null;               // guarda o objeto YT.Player
    let videoID = null;              // ID do vídeo
    let pendingVideoID = null;       // ID a ser usado quando a API estiver pronta
    // let times = [null, null];        // [start, end]
    // let cut = [null, null];          // corte [inicio, fim]
    const cutList = document.getElementById("cut-list"); 
    const displayStart = document.getElementById("press_Start");

    // ===== Estado Global =====
    let globalState = {
        "currentStart" : null,
        "cutQueue": [],
        "isProcessing": false
    };

    // ===== Função para criar o player =====
    function createPlayer() {
        player = new YT.Player('player', {
            videoId: pendingVideoID,
            width: 560,
            height: 315
        });
        pendingVideoID = null;
    }

    // ===== Função para marcar tempo =====
    function marcarTempo(){
        let time = null
        if (player){
            if(player.getPlayerState() === YT.PlayerState.PLAYING){
                time = player.getCurrentTime();
            }
            else{
                alert("O player não está reproduzindo");
            }
        }
        else{
            alert("O player não foi carregado")
        }
        return time
    }

    // ===== Listener do form =====
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const input_value = document.getElementById("video-url").value;
        const url = input_value.split("v=");
        let identificador = null;

        if (url[1].includes("&")) {
            identificador = url[1].split("&");
            videoID = identificador[0];
        } else {
            videoID = url[1];
        }

        console.log("Video ID:", videoID);

        // Limpa a div antes de criar o player
        const playerDiv = document.getElementById("player");
        playerDiv.innerHTML = "";

        // Remove player antigo, se existir
        if (player) {
            player.destroy();
        }

        // Guarda o ID para a API carregar
        pendingVideoID = videoID;

        // Se a API já carregou, cria o player imediatamente
        if (typeof YT !== "undefined" && YT.Player) {
            createPlayer();
        }
        // Senão, onYouTubeIframeAPIReady() vai criar quando a API estiver pronta
    });

    // ===== Função chamada automaticamente pela API do YouTube =====
    window.onYouTubeIframeAPIReady = function() {
        if (pendingVideoID) {
            createPlayer();
        }
    };

    // ===== Função de atualizar lista =====
    function atualizar_lista(){
        cutList.innerHTML = "";
        globalState.cutQueue.forEach(corte =>{
            const li = document.createElement("li");
            li.textContent = `Início: ${corte.start.toFixed(2)}    ->  Fim: ${corte.end.toFixed(2)}    Status: ${corte.status}`;
            cutList.appendChild(li);
        });
    };

    // ===== Botões de início e fim =====
    startBtn.addEventListener("click", function() {
        globalState.currentStart = marcarTempo();
        if (globalState.currentStart != null){
            displayStart.textContent = `Inicio marcado em: ${globalState.currentStart.toFixed(2)} segundos`
        }
    });

    endBtn.addEventListener("click", function() {
        if (globalState.currentStart != null) {
            let end = marcarTempo();
            if (end != null){
                if (end > globalState.currentStart){
                    let corte = {
                        "start" : globalState.currentStart,
                        "end" : end,
                        "status" : "pending"
                    };
                    globalState.cutQueue.push(corte);
                    globalState.currentStart = null;
                    displayStart.innerHTML = "";
                    atualizar_lista();
                }
                else{
                    alert("O fim deve ser maior que o início")
                };
            };
        }
        else{
            alert("Você deve marcar o início antes do fim");
            return;
        }
        enviarCorte();
    });

    // ===== Função post =====
    function enviarCorte() {
        if (globalState.isProcessing === true){
            return;
        }
        
        let indice_selecionado = null;

        for (let i=0; i < globalState.cutQueue.length; i++){
            if (globalState.cutQueue[i].status === "pending"){
                indice_selecionado = i;
                break;
            }
        }

        if (indice_selecionado == null){
            return;
        }

        let currentCut = globalState.cutQueue[indice_selecionado];

        currentCut.status = "processing"
        globalState.isProcessing = true

        atualizar_lista()

        fetch("/cut", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: document.getElementById("video-url").value,
                video_id: videoID,
                start: currentCut.start,
                end: currentCut.end
            })
        })
        .then(response => response.text())
        .then(data => {
            console.log("Resposta do servidor: ", data)
            currentCut.status = "done"
            globalState.isProcessing = false
            atualizar_lista()
            enviarCorte()
        })
        .catch(error => {
            console.log("Erro na requisição", error)
            currentCut.status = "error"
            globalState.isProcessing = false
            atualizar_lista()
            enviarCorte()
        });
    }
});
