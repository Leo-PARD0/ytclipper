function extrair_id(caminho, base) {
    // Remove a base (ex: /shorts/) e limpa possíveis barras extras
    let id_extraido = caminho.replace(base, '').replace(/^\//, '');
    
    // Separa por '&' (caso venha de watch) ou '?' (caso venha de shorts/youtu.be)
    // O split captura o primeiro elemento [0], que é o ID de 11 caracteres
    return id_extraido.split(/[&?]/)[0];
}

export function id_url(input_value) {
    try {
        const url = new URL(input_value);
        const host = url.hostname.replace('www.', '');
        const path = url.pathname;
        const searchParams = url.searchParams;

        if (host === "youtu.be") {
            // Em youtu.be, o ID está no path: /ID_DO_VIDEO
            return extrair_id(path, '/');
        }

        if (host === 'youtube.com') {
            switch (true) {
                case path.startsWith('/shorts/'):
                    return extrair_id(path, '/shorts/');
                
                case path.startsWith('/embed/'):
                    return extrair_id(path, '/embed/');
                
                case path.startsWith('/watch'):
                    // No caso do watch, o ID não está no path, mas no parâmetro 'v'
                    return searchParams.get('v');
                
                case path.startsWith('/live/'):
                    return extrair_id(path, '/live/');

                default:
                    return "Link não suportado";
            }
        }
    } catch (e) {
        return "URL Inválida";
    }
}
