import React from 'react'
import {Route} from 'react-router-dom'
import { Counter, Todo} from './components/index'
const App = () => {
  return (<>
    
    <Route exact path='/' component={Counter}/>
    <Route exact path='/todo' component={Todo}/>
   
  </>
  );
}
export default App;

