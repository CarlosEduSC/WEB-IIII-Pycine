<script>
  let resposta = "";

  async function sendForm(e) {
    try {
      let formData = new FormData(e.target);
      let data = Object.fromEntries(formData.entries());
      const res = await fetch('http://localhost:8000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      const json = await res.json();
      resposta = JSON.stringify(json);
    } catch (error) {
      resposta = `Erro ao enviar o formulário: ${error.message}`;
    }
  }
</script>

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
  }

  #container {
    max-width: 400px;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  h2 {
    color: #343a40;
    margin-bottom: 20px;
  }

  p {
    color: #28a745;
    margin-bottom: 10px;
  }

  form.crud {
    display: grid;
    gap: 10px;
    row-gap: 15px;
  }

  input[type="text"],
  input[type="password"] {
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 4px;
    width: 100%;
  }

  input[type="submit"] {
    padding: 10px;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  input[type="submit"]:hover {
    background-color: #0056b3;
  }

  .error {
    color: #dc3545;
    margin-top: 10px;
  }
</style>

<div id="container">
  <h2>New user</h2>

  <p>{resposta}</p>

  <form class="crud" on:submit|preventDefault={sendForm}>
    <input type="text" name="name" placeholder="User name" required autocomplete="off">
    <input type="text" name="email" placeholder="Email" required autocomplete="off">
    <input type="password" name="password" placeholder="Password" required autocomplete="off">
    <input type="submit" value="Add">
  </form>
</div>
