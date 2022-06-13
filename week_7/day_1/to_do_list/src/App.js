import React, { useState } from 'react';
import './App.css';

function App() {
  const [toDoList, setToDoList] = useState([
    { name: "Shopping", priority: true },
    { name: "Clean bathroom", priority: false },
    { name: "Book theatre tickets", priority: false }
  ]);

  const [newToDo, setNewToDo] = useState("");

  const toDoListNotes = toDoList.map((toDo, index) => {
    return (

      <li key={index} className={toDo.priority ? "priority" : "low-priority"}>

        <span>{toDo.name}</span>

        {toDo.priority ?
          <div>
            <input onChange={() => setPriorityTrue(index)} type="radio" name={toDo.name} checked className="priority" id="priority" value="" />Priority
            <input onChange={() => setPriorityFalse(index)} type="radio" name={toDo.name} className="low-priority" id="low-priority" value="" />Low Priority
          </div>
          :
          <div>
            <input onChange={() => setPriorityTrue(index)} type="radio" name={toDo.name} className="priority" id="priority" value="" />Priority
            <input onChange={() => setPriorityFalse(index)} type="radio" name={toDo.name} checked className="low-priority" id="low-priority" value="" />Low Priority
          </div>}

      </li>

    );
  });

  const handleToDoInput = (event) => {
    setNewToDo(event.target.value)
  };

  const saveNewToDo = (event) => {
    event.preventDefault();
    const copyList = [...toDoList];
    copyList.push({ name: newToDo, priority: false })
    setToDoList(copyList);
    setNewToDo("");
  };

  const setPriorityTrue = (index) => {
    const copyList = [...toDoList];
    copyList[index].priority = true;
    setToDoList(copyList);
  }

  const setPriorityFalse = (index) => {
    const copyList = [...toDoList];
    copyList[index].priority = false;
    setToDoList(copyList);
  }



  return (
    <div className="App">
      <h1>To Do List</h1>
      <hr></hr>

      <ul>
        {toDoListNotes}
      </ul>

      <form onSubmit={saveNewToDo}>
        <label htmlFor="new-toDo">Add a new ToDo: </label>
        <input id="new-ToDo" type="text" value={newToDo} onChange={handleToDoInput} />
        <input type="submit" value="Save New ToDo" />
      </form>

    </div>
  );
}

export default App;
