import React, { useState } from 'react';
import './App.css';

function App() {
  const [toDoList, setToDoList] = useState([
    // { name: "Shopping", priority: true },
    // { name: "Clean bathroom", priority: false },
    // { name: "Book theatre tickets", priority: false }
    { name: "Shopping", priority: "high" },
    { name: "Clean bathroom", priority: "low" },
    { name: "Book theatre tickets", priority: "low" }
  ]);

  const [newToDo, setNewToDo] = useState("");
  const [newPriority, setNewPriority] = useState("");

  const handleToDoInput = (event) => {
    // event refers to the thing that's triggered a change in our app - in this case it's the change to the input in our form below
    // it then goes to the TARGET, i.e. the thing that trigerred the event (so our input field) and it grabs the VALUE that's now been put in, i.e. the updated piece of information
    setNewToDo(event.target.value)
  };

  const handlePriority = (event) => {
    setNewPriority(event.target.value);
  }

  const saveNewToDo = (event) => {
    // line 46 is something we want to put in when we create forms - this is because when a form is submitted, but default it sends a POST request to the server, however
    // in this instance we want to handle what happens when submit is hit ourselves, so we prevent the default behaviour from happening and then we tell it what to do
    // remember here we're dealing with all data changes locally, we're not communicating with the server yet!!!
    event.preventDefault();
    // we create a new list here because we don't want to be manipulating the original array - we want to work with a copy of it
    // we do this because we want to get all of our data nice and updated before we mess with the original copy in any way - we want to leave the original as a single source of 
    // truth up until we "set" the new data to it - this makes sure our data is handled all correctly
    const copyList = [...toDoList];
    copyList.push({ name: newToDo, priority: newPriority })
    // so here we are calling the setter to "set" the new list of to does - so this happens very quickly after we've created our list, but these are important steps to follow nonetheless
    setToDoList(copyList);
    setNewToDo("");
    // setNewPriority("");
    // this resets the form after we've submitted it, so same as above, after the event we go to the target (the form) and clears everything - but we still need lines 39 and 40 to fully
    // clear everything
    event.target.reset();
  };



  // in react when you use a function like map, you need to give it both the value AND its key - in this case it's the index number in the array, but it could be something like
  // an ID number if the data comes from a database
  const toDoListNotes = toDoList.map((toDo, index) => {
    return (

      <li key={index} className={toDo.priority}>{toDo.name}
        {/* {toDo.priority ?
          <div>
            <input onChange={() => setPriorityTrue(index)} type="radio" name={toDo.name} checked className="priority" id="priority" value="" />Priority
            <input onChange={() => setPriorityFalse(index)} type="radio" name={toDo.name} className="low-priority" id="low-priority" value="" />Low Priority
          </div>
          :
          <div>
            <input onChange={() => setPriorityTrue(index)} type="radio" name={toDo.name} className="priority" id="priority" value="" />Priority
            <input onChange={() => setPriorityFalse(index)} type="radio" name={toDo.name} checked className="low-priority" id="low-priority" value="" />Low Priority
          </div>} */}
      </li>

    );
  });


  // const setPriorityTrue = (index) => {
  //   const copyList = [...toDoList];
  //   copyList[index].priority = true;
  //   setToDoList(copyList);
  // }

  // const setPriorityFalse = (index) => {
  //   const copyList = [...toDoList];
  //   copyList[index].priority = false;
  //   setToDoList(copyList);
  // }


  return (
    <div className="App">
      <h1>To Do List</h1>
      <hr></hr>

      <ul>
        {toDoListNotes}
      </ul>

      <form onSubmit={saveNewToDo}>
        <label htmlFor="new-toDo">Add a new ToDo: </label>
        <input id="new-toDo" type="text" value={newToDo} onChange={handleToDoInput} />
        <label htmlFor="high">High Priority: </label>
        <input type="radio" id="high" value="high" name="priority" onChange={handlePriority} />
        <label htmlFor="lost">Low Priority: </label>
        <input type="radio" id="low" value="low" name="priority" onChange={handlePriority} />
        <input type="submit" value="Save New ToDo" />
      </form>

    </div>
  );
}

export default App;
