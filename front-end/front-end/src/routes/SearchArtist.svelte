<script>
  import { onMount } from 'svelte';

  let searchTerm = '';
  let searchResults = [];
  const user_id = 1;

  async function searchArtists() {
    try {
      const response = await fetch(`http://localhost:8000/artistas/${encodeURIComponent(searchTerm)}`);
      const data = await response.json();
      searchResults = data;
    } catch (error) {
      console.error('Erro ao pesquisar artistas:', error);
    }
  }

  async function salvarFavorito(artista_id) {
    try {
      const response = await fetch(`http://localhost:8000/favoritos_artista/${user_id}/${artista_id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id, artista_id })
      });
      if (response.ok) {
        console.log('Artista adicionado aos favoritos com sucesso.');
        console.log(response);
        console.log(artista_id);
        console.log(user_id);
      } else {
        throw new Error('Erro ao adicionar o artista aos favoritos.');
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

  .artista-item {
    margin-bottom: 20px;
    border: 1px solid #ddd;
    padding: 10px;
  }

  .artista-image {
    max-width: 200px;
    max-height: 300px;
    margin-bottom: 10px;
  }
</style>

<main>
  <input bind:value={searchTerm} placeholder="Digite o nome do artista" />
  <button on:click={searchArtists}>Pesquisar</button>

  {#if searchResults.length > 0}
    <h2>Resultados da Pesquisa</h2>
    {#each searchResults as artista}
      <div class="artista-item">
        <h3>{artista.name}</h3>
        <p>ID: {artista.id}</p>
        <p>Popularidade: {artista.rank}</p>
        {#if artista.birthday}
          <p>Data de Nascimento: {artista.birthday}</p>
        {/if}
        {#if artista.image}
          <img class="artista-image" src="{artista.image}" alt="{artista.name}" />
        {/if}
        {#if artista.biography}
          <p>Biografia: {artista.biography}</p>
        {/if}
        <button on:click={() => salvarFavorito(artista.id)}>Favoritar</button>
      </div>
    {/each}
  {:else}
    {#if searchTerm !== ''}
      <p>Nenhum resultado encontrado para "{searchTerm}"</p>
    {/if}
  {/if}
</main>
