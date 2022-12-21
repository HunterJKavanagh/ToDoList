<script>
  // const { default: axios } = require('axios');
  import Counter from './lib/Counter.svelte'

  let task_name = '';

	async function postTask () {
		const res = await fetch('/addTask', {
			method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
			body: JSON.stringify({
				name: task_name,
			})
		})

	}
</script>

<main class="grid justify-items-center">
  <h1 class="text-4xl">To Do List!</h1>

  <div class="grid grid-cols-2">
    <input type="text" placeholder="enter your name" bind:value={task_name}/>
    <button class="" on:click={postTask}>POST</button>
  </div>

  <form method="POST" action="/addTask">
    <label for="taskName">Task Name</label>
    <input type="text" id="taskName" name="taskName"/>
    <div>
      <label for="taskName">Task Name</label>
      <input type="text" id="taskName" name="taskName"/>
    </div>
    <div>
      <label for="dueDate">Due Date</label>
      <input type="date" id="dueDate" name="dueDate"/>
      <input type="time" id="time" name="time"/>
    </div>
    <div>
      <label for="taskLength">Task Length</label>
      <input type="number" id="taskLength" name="taskLength"/>
    </div>
    <button  type="submit">Submit</button>
  </form>

</main>
