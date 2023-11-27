<script>
  export let menu;
</script>

<div id="componente-nav">
  <ul class="navbar">
    <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Movies</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Artista</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 3)}>Users</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 4)}>UsersList</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 5)}>FavoritesMoviesList</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 6)}>SearchMovie</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 7)}>SearchArtist</a></li>
    <li><a href="/" on:click|preventDefault={() => (menu = 8)}>FavoritesArtistsList</a></li>
  </ul>
</div>

<style>
  body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
  }

  #componente-nav {
    background-color: #f8f9fa;
    padding: 10px;
  }

  .navbar {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  li {
    display: inline-block;
    margin-right: 10px;
  }

  a {
    text-decoration: none;
    color: #007bff;
    font-weight: bold;
    padding: 8px 15px;
    border-radius: 4px;
    transition: background-color 0.3s;
  }

  a:hover {
    background-color: #0056b3;
    color: #ffffff;
  }
</style>
