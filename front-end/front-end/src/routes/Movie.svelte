<script>

    import { onMount } from 'svelte';
    let user_id = 1;
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

    async function salvarFavorito(filme_id) {
    try {
      const response = await fetch(`http://localhost:8000/favoritos/${user_id}/${filme_id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id, filme_id })
      });
      if (response.ok) {
        toast.success('Filme adicionado aos favoritos com sucesso.');
      } else {
        throw new Error('Erro ao adicionar o filme aos favoritos.');
      }
    } catch (error) {
      toast.error(`Erro: ${error.message}`);
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
            <button on:click={() => salvarFavorito(filme.id)}>Favoritar</button>
        </div>
    {/each}
{/if}