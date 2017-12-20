import React, { Component } from 'react';
import App from "../App";
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';

test('renders correctly app', () => {
  const elem = shallow(<App />);
  expect(shallowToJson(elem)).toMatchSnapshot();
});