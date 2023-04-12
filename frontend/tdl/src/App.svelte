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

  getTasks ()
</script>

<main class="">
  <header class="bg-blue-500 text-white grid p-12">
    <h1 class="text-4xl place-self-center">To Do List!</h1>
  </header>

  <body class="grid justify-items-center">
    <NewTaskv1 on:dbupdate={getTasks}></NewTaskv1>

    <div class="space-y-8">
      {#each result as r}
        <!-- <p>{r.taskName}| Length: {r.taskLength}</p> -->
        <TaskCard>
          <p slot="taskName">{r.taskName}</p>
          <p slot="taskLength">{r.taskLength}</p>
        </TaskCard>
      {/each}
    </div>
  </body>
  


</main>
