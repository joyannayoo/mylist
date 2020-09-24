import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
// import HOCWrapper from '../../HOC';
// import store from "../../store";
import SignUp from '../SignUp';

// fetches the token from the localStorage and saves it in the state
// const token = localStorage.getItem('token');
// if (token) {
//   store.dispatch(loginAction(token))
// }

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/signup" component={ SignUp }/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
