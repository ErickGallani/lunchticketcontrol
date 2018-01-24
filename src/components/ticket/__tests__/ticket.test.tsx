import * as React from 'react';
import Ticket from "../Ticket";
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';

it('renders correctly ticket', () => {
  const elem = shallow(<Ticket />);
  expect(shallowToJson(elem)).toMatchSnapshot();
});