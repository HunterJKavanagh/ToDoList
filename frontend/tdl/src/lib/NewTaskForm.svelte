<script>
  // const { default: axios } = require('axios');
</script>

<form method="POST" action="/addTask" class="border-dashed border-2 p-2 m-2">
  <div class="pb-1">
    <label for="taskName">Task Name</label>
    <input type="text" id="taskName" name="taskName"/>
  </div>
  <div class="pb-1">
    <label for="dueDate">Due Date</label>
    <input type="date" id="dueDate" name="dueDate"/>
    <input type="time" id="time" name="time"/>
  </div>
  <div class="pb-1">
    <label for="taskLength">Task Length</label>
    <input type="number" id="taskLength" name="taskLength"/>
  </div>
  <div class="grid bg-gray-200 pb-1">
    <button class="border-2 justify-self-stretch text-center" type="submit">Submit</button>
  </div>
</form>

