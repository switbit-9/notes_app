import React from 'react';
import { View, Text, Button } from 'react-native';

const ErrorPage = ({ message, onRetry }) => (
  <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
    <Text>Error: {message}</Text>
    <Button title="Retry" onPress={onRetry} />
  </View>
);

export default ErrorPage;