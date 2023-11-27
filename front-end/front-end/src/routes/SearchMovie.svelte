<script>
  import { onMount } from 'svelte';

  let user_id = 1;
  let searchTerm = '';
  let searchResults = [];

  async function searchFilmes() {
    try {
      const response = await fetch(`http://localhost:8000/filme/${encodeURIComponent(searchTerm)}`);
      const data = await response.json();
      searchResults = data;
    } catch (error) {
      console.error('Erro ao pesquisar filmes:', error);
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

  onMount(() => {});
</script>

<style>
  body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
  }

  main {
    margin: 20px;
  }

  input {
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  button {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #ffffff;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }

  .filme-item {
    margin-bottom: 20px;
    border: 1px solid #ddd;
    padding: 10px;
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

<main>
  <input bind:value={searchTerm} placeholder="Digite o nome do filme" />
  <button on:click={searchFilmes}>Pesquisar</button>

  {#if searchResults.length > 0}
    <h2>Resultados da Pesquisa</h2>
    {#each searchResults as filme}
      <div class="filme-item" on:click={() => handleClick(filme)}>
        <h3>{filme.title}</h3>
        <img src="{filme.image}" alt="{filme.title}" />
        <button on:click={() => salvarFavorito(filme.id)}>Favoritar</button>
      </div>
    {/each}
  {:else}
    {#if searchTerm !== ''}
      <p>Nenhum resultado encontrado para "{searchTerm}"</p>
    {/if}
  {/if}
</main>
