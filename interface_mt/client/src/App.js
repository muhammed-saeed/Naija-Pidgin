import React from "react"
// import { Container, AppBar, Typography, Grow, Grid } from "@material-ui/core";
import { Container, AppBar, Typography, Grow, Grid } from '@mui/material';

import memories from "./images/naija.jpg"
import Posts from "./components/Posts/Posts"
import Form from "./components/Form/Form"

import useStyles from './styles'



const App =() => {
    const classes = useStyles();
    return (
        <Container maxwidth="lg">
            <AppBar position="static" color="inherit" className={classes.appBar}>
                <Typography variants="h2" className={classes.heading} >Memories</Typography>
                <img className={classes.image} src={memories} alt="memories" height="200"/>
            </AppBar>
            <Grow in>
                <Container>
                    <Grid container justify="space-between" alignItems="stretch" spacing={3}>
                        <Grid item xs={12} sm={7}>
                            <Posts />
                        </Grid>
                        <Grid item xs={12} sm={4}>
                            <Form />
                        </Grid>
                    </Grid>
                </Container>
            </Grow>
        </Container>
    )
}

export default App;
// each react front-end component has to have 