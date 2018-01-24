import * as React from 'react';
import App from "../App";
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';

it('renders correctly app', () => {
  const elem = shallow(<App />);
  expect(shallowToJson(elem)).toMatchSnapshot();
});