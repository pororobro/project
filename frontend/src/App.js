import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, SignUp, UserDetail, UserEdit,UserList  } from './user'
import { Home, User, Counter, Article } from './templates'
import { Nav } from './common'
import { BrowserRouter as Router } from 'react-router-dom'
import { todoReducer } from './store'
import { createStore, combineReducers} from 'redux'
import { Provider } from 'react-redux'
import { TodoList } from 'todos/components'
const rootReducer = combineReducers({todoReducer})

const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
    <Nav/>
     <Route exact path = '/login-form' component={Login}/>
     <Route exact path = '/signup-form' component={SignUp}/>
     <Route exact path = '/user-remove' component={UserDetail}/>
     <Route exact path = '/user-modify' component={UserEdit}/>
     <Route exact path = '/user-detail' component={UserList}/>
     <Route exact path = '/home' component={Home}/>
     <Route exact path = '/user' component={User}/>
     <Route exact path = '/conter' component={Counter}/>
     <Route exact path = '/article' component={Article}/>
     <Route exact path = '/todos' component={TodoList}/>

      </Provider>
    </Router>
  </div>)
}

export default App