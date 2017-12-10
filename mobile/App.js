/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,
  Button,
  Image,
  ImageBackground
} from 'react-native';

// const instructions = Platform.select({
//   ios: 'Press Cmd+R to reload,\n' +
//     'Cmd+D or shake for dev menu',
//   android: 'Double tap R on your keyboard to reload,\n' +
//     'Shake or press menu button for dev menu',
// });

const onPressLearnMore = () => {
    console.log('pressed');
};

export default class App extends Component < {} > {
  render() {
    return (
      <View style={styles.container}>
        <ImageBackground 
          source={require('./images/background.png')}
          style={styles.backgroundColor}
        >
          <Text style={styles.welcome}>
            Welcome to Better Off Costumes!
          </Text>
          {/* <Text style={styles.instructions}>
            To get started, edit App.js
          </Text>
          <Text style={styles.instructions}>
            {instructions}
          </Text> */}
          <Button
            style={styles.button}
            onPress={onPressLearnMore}
            title="Settings"
            color="white"
            accessibilityLabel="Learn more about this purple button"/>
          <Button
            onPress={onPressLearnMore}
            title="New Costume"
            color="white"
            accessibilityLabel="Learn more about this purple button"/>
          <Button
            onPress={onPressLearnMore}
            title="Search"
            color="white"
            accessibilityLabel="Learn more about this purple button"/>
          <Button
            onPress={onPressLearnMore}
            title="Check In"
            color="white"
            accessibilityLabel="Learn more about this purple button"/>
          <Button
            onPress={onPressLearnMore}
            title="Check Out"
            color="white"
            accessibilityLabel="Learn more about this purple button"/>
        </ImageBackground>
      </View> 
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0)'
  },
  backgroundColor: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    width:'100%',
    height:'100%',
    // resizeMode: 'stretch'
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
