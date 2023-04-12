<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();


  let taskName = null
  let taskLength = null
  let result = null

  async function postTask () {
    const res = await fetch('/postTask', {
      method: 'POST',
      body: JSON.stringify({
        taskName,
        taskLength,
      })
    })

    const json = await res.json()
    result = JSON.stringify(json)

    dispatch('dbupdate');
  }
</script>

<div class="grid border-dashed rounded-2xl w-80 border-2 p-2 m-2 space-y-2 ">
    <input bind:value={taskName} placeholder="Task Name">
    <input bind:value={taskLength} placeholder="Task Length">
    <button type="button" on:click={postTask} class="bg-gray-200">POST</button>
</div>

