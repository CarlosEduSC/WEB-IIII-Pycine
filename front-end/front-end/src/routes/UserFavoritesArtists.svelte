<script>
    import { onMount } from "svelte";
    
    let artistasFavoritos = [];
    
    const user_id = 1;
    
    async function fetchFavorites() {
      try {
        const response = await fetch(`http://localhost:8000/favoritos_artista/${user_id}`);
        if (response.ok) {
          artistasFavoritos = await response.json();
        } else {
          throw new Error('Erro ao recuperar artistas favoritos.');
        }
      } catch (error) {
        console.error(error.message);
      }
    }
    
    async function excluirFavorito(artista_id) {
      try {
        const response = await fetch(`http://localhost:8000/favoritos_artista/${user_id}/${artista_id}`, {
          method: 'DELETE'
        });
        if (response.ok) {
          console.log('Artista removido dos favoritos com sucesso.');
          artistasFavoritos = artistasFavoritos.filter((artista) => artista.id !== artista_id);
        } else {
          throw new Error('Erro ao remover o artista dos favoritos.');
        }
      } catch (error) {
        console.error(`Erro: ${error.message}`);
      }
    }
    
    onMount(fetchFavorites);
  </script>
  
  <style>
    div {
      font-family: 'Arial', sans-serif;
      background-color: #f8f9fa;
      padding: 20px;
    }
  
    h1 {
      color: #343a40;
    }
  
    .favorite-item {
      border: 1px solid #dee2e6;
      padding: 15px;
      margin: 10px;
      border-radius: 8px;
      background-color: #ffffff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  
    h3 {
      color: #343a40;
    }
  
    p {
      color: #6c757d;
    }
  
    .artista-image {
    max-width: 200px;
    max-height: 300px;
    margin-bottom: 10px;
  }
  
    button {
      background-color: #dc3545;
      color: #ffffff;
      border: none;
      padding: 8px 15px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
  
    button:hover {
      background-color: #c82333;
    }
  </style>
  
  <div>
    <h1>Meus Artistas Favoritos</h1>
    {#if artistasFavoritos.length === 0}
      <p>Você não tem nenhum artista favorito.</p>
    {:else}
      {#each artistasFavoritos as artista}
        <div class="favorite-item">
          <h3>{artista.name}</h3>
          <p>ID: {artista.id}</p>
          <p>Popularidade: {artista.rank}</p>
          <p>Data de Nascimento: {artista.birthday}</p>
          <img class="artista-image" src="{artista.image}" alt="{artista.name}" />
          <p>Biografia: {artista.biography}</p>
          <button on:click={() => excluirFavorito(artista.id)}>Remover dos Favoritos</button>
        </div>
      {/each}
    {/if}
  </div>
  