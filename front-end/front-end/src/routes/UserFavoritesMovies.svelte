<script>
    import { onMount } from "svelte";
    import Page from "./+page.svelte";

    let filmesFavoritos = [];

    const user_id = 1;
    
    async function fetchFavorites() {
        const response = await fetch(`http://localhost:8000/favoritos/${user_id}`);
        if (response.ok) {
            filmesFavoritos = await response.json();
        } else {
            console.error('Erro ao recuperar filmes favoritos.');
        }
    }
  
    async function excluirFavorito(filme_id) {
    try {
      const response = await fetch(`http://localhost:8000/favoritos/${user_id}/${filme_id}`, {
        method: 'DELETE'
      });
      if (response.ok) {
        toast.success('Filme removido dos favoritos com sucesso.');
        filmesFavoritos = filmesFavoritos.filter((filme) => filme.id !== filme_id);
      } else {
        throw new Error('Erro ao remover o filme dos favoritos.');
      }
    } catch (error) {
      toast.error(`Erro: ${error.message}`);
    }
  }
  
    onMount(fetchFavorites)
  </script>
  
  <div>
    <h1>Meus Filmes Favoritos</h1>
    {#if filmesFavoritos.length === 0}
      <p>Você não tem nenhum filme favorito.</p>
    {:else}
      {#each filmesFavoritos as filme}
        <div class="favorite-item">
          <h3>{filme.title}</h3>
          <img src="{filme.image}" alt="{filme.title}" />
          <button on:click={() => excluirFavorito(filme.id)}>Remover dos Favoritos</button>
        </div>
      {/each}
    {/if}
  </div>

  <style>
    div {
      font-family: 'Arial', sans-serif;
      background-color: #f8f9fa;
      margin: 0;
      padding: 0;
    }
  
    .favorite-item {
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