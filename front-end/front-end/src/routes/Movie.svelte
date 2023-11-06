<script>

    import { onMount } from 'svelte';
    let user_id = 1; // Defina o user_id conforme necessário
    let filmes = [];

    async function getFilmes() {
        try {
            const response = await fetch('http://localhost:8000/filmes');
            const data = await response.json();
            filmes = data;
        } catch (error) {
            console.error('Erro ao obter filmes:', error);
        }
    }

    async function handleClick(filme) {
        console.log('Filme selecionado:', filme.title);
    }

    async function salvarFavorito(user_id, filme_id) {
        try {
            const response = await fetch(`http://localhost:8000/favoritos/${user_id}/${filme_id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id, filme_id })
            });
            if (response.ok) {
                console.log('Filme salvo com sucesso.');
                // Adicione aqui a lógica para atualizar a lista de favoritos na tela
            } else {
                console.error('Erro ao salvar o filme.');
            }
        } catch (error) {
            console.error('Erro ao salvar o filme:', error);
        }
    }

    async function excluirFavorito(user_id, filme_id) {
        try {
            const response = await fetch(`http://localhost:8000/favoritos/${user_id}/${filme_id}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                console.log('Filme removido com sucesso.');
                // Adicione aqui a lógica para atualizar a lista de favoritos na tela
            } else {
                console.error('Erro ao excluir o filme.');
            }
        } catch (error) {
            console.error('Erro ao excluir o filme:', error);
        }
    }

    onMount(getFilmes);
</script>

{#if filmes.length === 0}
    <p>Carregando filmes...</p>
{:else}
    {#each filmes as filme}
        <div class="filme-item" on:click={() => handleClick(filme)}>
            <h3>{filme.title}</h3>
            <img src="{filme.image}" alt="{filme.title}" />
            <button on:click={() => salvarFavorito(user_id, filme.id)}>Favoritar</button>
            <button on:click={() => excluirFavorito(user_id, filme.id)}>Remover dos Favoritos</button>
        </div>
    {/each}
{/if}