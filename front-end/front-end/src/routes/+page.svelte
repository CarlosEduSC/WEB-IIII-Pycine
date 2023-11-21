
<script>
    let user_id = 1; // Defina o user_id conforme necessário

    let menu = 1;
    import Movie from "./Movie.svelte"
    import Artist from "./Artist.svelte"
    import Nav from "./Nav.svelte"
    import User from "./User.svelte"
    import UserList from "./UserList.svelte";
    import UserFavorites from "./UserFavorites.svelte";
    import { onMount } from 'svelte';
    import SearchMovie from "./SearchMovie.svelte";
    import SearchArtist from "./SearchArtist.svelte";

    let filmes = [];

    onMount(async () => {
        try {
            const response = await fetch('http://localhost:8000/filmes');
            const data = await response.json();
            filmes = data;
        } catch (error) {
            console.error('Erro ao obter filmes:', error);
        }
    });

    function handleClick(filme) {
        console.log('Filme selecionado:', filme.title);
    }
</script>

<Nav bind:menu/>

<div class="card">
    {#if menu == 1}
        <Movie/>
    {:else if menu == 2}
        <Artist/>
    {:else if menu == 3}
        <User/>
    {:else if menu == 4}
        <UserList/>
    {:else if menu == 5}
        <UserFavorites user_id={user_id}/>
    {:else if menu == 6}
        <SearchMovie/>
    {:else if menu == 7}
        <SearchArtist/>
    {/if}
</div>