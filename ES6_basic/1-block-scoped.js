export default function taskBlock(trueOrFalse) {
	let task = false;  // Declare and initialize task with false
	let task2 = true;   // Declare and initialize task2 with true
  
	if (trueOrFalse) {
	  task = true;     // Assign a new value to task
	  task2 = false;   // Assign a new value to task2
	}
  
	return [task, task2];  // Return the values of task and task2
  }
  