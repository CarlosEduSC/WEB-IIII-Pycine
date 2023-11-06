<script>
	/* iniciar o servidor:
	npm run dev 
	*/
	  let promise = getUsers();
	  async function getUsers() {
	  // faz um request GET para endpoint /users
		  const res = await fetch(`http://localhost:8000/users`);
		  const text = await res.json();
		  if (res.ok) { return text; } 
	  else { throw new Error(text);}
	  }
	  function handleClick() {
		  promise = getUsers();
	  }
  </script>
  
  <button on:click={handleClick}> Get Users </button>
  
  {#await promise}
	  <p>...loading</p>
  {:then users}
	<h1>Lista de usuários</h1>
    {#each users as user}
        <p>{user.id}</p>
        <p>{user.email}</p>
    {/each}
  {:catch error}
	  <p style="color: red">{error.message}</p>
  {/await}