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
        console.log('Filme adicionado aos favoritos com sucesso.');
      } else {
        throw new Error('Erro ao adicionar o filme aos favoritos.');
      }
    } catch (error) {
      console.error(`Erro: ${error.message}`);
    }
  }

  onMount(getFilmes);
</script>

{#if filmes.length === 0}
  <p>Carregando filmes...</p>
{:else}
  {#each filmes as filme}
    <div
      class="filme-item"
      role="button"
      on:click={() => handleClick(filme)}
      on:keydown={(event) => event.key === 'Enter' && handleClick(filme)}
      tabindex="0"
    >
      <h3>{filme.title}</h3>
      <img src="{filme.image}" alt="{filme.title}" />
      <button on:click={() => salvarFavorito(filme.id)}>Favoritar</button>
    </div>
  {/each}
{/if}

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
  }

  .filme-item {
    border: 1px solid #dee2e6;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    cursor: pointer;
  }

  h3 {
    color: #343a40;
  }

  img {
    max-width: 100%;
    height: auto;
    margin-top: 10px;
  }

  button {
    background-color: #007bff;
    color: #ffffff;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>
