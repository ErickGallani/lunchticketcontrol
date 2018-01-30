import * as React from 'react';
import * as PropTypes from 'prop-types';
import FlatButton from 'material-ui/FlatButton';
import * as styles from './Header.css';

export default class Header extends React.Component {
    constructor(props: any){
        super(props);
    }
        
    render() {
        return (
            <div className={styles.title}>
                <p>Header</p>
            </div>
        );
    }
}