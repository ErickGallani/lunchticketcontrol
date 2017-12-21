import React, { Component } from 'react';
import Header from "../Header";
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';

test('renders correctly headr', () => {
  const elem = shallow(<Header />);
  expect(shallowToJson(elem)).toMatchSnapshot();
});