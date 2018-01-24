import * as React from 'react';
import * as PropTypes from 'prop-types';
import FlatButton from 'material-ui/FlatButton';
import './header.css';

export default class Header extends React.Component {
    constructor(props: any){
        super(props);
    }
    
    render() {
        return (
            <div className="header">
                <p>Header</p>
            </div>
        );
    }
}