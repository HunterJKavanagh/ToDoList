<script>
  import TaskCard from './lib/TaskCard.svelte';

  import NewTaskv1 from './lib/NewTaskv1.svelte';

  let result = []

  async function getTasks () {
    const res = await fetch('/getTasks', {
      method: 'GET',
    })

    const json = await res.json()
    const sjson = await JSON.stringify(json)
    result = JSON.parse(sjson)
    console.log(result)
  }

  function timeToDeadline(date, time) {
    let today = new Date()
    return Math.round((new Date(date + ' ' + time) - today) / 1000 / 60 / 60 / 24)
  }

  getTasks()
</script>

<main class="">
  <header class="bg-blue-800 text-white flex justify-between p-2 sticky top-0">
    <h1 class="text-xl">To Do List!</h1>
    <div class="text-xl">Sing Up Here!</div>
  </header>

  <body class="grid justify-items-center">
    <h2 class="text-2xl pt-4 pb-2">New Task</h2>
    <NewTaskv1 on:dbupdate={getTasks}></NewTaskv1>

    <h2 class="text-2xl pt-4 pb-2">Task List</h2>
    <div class="space-y-4">
      {#each result as r}
        <!-- <p>{r.taskName}| Length: {r.taskLength}</p> -->
        <TaskCard taskName={r.taskName} taskLength={r.taskLength} taskDescription={r.taskDescription} timeToDeadline={timeToDeadline(r.taskDate, r.taskTime)}></TaskCard>
      {/each}
    </div>
  </body>
  


</main>
