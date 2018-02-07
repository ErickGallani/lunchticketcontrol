import * as React from 'react';
import { BrowserRouter, Route, Switch, Link, NavLink } from 'react-router-dom';
import Header from '../components/header/Header';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Header title="Header" />
      <Switch>
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;