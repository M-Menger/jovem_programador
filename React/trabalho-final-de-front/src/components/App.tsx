import './App.css'
import { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import ListToDo from './ListToDo'
import AddToDo from './AddTodo';

const App = () => {
  const [tasks, setTasks] = useState<{title: string, description: string }[]>([]);

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to={"/add"}> Adicionar Tarefa </Link>
            </li>
            <li>
              <Link to={"/list"}> Ver tarefas </Link>
            </li>
          </ul>
        </nav>
          <Routes>
            <Route path="/add" element={<AddToDo tasks={tasks} setTasks={setTasks} />}/> 
            <Route path="/list" element={<ListToDo tasks={tasks} />} />
          </Routes>
        </div>
    </Router>
  )
}

export default App
