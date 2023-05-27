<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();




  let taskName = null
  let taskLength = null
  let taskDate = null
  let taskTime = null
  let taskDescription = null
  let result = null

  async function postTask () {
    // const res = await fetch('/postTask', {
    //   method: 'POST',
    //   body: JSON.stringify({
    //     taskName,
    //     taskLength,
    //     taskDate,
    //     taskTime,
    //     taskDescription,
    //   })
    // })

    // const json = await res.json()
    // result = JSON.stringify(json)
    // console.log(result)

    const {error} = await supabase
      .from('tasks')
      .insert({taskName, taskLength, taskDate, taskTime, taskDescription})

    dispatch('dbupdate');

    taskName = null
    taskLength = null
    taskDate = null
    taskTime = null
    taskDescription = null
    result = null
  }
</script>

<div class="grid border-dashed rounded-2xl w-80 border-2 p-2 space-y-2 ">
    <input bind:value={taskName} placeholder="Task Name" maxlength="10">
    <input bind:value={taskLength} placeholder="Task Length">
    <div class="flex justify-between">
      <input type="date" bind:value={taskDate}>
      <input type="time" bind:value={taskTime}>
    </div>
    <textarea bind:value={taskDescription} placeholder="Task Description" cols="30" rows="2" class="border-2 rounded-xl p-1"></textarea>
    <button type="button" on:click={postTask} class="bg-gray-200 rounded-2xl">POST</button>
</div>


