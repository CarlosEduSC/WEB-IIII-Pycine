<script>
    export let menu;
  </script>
  
  <div id="componente-nav">
    <ul>
      <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Movies</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Artista</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 3)}>Users</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 4)}>UsersList</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 5)}>FavoritesList</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 6)}>SearchMovie</a></li>
      <li><a href="/" on:click|preventDefault={() => (menu = 7)}>SearchArtist</a></li>
    </ul>
  </div>
  
  <style>
  div{
    background-color: rgb(217, 217, 217);
  }
  ul { 
    color: navy; 
    padding: 10px;
  }
  li {
    display: inline-block;
    padding-right: 10px;
  }
  </style>