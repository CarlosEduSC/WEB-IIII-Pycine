<script>
	let promise = getUsers();
  
	async function getUsers() {
	  try {
		const res = await fetch(`http://localhost:8000/users`);
		const text = await res.json();
		if (res.ok) {
		  return text;
		} else {
		  throw new Error(text);
		}
	  } catch (error) {
		console.error('Erro ao obter usuários:', error);
		throw error;
	  }
	}
  
	function handleClick() {
	  promise = getUsers();
	}
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
  
	p {
	  color: #343a40;
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
  
	.loading {
	  color: #28a745;
	}
  
	.error {
	  color: #dc3545;
	}
  </style>
  
  <div>
	<h1>Lista de usuários</h1>
	<button on:click={handleClick}>Get Users</button>
  
	{#await promise}
	  <p class="loading">...Carregando</p>
	{:then users}
	  {#each users as user}
		<div>
		  <p>ID: {user.id}</p>
		  <p>Email: {user.email}</p>
		  {#if user.artistasFavoritos}
			<p>Artistas Favoritos: {JSON.stringify(user.artistasFavoritos)}</p>
		  {/if}
		</div>
	  {/each}
	{:catch error}
	  <p class="error">{error.message}</p>
	{/await}
  </div>
  