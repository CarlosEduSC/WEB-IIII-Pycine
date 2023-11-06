<script>
    let filmesFavoritos = [];
    
    async function fetchFavorites() {
        const response = await fetch(`http://localhost:8000/favoritos/${user_id}`);
        if (response.ok) {
            filmesFavoritos = await response.json();
        } else {
            console.error('Erro ao recuperar filmes favoritos.');
        }
    }
  
    async function excluirFavorito(filme_id) {
        const response = await fetch(`http://localhost:8000/favoritos/${user_id}/${filme_id}`, {
            method: 'DELETE'
        });
        if (response.ok) {
            console.log('Filme removido com sucesso.');
            filmesFavoritos = filmesFavoritos.filter((filme) => filme.id !== filme_id);
        } else {
            console.error('Erro ao excluir o filme.');
        }
    }
  
    fetchFavorites();
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