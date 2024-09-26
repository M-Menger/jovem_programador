import { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import ListToDo from './ListToDo'
import AddToDo from './AddTodo';

const App = () => {
  const [tasks, setTasks] = useState<{title: string, description: string }[]>([]);

  return (
    <Router>
      <div>
        <nav className='navBar'>
          <h1>ToDo List JP</h1>
            <ul className='main-menu'>
              <li className='itens'>
                <Link to={"/add"} className='router'> Adicionar Tarefa </Link>
              </li>
              <li className='itens'>
                <Link to={"/list"} className='router'> Ver tarefas </Link>
              </li>
            </ul>
        </nav>
        <div>
          <Routes>
            <Route path="/add" element={<AddToDo tasks={tasks} setTasks={setTasks} />}/>
            <Route path="/list" element={<ListToDo tasks={tasks} />} />
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App
