<script>

</script>



<div class="bg-gray-100 w-80 p-4 rounded-2xl shadow-xl grid">
    <div class="text-lg">
       <slot name="taskName">Task Name</slot>
    </div>
    <div class="flex space-x-1"><p>Length:</p><div><slot name="taskLength">#</slot></div></div>
</div>

