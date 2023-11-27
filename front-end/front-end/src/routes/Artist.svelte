<script>
	let promise = getArtista();
  
	async function getArtista() {
	  try {
		const res = await fetch(`http://localhost:8000/artista/1100`);
		const text = await res.json();
  
		if (res.ok) {
		  return text;
		} else {
		  throw new Error(text);
		}
	  } catch (error) {
		throw new Error(`Erro na requisição: ${error.message}`);
	  }
	}
  
	function handleClick() {
	  promise = getArtista();
	}
  </script>
  
  <style>
	body {
	  font-family: 'Arial', sans-serif;
	  background-color: #f8f9fa;
	}
  
	#container {
	  max-width: 600px;
	  margin: 50px auto;
	  padding: 20px;
	  background-color: #ffffff;
	  border-radius: 8px;
	  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}
  
	button {
	  padding: 10px;
	  background-color: #007bff;
	  color: #ffffff;
	  border: none;
	  border-radius: 4px;
	  cursor: pointer;
	  transition: background-color 0.3s;
	}
  
	button:hover {
	  background-color: #0056b3;
	}
  
	.loading {
	  color: #6c757d;
	  margin-top: 20px;
	}
  
	h1 {
	  color: #343a40;
	}
  
	p {
	  color: #6c757d;
	  margin-bottom: 10px;
	}
  
	img {
	  max-width: 100%;
	  height: auto;
	  margin-top: 10px;
	  border-radius: 4px;
	}
  
	.error {
	  color: #dc3545;
	  margin-top: 20px;
	}
  </style>
  
  <div id="container">
	<button on:click={handleClick}>Get artista</button>
  
	{#await promise}
	  <p class="loading">...loading</p>
	{:then artista}
	  <h1>Artista:</h1>
	  <p>{artista.name}</p>
	  <img src={`http://image.tmdb.org/t/p/w500${artista.profile_path}`} alt="" />
	  <h1>Biografia:</h1>
	  <p>{artista.biography}</p>
	{:catch error}
	  <p class="error">{error.message}</p>
	{/await}
  </div>
  