import logo from './logo.svg';
import './App.css';
import {Todos} from './components/index'
import {Route} from 'react-router-dom'


const App = () => {
  return(<>

  <Route exact path='/' component={Todos}/>
  </>
  )
}

export default App;
