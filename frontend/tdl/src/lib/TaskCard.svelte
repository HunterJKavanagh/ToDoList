<script>
    export let taskName = null
    export let taskLength = null
    export let timeToDeadline = null
    export let taskDescription = null

    let bgcolor = 'bg-blue-800'

    if (timeToDeadline != null) {
        if( timeToDeadline < 1 ){
            bgcolor = 'bg-red-800'
        } else if( timeToDeadline < 2 ){
            bgcolor = 'bg-yellow-500'
        } else if( timeToDeadline < 5 ){
            bgcolor = 'bg-green-800'
        }
    }

</script>

<div>
    <div class="{bgcolor} w-80 p-4 rounded-t-2xl shadow-xl text-white text-xl grid space-y-2">
        <div class="flex">
            <h1 class="basis-3/5">Project</h1>
            <div class="grid grid-cols-2 basis-2/5">
                <h1 class="">{taskLength}h</h1>
                <h1 class="justify-self-end">{timeToDeadline}d</h1>
            </div>
        </div>
        <div class="text-xs grid justify-center">
            <h3>{taskName}</h3>
        </div>
    </div>
    <div class="bg-gray-100 w-80 pb-4 px-4 rounded-b-2xl shadow-xl grid">
        {taskDescription}
    </div>
</div>

