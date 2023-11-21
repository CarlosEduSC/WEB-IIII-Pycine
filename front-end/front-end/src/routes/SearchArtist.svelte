<script>
    import { onMount } from 'svelte';
  
    let searchTerm = '';
    let searchResults = [];
  
    async function searchArtists() {
      try {
        const response = await fetch(`http://localhost:8000/artistas/${encodeURIComponent(searchTerm)}`);
        const data = await response.json();
        searchResults = data;
      } catch (error) {
        console.error('Erro ao pesquisar artistas:', error);
      }
    }
  
    onMount(() => {});
  
  </script>
  
  <style>
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
        </div>
      {/each}
    {:else}
      {#if searchTerm !== ''}
        <p>Nenhum resultado encontrado para "{searchTerm}"</p>
      {/if}
    {/if}
  </main>
  