<script>
  import PopOver from './PopOver.svelte';

  import TaskCard from './lib/TaskCard.svelte';
  import NewTaskv1 from './lib/NewTaskv1.svelte';
  import Overlay from './lib/Overlay.svelte';

  
  import { createClient } from '@supabase/supabase-js'

  // Create a single supabase client for interacting with your database
  const supabase = createClient('https://wzlxhmothxekqaejfgie.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind6bHhobW90aHhla3FhZWpmZ2llIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODE4NzI2MTEsImV4cCI6MTk5NzQ0ODYxMX0.AXuwk18Bhc8C09k7V4Dmx-VBkvIEKYqkHjJLOUbfgU0')



  let result = []

  async function getTasks () {
    // const res = await fetch('/getTasks', {
    //   method: 'GET',
    // })

    // const json = await res.json()
    // const sjson = await JSON.stringify(json)
    // result = JSON.parse(sjson)

    const data = await supabase
      .from('tasks')
      .select('taskName')

    console.log(data)
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
    <!-- <PopOver></PopOver> -->
    <Overlay></Overlay>
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
