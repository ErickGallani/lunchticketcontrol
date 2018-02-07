import * as React from 'react';
import * as PropTypes from 'prop-types';
import FlatButton from 'material-ui/FlatButton';
import * as styles from './Header.css';

interface HeaderProps { title: String }

export default class Header extends React.Component<HeaderProps, {}> {
    constructor(props: HeaderProps){
        super(props);
    }
        
    render() {
        return (
            <div className={styles.title}>
                <p>{this.props.title}</p>
            </div>
        );
    }
}