import * as React from 'react';
import Header from "../Header";
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';

it('renders correctly headr', () => {
  const elem = shallow(<Header title="test" />);
  expect(shallowToJson(elem)).toMatchSnapshot();
});