<script>
    export let taskName = null
    export let taskLength = null
    export let timeToDeadline = null
    export let taskDescription = null
</script>

<div>
    <div class="bg-blue-800 w-80 p-4 rounded-t-2xl shadow-xl flex text-white text-xl">
        <h1 class="basis-3/5">{taskName}</h1>
        <div class="grid grid-cols-2 basis-2/5">
            <h1 class="">{taskLength}h</h1>
            <h1 class="justify-self-end">{timeToDeadline}d</h1>
        </div>
    </div>
    <div class="bg-gray-100 w-80 pb-4 px-4 rounded-b-2xl shadow-xl grid">
        {taskDescription}
    </div>
</div>

