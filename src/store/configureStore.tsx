import { createStore, combineReducers } from 'redux';

function temporary(state: any[] = [], action: any): any { }

export default () => {
  const store = createStore(temporary);

  return store;
};