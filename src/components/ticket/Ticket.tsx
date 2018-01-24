import * as React from 'react';
import * as PropTypes from 'prop-types';
import './ticket.css';

export default class Ticket extends React.Component {
    constructor(props: any){
        super(props);
    }
    
    render() {      
      return (
        <div className="ticket">
            <p>Test</p>
        </div>
      );
    }
  }
  
  