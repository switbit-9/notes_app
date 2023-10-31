import React from "react";
import { StyleSheet, View, ActivityIndicator } from "react-native";
import styles from "./styles";

function AppLoader() {
  return (
    <View style={[StyleSheet.absoluteFillObject, styles.container]}>
      <ActivityIndicator
        size="large"
        color="#0000ff"
      />
    </View>
  );
}

export default AppLoader;
