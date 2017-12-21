import { createStore, combineReducers } from 'redux';

function temporary(state = [], action) {}

export default () => {
  const store = createStore(temporary);

  return store;
};