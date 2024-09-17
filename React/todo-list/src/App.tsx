import linkedin from './assets/linkedin-logo.png'
import gitHub from './assets/github-logo.png'
import './App.css'
import FormToDo from './FormToDo'

function App() {

  return (
    <>
      <h1>Todo List</h1>
      <div className="card">
        <FormToDo/>
      </div>

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <div>
        <a href="https://github.com/M-Menger" target="_blank">
          <img src={gitHub} className="logo GitHub" alt="GitHub Logo" />
        </a>
        <a href="https://www.linkedin.com/in/matheus-menger-da-silva-20a3a0246/" target="_blank">
          <img src={linkedin} className="logo Linkedin" alt="Linkedin Logo" />
        </a>
      </div>
    </>
  )
}

export default App
