<script>
	/* iniciar o servidor:
	npm run dev 
	*/
	  let promise = getArtista();
	  async function getArtista() {
	  // faz um request GET para endpoint /filmes
		  const res = await fetch(`http://localhost:8000/artista/1100`);
		  const text = await res.json();
		  if (res.ok) { return text; } 
	  else { throw new Error(text);}
	  }
	  function handleClick() {
		  promise = getArtista();
	  }
  </script>
  
  <button on:click={handleClick}> Get artista </button>
  
  {#await promise}
	  <p>...loading</p>
  {:then artista}
	<h1>Artista: </h1> <p>{artista.name}</p>
	<h1>Biofrafia: </h1> <p>{artista.biography}</p>
    <img src="http://image.tmdb.org/t/p/w500{artista.profile_path}" alt=""/>
  {:catch error}
	  <p style="color: red">{error.message}</p>
  {/await}